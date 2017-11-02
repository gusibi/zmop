#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.ep.cloudatlas.get request
:author: auto create
:date: 2017-06-21 09:19:45
'''


class ZhimaCreditEpCloudatlasGetRequest:
    def __init__(self):
        self.__cloudatlasCode = '' # 请输入调用云图产品申请接口返回的云图编码
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 此transaction_id请传云图查询请求接口的transaction_id

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setCloudatlasCode(self, cloudatlasCode):
        self.__cloudatlasCode = cloudatlasCode
        self.__apiParas["cloudatlas_code"] = cloudatlasCode

    def getCloudatlasCode(self):
        return self.__cloudatlasCode

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
        return "zhima.credit.ep.cloudatlas.get"

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
