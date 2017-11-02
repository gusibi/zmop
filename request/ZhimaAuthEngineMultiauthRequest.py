#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.engine.multiauth request
:author: auto create
:date: 2017-07-26 21:17:44
'''


class ZhimaAuthEngineMultiauthRequest:
    def __init__(self):
        self.__authAppId = '' # 外部商户应用id
        self.__authMerchantId = '' # 外部商户id
        self.__userId = '' # 支付宝用户id

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAuthAppId(self, authAppId):
        self.__authAppId = authAppId
        self.__apiParas["auth_app_id"] = authAppId

    def getAuthAppId(self):
        return self.__authAppId

    def setAuthMerchantId(self, authMerchantId):
        self.__authMerchantId = authMerchantId
        self.__apiParas["auth_merchant_id"] = authMerchantId

    def getAuthMerchantId(self):
        return self.__authMerchantId

    def setUserId(self, userId):
        self.__userId = userId
        self.__apiParas["user_id"] = userId

    def getUserId(self):
        return self.__userId

    def getApiMethodName(self):
        return "zhima.auth.engine.multiauth"

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
