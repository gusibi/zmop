#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.data.feedbackurl.query request
:author: auto create
:date: 2016-09-08 08:34:08
'''


class ZhimaDataFeedbackurlQueryRequest:
    def __init__(self):
        self.__merchantId = '' # 

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setMerchantId(self, merchantId):
        self.__merchantId = merchantId
        self.__apiParas["merchant_id"] = merchantId

    def getMerchantId(self):
        return self.__merchantId

    def getApiMethodName(self):
        return "zhima.data.feedbackurl.query"

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
