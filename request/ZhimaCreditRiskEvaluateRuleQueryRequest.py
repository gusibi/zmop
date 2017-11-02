#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.risk.evaluate.rule.query request
:author: auto create
:date: 2017-06-29 14:03:10
'''


class ZhimaCreditRiskEvaluateRuleQueryRequest:
    def __init__(self):
        self.__productCode = '' # 签约产品标示，唯一对应一个产品
        self.__ruleCode = '' # 可选参数，传值则标示只查询对应规则配置值，不传则输出所有规则配置值
        self.__ruleId = '' # 1000806 【规则标识，使用APPID】如果是ISV商户： 传入二级商户APPID如果是普通商户：传入自己调用APPID
        self.__sceneCode = '' # 标识对接业务场景，业务场景下商户可做自定义策略配置
        self.__transactionId = '' # 唯一标示商户每一笔请求

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setRuleCode(self, ruleCode):
        self.__ruleCode = ruleCode
        self.__apiParas["rule_code"] = ruleCode

    def getRuleCode(self):
        return self.__ruleCode

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
        return "zhima.credit.risk.evaluate.rule.query"

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
