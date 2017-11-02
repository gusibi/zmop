#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.certify.check request
:author: auto create
:date: 2017-04-26 11:35:45
'''


class ZhimaCustomerCertifyCheckRequest:
    def __init__(self):
        self.__token = '' # 芝麻认证每一次请求返回的令牌，发起页面认证请求和认证请求结果查询接口都需要使用到该返回值作为入参

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setToken(self, token):
        self.__token = token
        self.__apiParas["token"] = token

    def getToken(self):
        return self.__token

    def getApiMethodName(self):
        return "zhima.customer.certify.check"

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
