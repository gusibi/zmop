#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.data.upload.initialize request
:author: auto create
:date: 2017-04-28 14:30:00
'''


class ZhimaMerchantDataUploadInitializeRequest:
    def __init__(self):
        self.__sceneCode = '' # 

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setSceneCode(self, sceneCode):
        self.__sceneCode = sceneCode
        self.__apiParas["scene_code"] = sceneCode

    def getSceneCode(self):
        return self.__sceneCode

    def getApiMethodName(self):
        return "zhima.merchant.data.upload.initialize"

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
