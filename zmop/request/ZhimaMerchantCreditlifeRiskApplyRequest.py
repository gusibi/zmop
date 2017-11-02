#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.creditlife.risk.apply request
:author: auto create
:date: 2017-04-06 09:38:31
'''


class ZhimaMerchantCreditlifeRiskApplyRequest:
    def __init__(self):
        self.__address = '' # 
        self.__certNo = '' # 
        self.__itemId = '' # 
        self.__mobile = '' # 
        self.__name = '' # 
        self.__transactionId = '' # 

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAddress(self, address):
        self.__address = address
        self.__apiParas["address"] = address

    def getAddress(self):
        return self.__address

    def setCertNo(self, certNo):
        self.__certNo = certNo
        self.__apiParas["cert_no"] = certNo

    def getCertNo(self):
        return self.__certNo

    def setItemId(self, itemId):
        self.__itemId = itemId
        self.__apiParas["item_id"] = itemId

    def getItemId(self):
        return self.__itemId

    def setMobile(self, mobile):
        self.__mobile = mobile
        self.__apiParas["mobile"] = mobile

    def getMobile(self):
        return self.__mobile

    def setName(self, name):
        self.__name = name
        self.__apiParas["name"] = name

    def getName(self):
        return self.__name

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def getApiMethodName(self):
        return "zhima.merchant.creditlife.risk.apply"

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
