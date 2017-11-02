#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.contact.analyze.query request
:author: auto create
:date: 2017-04-25 15:59:23
'''


class ZhimaCreditContactAnalyzeQueryRequest:
    def __init__(self):
        self.__productCode = '' # 芝麻开放平台信用产品码， 唯一标示云产品
        self.__transactionId = '' # 商户请求的唯一标志，长度64位以内字符串，仅限字母数字下划线组合。 该标识作为业务调用的唯一标识，商户要保证其业务唯一性，使用相同transaction_id的查询， 芝麻在一段时间内（一般为1天）返回首次查询结果， 超过有效期的查询即为无效并返回异常，有效期内的重复查询不重新计费。
        self.__userIds = '' # 支付宝用户id的列表，String类型，多个uid之间用逗号【,】分隔

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
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

    def setUserIds(self, userIds):
        self.__userIds = userIds
        self.__apiParas["user_ids"] = userIds

    def getUserIds(self):
        return self.__userIds

    def getApiMethodName(self):
        return "zhima.credit.contact.analyze.query"

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
