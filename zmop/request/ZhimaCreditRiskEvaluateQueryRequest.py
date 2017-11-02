#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.risk.evaluate.query request
:author: auto create
:date: 2017-09-21 13:15:15
'''


class ZhimaCreditRiskEvaluateQueryRequest:
    def __init__(self):
        self.__certNo = '' # 证件号。当证件类型为身份证时，cert_no为身份证号
        self.__certType = '' # 证件类型 目前支持两种IDENTITY_CARD(身份证),ALIPAY_USER_ID(支付宝uid)
        self.__extendInfo = '' # 扩展参数，供提供更多信息给规则引擎做风险判断。以JSON字符串形式配置
        self.__name = '' # 姓名，当传入cert_type类型为IDENTITY_CARD时该值为必传项
        self.__productCode = '' # 产品码
        self.__ruleId = '' # ISV商户传入二级商户APPID普通商户传入自身APPID
        self.__sceneCode = '' # 标识对接业务场景，业务场景下商户可做自定义策略配置
        self.__transactionId = '' # 芝麻业务凭证，详见https://b.zmxy.com.cn/technology/openDoc.htm?id=334

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setCertNo(self, certNo):
        self.__certNo = certNo
        self.__apiParas["cert_no"] = certNo

    def getCertNo(self):
        return self.__certNo

    def setCertType(self, certType):
        self.__certType = certType
        self.__apiParas["cert_type"] = certType

    def getCertType(self):
        return self.__certType

    def setExtendInfo(self, extendInfo):
        self.__extendInfo = extendInfo
        self.__apiParas["extend_info"] = extendInfo

    def getExtendInfo(self):
        return self.__extendInfo

    def setName(self, name):
        self.__name = name
        self.__apiParas["name"] = name

    def getName(self):
        return self.__name

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setRuleId(self, ruleId):
        self.__ruleId = ruleId
        self.__apiParas["rule_id"] = ruleId

    def getRuleId(self):
        return self.__ruleId

    def setSceneCode(self, sceneCode):
        self.__sceneCode = sceneCode
        self.__apiParas["scene_code"] = sceneCode

    def getSceneCode(self):
        return self.__sceneCode

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def getApiMethodName(self):
        return "zhima.credit.risk.evaluate.query"

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
