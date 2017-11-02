#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.engine.protocol request
:author: auto create
:date: 2017-07-26 21:18:54
'''


class ZhimaAuthEngineProtocolRequest:
    def __init__(self):
        self.__bizParams = '' # 业务扩展入参
        self.__identityParam = '' # 授权的身份标识参数
        self.__identityType = '' # 用户的身份标识类型\n3：身份证+姓名+手机号进行支付宝识别，核身，授权\n4：身份证+姓名+手机号（可选）进行公安网的核身，授权

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizParams(self, bizParams):
        self.__bizParams = bizParams
        self.__apiParas["biz_params"] = bizParams

    def getBizParams(self):
        return self.__bizParams

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
        return "zhima.auth.engine.protocol"

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
