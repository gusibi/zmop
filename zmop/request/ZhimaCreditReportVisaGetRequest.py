#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.report.visa.get request
:author: auto create
:date: 2017-07-13 18:39:47
'''


class ZhimaCreditReportVisaGetRequest:
    def __init__(self):
        self.__openId = '' # 芝麻会员在商户端的身份标识
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 商户传入的业务流水号

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def getApiMethodName(self):
        return "zhima.credit.report.visa.get"

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
