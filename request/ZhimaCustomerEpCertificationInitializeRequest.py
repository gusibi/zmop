#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.ep.certification.initialize request
:author: auto create
:date: 2017-07-27 20:20:02
'''


class ZhimaCustomerEpCertificationInitializeRequest:
    def __init__(self):
        self.__bizCode = '' # 认证场景码，支持的场景码有： EP_ALIPAY_ACCOUNT,  签约的协议决定了可以使用的场景
        self.__extBizParam = '' # 扩展业务参数，暂时没有用到，接口预留
        self.__identityParam = '' # 值为一个json串，无入参时值为"{}"，有入参时必须指定身份类型identity_type，不同的身份类型对应的身份信息不同 当前支持的身份信息为证件信息，identity_type=EP_CERT_INFO  需要输入法人证件三要素，企业证件三要素，如 {"identity_type": "EP_CERT_INFO", "cert_type": "IDENTITY_CARD", "cert_name": "收委", "cert_no":"260104197909275964", "ep_cert_type": "NATIONAL_LEGAL_MERGE", "ep_cert_name": "xxx有限公司", "ep_cert_no":"260104199909275964"}； 特别备注： 上述json串中的 ep_cert_type 属性仅支持2种类型：NATIONAL_LEGAL：工商注册号类型NATIONAL_LEGAL_MERGE ： 社会统一信用代码类型
        self.__merchantConfig = '' # 认证商户自定义配置，支持一些商户可选的功能,目前为预留的属性值
        self.__productCode = '' # 芝麻认证产品码,示例值为真实的产品码
        self.__transactionId = '' # 商户请求的唯一标志，32位长度的字母数字下划线组合。该标识作为对账的关键信息，商户要保证其唯一性.建议:前面几位字符是商户自定义的简称,中间可以使用一段日期,结尾可以使用一个序列

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizCode(self, bizCode):
        self.__bizCode = bizCode
        self.__apiParas["biz_code"] = bizCode

    def getBizCode(self):
        return self.__bizCode

    def setExtBizParam(self, extBizParam):
        self.__extBizParam = extBizParam
        self.__apiParas["ext_biz_param"] = extBizParam

    def getExtBizParam(self):
        return self.__extBizParam

    def setIdentityParam(self, identityParam):
        self.__identityParam = identityParam
        self.__apiParas["identity_param"] = identityParam

    def getIdentityParam(self):
        return self.__identityParam

    def setMerchantConfig(self, merchantConfig):
        self.__merchantConfig = merchantConfig
        self.__apiParas["merchant_config"] = merchantConfig

    def getMerchantConfig(self):
        return self.__merchantConfig

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def getApiMethodName(self):
        return "zhima.customer.ep.certification.initialize"

    def setScene(self, scene):
        self.__scene = scene

    def getScene(self):
        return self.__scene

    def setChannel(self, channel):
        self.__channel = channel

    def getChannel(self):
        return self.__channel

    def setPlatform(self, platform):
        self.__platform = platform

    def getPlatform(self):
        return self.__platform

    def setExtParams(self, extparams):
        self.__extParams = extparams

    def getExtParams(self):
        return self.__extParams

    def getApiParas(self):
        return self.__apiParas

    def getFileParas(self):
        return self.__fileParas

    def setApiVersion(self, apiversion):
        self.__apiVersion = apiversion

    def getApiVersion(self):
        return self.__apiVersion
