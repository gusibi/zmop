#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.ep.certification.query request
:author: auto create
:date: 2017-07-27 20:19:37
'''


class ZhimaCustomerEpCertificationQueryRequest:
    def __init__(self):
        self.__bizNo = '' # 一次认证的唯一标识，在商户调用认证初始化接口的时候获取

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizNo(self, bizNo):
        self.__bizNo = bizNo
        self.__apiParas["biz_no"] = bizNo

    def getBizNo(self):
        return self.__bizNo

    def getApiMethodName(self):
        return "zhima.customer.ep.certification.query"

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
