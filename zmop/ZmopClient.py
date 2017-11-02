#!/usr/bin/python
# encoding=utf-8
'''
依赖包：
1.M2Crypto（加解密，加验签）
2.requests（post请求）
'''
import logging, time, os, json
from logging import handlers
from RSAUtil import *
from WebUtil import *


class ZmopClient():
    def __init__(self, gatewayUrl, appid, charset, privateKeyFilePath, zhiMaPublicKeyFilePath):
        self.appid = appid
        self.privateKeyFilePath = privateKeyFilePath
        self.zhiMaPublicKeyFilePath = zhiMaPublicKeyFilePath
        self.gatewayUrl = gatewayUrl
        self.format = "json"
        self.apiVersion = "1.0"
        self.charset = charset
        self.__signType = "RSA"
        self.__signParam = 'sign'
        self.__bizParam = "params"
        self.logDir = ""  # 日志路径，留空则不启用日志
        self.logSeparator = " | "  # 日志分隔符
        self.logRequest = False  # 是否记录请求

    def execute(self, request):
        # 获取业务参数
        apiParamsQuery = self.getBizParamStr(request)
        # 获取系统参数
        sysParams = self.getSystemParams(request)
        # 业务参数加签到系统参数内
        sysParams[self.__signParam] = sign(self.privateKeyFilePath, apiParamsQuery)
        # 业务参数加密
        encryptedApiParams = {self.__bizParam: rsaEncrypt(self.zhiMaPublicKeyFilePath, apiParamsQuery)}
        # 如果有上传文件则把文件参数放到加密串
        files = request.getFileParas()
        if (files):
            for (key, value) in files.iteritems():
                encryptedApiParams[key] = (
                    os.path.basename(value), open(value, 'rb'), 'application/json', {'Expires': '0'})
        # 拼装requestURL
        requestUrl = self.gatewayUrl + "?" + buildQueryWithEncode(sysParams)
        # 发起请求
        try:
            resp = curl(requestUrl, encryptedApiParams)
            if self.logRequest:
                self.__logInfo('request', 'RequestUrl:%s%sContent:%s' % (
                    requestUrl, self.logSeparator, json.dumps(encryptedApiParams)))
        except ValueError, e:
            self.__logInfo('comm', '%s%s%s%sHTTP_ERROR:%s' % (
                sysParams['method'], self.logSeparator, requestUrl, self.logSeparator, e))
            raise ValueError("CurlError:%s" % (e))

        # 解析ZMOP返回
        respWellFormed = False
        if self.format == "json":
            respDic = json.loads(resp)
            biz_response = self.get_biz_response(respDic)
            encrypted = respDic['encrypted']
            if encrypted:
                biz_response = rsaDecrypt(self.privateKeyFilePath, biz_response)
            bizRespDic = json.loads(biz_response)
            if respDic:
                respWellFormed = True

        # HTTP文本不是json
        if respWellFormed == False:
            self.__logInfo('comm', '%s%s%s%sHTTP_RESPONSE_NOT_WELL_FORMED:%s' % (
                sysParams['method'], self.logSeparator, requestUrl, self.logSeparator, resp))
            raise ValueError("Response format is not json:%s" % (resp))

        # 验签
        if 'biz_response_sign' in respDic.keys():
            bizResponseSign = respDic['biz_response_sign']
            verifyResult = verify(self.zhiMaPublicKeyFilePath, biz_response, bizResponseSign)
            if verifyResult == False:
                raise ValueError("验签失败:%s" % (resp))

        # ZMOP返回错误码的话记录到业务错误日志中
        if 'error_code' in bizRespDic.keys():
            self.__logInfo('biz', resp)

        return bizRespDic

    def generatePageRedirectInvokeUrl(self, request):
        '''
        对于page_redirect类型的接口调用,生成用来调用这种类型接口的url,便于在浏览器中使用
        :param request:请求
        :return str: 浏览器访问的url
        '''
        apiParamsQuery = self.getBizParamStr(request)
        systemParams = self.getSystemParams(request)
        systemParams[self.__signParam] = sign(self.privateKeyFilePath, apiParamsQuery)
        systemQueryParams = buildQueryWithEncode(systemParams)

        bizParam = rsaEncrypt(self.zhiMaPublicKeyFilePath, apiParamsQuery)
        url = self.gatewayUrl + '?' + systemQueryParams + '&' + self.__bizParam + '=' + quote(bizParam)
        return url

    def decryptAndVerifySign(self, encryptedResponse, sign):
        '''
        解密验签
        1.先解密，再验签
        2.如果验签成功，则返回解密后的值
        3.如果验签失败，则抛出异常
        :param encryptedResponse: 返回值中的加密串
        :param sign: 返回值中的签名串
        :return str: 解密后的明文
        '''
        decryptedResponse = rsaDecrypt(self.privateKeyFilePath, encryptedResponse)
        success = verify(self.zhiMaPublicKeyFilePath, decryptedResponse, sign)
        if success:
            return decryptedResponse
        else:
            raise ValueError("验签失败:%s" % (decryptedResponse))

    def generateSign(self, request):
        '''
        业务参数签名
        :param request:请求
        :return str: 签名串
        '''
        paramStr = self.getBizParamStr(request)
        return sign(self.privateKeyFilePath, paramStr)

    def generateSignWithUrlEncode(self, request):
        '''
        业务参数签名和urlencode
        :param request:  请求
        :return: urlencode(signStr)
        '''
        paramSignStr = self.generateSign(request)
        return quote(paramSignStr)

    def generateEncryptedParam(self, request):
        '''
        业务参数加密
        :param request: 请求
        :return str: 加密串
        '''
        paramStr = self.getBizParamStr(request)
        return rsaEncrypt(self.zhiMaPublicKeyFilePath, paramStr)

    def generateEncryptedParamWithUrlEncode(self, request):
        '''
        业务参数加密和urlencode
        :param request: 请求
        :return str: urlencode(encryptedStr)
        '''
        paramEncryptedStr = self.generateEncryptedParam(request)
        return quote(paramEncryptedStr)

    def get_biz_response(self, dic):
        '''
        获取返回中的业务参数
        :param dic: 返回结果
        :return str: 以_response结尾的key对应的value
        '''
        for (key, value) in dic.iteritems():
            if key[-9:] == '_response':
                return value
        return ''

    def getBizParamStr(self, request):
        '''
        获取业务参数
        :param request:请求
        :return str: apiParamsQuery
        '''
        apiParams = request.getApiParas()
        apiParamsQuery = buildQueryWithEncode(apiParams)
        return apiParamsQuery

    def getSystemParams(self, request):
        '''
        获取系统参数
        :param request: 请求
        :return dic: sysParams
        '''
        # 没有给charset则给出默认
        if not checkEmpty(self.charset):
            self.charset = 'UTF-8'

        # 没有给api_ver则给出默认
        ver = ''
        if not checkEmpty(request.getApiVersion()):
            ver = request.getApiVersion()
        else:
            ver = self.apiVersion

        # 拼装参数
        sysParams = {}
        sysParams['app_id'] = self.appid
        sysParams['version'] = ver
        sysParams['method'] = request.getApiMethodName()
        sysParams['charset'] = self.charset
        sysParams['scene'] = request.getScene()
        sysParams['channel'] = request.getChannel()
        sysParams['platform'] = request.getPlatform()
        sysParams['ext_params'] = request.getExtParams()
        return sysParams

    def __logInfo(self, logType, message):
        '''
        错误日志
        :param logType: 日志类型：
        1.biz业务日志
        2.comm通信错误
        3.request请求日志
        :param message: 日志内容
        '''
        if self.logDir == '':  # 目录没有配置则不使用日志功能
            return

        if not os.path.exists(self.logDir):  # 目录是否存在
            raise ValueError('logDirectory does not exist: %s' % (self.logDir))

        if self.logDir[-1:] != '/':  # 目录是否以/结尾
            self.logDir = self.logDir + '/'

        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if logType == 'biz':  # 业务错误
            LogFile = self.logDir + 'zmop_biz_err_' + self.appid + '_' + date + '.log'
        elif logType == 'comm':  # 通信错误
            LogFile = self.logDir + 'zmop_comm_err_' + self.appid + '_' + date + '.log'
        elif logType == 'request':  # 请求日志
            LogFile = self.logDir + 'zmop_request_' + self.appid + '_' + date + '.log'
        else:
            raise ValueError('logType_Error: %s' % (logType))

        handler = logging.handlers.RotatingFileHandler(LogFile, maxBytes=1024 * 1024, backupCount=5)
        fmt = '%(asctime)s' + self.logSeparator + '%(message)s'
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        logger = logging.getLogger(LogFile)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        logger.info(message)
