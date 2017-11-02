#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.creditrecord.summary.query request
:author: auto create
:date: 2017-10-20 14:52:52
'''


class ZhimaCustomerCreditrecordSummaryQueryRequest:
    def __init__(self):
        self.__alipayUserId = '' # 用户支付宝ID
        self.__bizScene = '' # 足迹业务场景

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAlipayUserId(self, alipayUserId):
        self.__alipayUserId = alipayUserId
        self.__apiParas["alipay_user_id"] = alipayUserId

    def getAlipayUserId(self):
        return self.__alipayUserId

    def setBizScene(self, bizScene):
        self.__bizScene = bizScene
        self.__apiParas["biz_scene"] = bizScene

    def getBizScene(self):
        return self.__bizScene

    def getApiMethodName(self):
        return "zhima.customer.creditrecord.summary.query"

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
