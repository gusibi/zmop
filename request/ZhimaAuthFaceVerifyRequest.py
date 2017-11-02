#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.face.verify request
:author: auto create
:date: 2017-03-29 13:11:30
'''


class ZhimaAuthFaceVerifyRequest:
    def __init__(self):
        self.__bizType = '' # 活体认证类型，目前有认证和授权两种类型；默认为授权类型
        self.__images = '' # 
        self.__token = '' # 标识一次请求流水

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizType(self, bizType):
        self.__bizType = bizType
        self.__apiParas["biz_type"] = bizType

    def getBizType(self):
        return self.__bizType

    def setImages(self, images):
        self.__images = images
        self.__apiParas["images"] = images

    def getImages(self):
        return self.__images

    def setToken(self, token):
        self.__token = token
        self.__apiParas["token"] = token

    def getToken(self):
        return self.__token

    def getApiMethodName(self):
        return "zhima.auth.face.verify"

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
