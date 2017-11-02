#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.open.log.feedback request
:author: auto create
:date: 2017-03-02 15:23:56
'''


class ZhimaOpenLogFeedbackRequest:
    def __init__(self):
        self.__logInfo = '' # 

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setLogInfo(self, logInfo):
        self.__logInfo = logInfo
        self.__apiParas["log_info"] = logInfo

    def getLogInfo(self):
        return self.__logInfo

    def getApiMethodName(self):
        return "zhima.open.log.feedback"

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
