#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.face.init request
:author: auto create
:date: 2017-06-23 17:18:57
'''


class ZhimaAuthFaceInitRequest:
    def __init__(self):
        self.__apiKey = '' # 应用的标识
        self.__authMsg = '' # 参数的加密串
        self.__bizType = '' # 用于标识使用人脸业务的类型是授权或者认证，默认为授权类型
        self.__bundleId = '' # 不同商户的bundle_id,用来做缓存
        self.__token = '' # 请求的sessionId

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setApiKey(self, apiKey):
        self.__apiKey = apiKey
        self.__apiParas["api_key"] = apiKey

    def getApiKey(self):
        return self.__apiKey

    def setAuthMsg(self, authMsg):
        self.__authMsg = authMsg
        self.__apiParas["auth_msg"] = authMsg

    def getAuthMsg(self):
        return self.__authMsg

    def setBizType(self, bizType):
        self.__bizType = bizType
        self.__apiParas["biz_type"] = bizType

    def getBizType(self):
        return self.__bizType

    def setBundleId(self, bundleId):
        self.__bundleId = bundleId
        self.__apiParas["bundle_id"] = bundleId

    def getBundleId(self):
        return self.__bundleId

    def setToken(self, token):
        self.__token = token
        self.__apiParas["token"] = token

    def getToken(self):
        return self.__token

    def getApiMethodName(self):
        return "zhima.auth.face.init"

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
