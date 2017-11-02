#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.certification.initialize request
:author: auto create
:date: 2017-05-31 10:19:55
'''


class ZhimaCustomerCertificationInitializeRequest:
    def __init__(self):
        self.__bizCode = '' # 认证场景码，支持的场景码有：FACE：多因子活体人脸认证，SMART_FACE：多因子快捷活体人脸认证，FACE_SDK：SDK活体人脸认证签约的协议决定了可以使用的场景
        self.__extBizParam = '' # 扩展业务参数，暂时没有用到，接口预留
        self.__identityParam = '' # 值为一个json串，无入参时值为"{}"，有入参时必须指定身份类型identity_type，不同的身份类型对应的身份信息不同当前支持：身份信息为证件信息，identity_type值为CERT_INFO：证件类型为身份证cert_type值为IDENTITY_CARD，必要信息cert_name和cert_no；身份信息为短信手机号，适用于短信认证，identity_type值为SMS_MOBILE_NO：证件类型可以为空，当证件类型为身份证cert_type值为IDENTITY_CARD，必要信息cert_name和cert_no，mobile_no可以为空，以上信息没有传入的时候会上用户录入；身份信息为支付宝UID，identity_type值为USER_ID:必要信息user_id示例：{"identity_type": "USER_ID", "user_id": "2088172637486509"}
        self.__merchantConfig = '' # 认证商户自定义配置，支持一些商户可选的功能need_user_authorization： 值为true或者false当值为true时，在认证用户引导页会展示用户授权协议，在认证通过后会进行授权，但是授权是否成功不影响认证结果
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
        return "zhima.customer.certification.initialize"

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
