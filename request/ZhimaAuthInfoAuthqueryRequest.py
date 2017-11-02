#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.info.authquery request
:author: auto create
:date: 2017-04-07 10:48:13
'''


class ZhimaAuthInfoAuthqueryRequest:
    def __init__(self):
        self.__authCategory = '' # 授权类型，用于识别当前查询是否授权的分流；可传参数“B2B”或“C2B”，自助商户请填写“C2B”。
        self.__identityParam = '' # 不同身份类型传入的参数列表,json字符串的key-value格式身份类型identityType=0:{"openId":"268801234567890123456"}身份类型identityType=2:{"certNo":"330100xxxxxxxxxxxx","name":"张三","certType":"IDENTITY_CARD"}
        self.__identityType = '' # 身份标识类型0:按照openId查询2:按照身份证+姓名查询

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAuthCategory(self, authCategory):
        self.__authCategory = authCategory
        self.__apiParas["auth_category"] = authCategory

    def getAuthCategory(self):
        return self.__authCategory

    def setIdentityParam(self, identityParam):
        self.__identityParam = identityParam
        self.__apiParas["identity_param"] = identityParam

    def getIdentityParam(self):
        return self.__identityParam

    def setIdentityType(self, identityType):
        self.__identityType = identityType
        self.__apiParas["identity_type"] = identityType

    def getIdentityType(self):
        return self.__identityType

    def getApiMethodName(self):
        return "zhima.auth.info.authquery"

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
