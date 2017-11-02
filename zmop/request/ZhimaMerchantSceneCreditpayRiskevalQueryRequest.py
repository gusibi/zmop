#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.scene.creditpay.riskeval.query request
:author: auto create
:date: 2017-06-19 11:21:17
'''


class ZhimaMerchantSceneCreditpayRiskevalQueryRequest:
    def __init__(self):
        self.__needAuth = '' # 是否需要授权
        self.__userId = '' # 支付宝userid

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setNeedAuth(self, needAuth):
        self.__needAuth = needAuth
        self.__apiParas["need_auth"] = needAuth

    def getNeedAuth(self):
        return self.__needAuth

    def setUserId(self, userId):
        self.__userId = userId
        self.__apiParas["user_id"] = userId

    def getUserId(self):
        return self.__userId

    def getApiMethodName(self):
        return "zhima.merchant.scene.creditpay.riskeval.query"

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
