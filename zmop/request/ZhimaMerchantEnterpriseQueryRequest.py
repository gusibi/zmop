#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.enterprise.query request
:author: auto create
:date: 2017-03-02 14:54:06
'''


class ZhimaMerchantEnterpriseQueryRequest:
    def __init__(self):
        self.__bizExtParams = '' # 业务扩展参数，当前无需设置该参数

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizExtParams(self, bizExtParams):
        self.__bizExtParams = bizExtParams
        self.__apiParas["biz_ext_params"] = bizExtParams

    def getBizExtParams(self):
        return self.__bizExtParams

    def getApiMethodName(self):
        return "zhima.merchant.enterprise.query"

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
