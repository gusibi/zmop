#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.scene.creditpay.bizriskeval.query request
:author: auto create
:date: 2017-07-20 22:17:50
'''


class ZhimaMerchantSceneCreditpayBizriskevalQueryRequest:
    def __init__(self):
        self.__linkedAppId = '' # 二级商户应用id
        self.__linkedMerchantId = '' # 二级商户merchantId
        self.__openId = '' # openId
        self.__ruleId = '' # 规则id
        self.__scenceCode = '' # 风险评估场景码
        self.__userId = '' # 支付宝uid

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setLinkedAppId(self, linkedAppId):
        self.__linkedAppId = linkedAppId
        self.__apiParas["linked_app_id"] = linkedAppId

    def getLinkedAppId(self):
        return self.__linkedAppId

    def setLinkedMerchantId(self, linkedMerchantId):
        self.__linkedMerchantId = linkedMerchantId
        self.__apiParas["linked_merchant_id"] = linkedMerchantId

    def getLinkedMerchantId(self):
        return self.__linkedMerchantId

    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

    def setRuleId(self, ruleId):
        self.__ruleId = ruleId
        self.__apiParas["rule_id"] = ruleId

    def getRuleId(self):
        return self.__ruleId

    def setScenceCode(self, scenceCode):
        self.__scenceCode = scenceCode
        self.__apiParas["scence_code"] = scenceCode

    def getScenceCode(self):
        return self.__scenceCode

    def setUserId(self, userId):
        self.__userId = userId
        self.__apiParas["user_id"] = userId

    def getUserId(self):
        return self.__userId

    def getApiMethodName(self):
        return "zhima.merchant.scene.creditpay.bizriskeval.query"

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
