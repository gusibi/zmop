#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.card.limit.get request
:author: auto create
:date: 2016-07-12 10:47:59
'''


class ZhimaCreditCardLimitGetRequest:
    def __init__(self):
        self.__instId = '' # 机构ID
        self.__openId = '' # 芝麻开放平台OPENID
        self.__orderId = '' # 订单号
        self.__productCode = '' # 云产品id
        self.__transactionId = '' # test
        self.__userId = '' # 支付宝用户ID

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setInstId(self, instId):
        self.__instId = instId
        self.__apiParas["inst_id"] = instId

    def getInstId(self):
        return self.__instId

    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

    def setOrderId(self, orderId):
        self.__orderId = orderId
        self.__apiParas["order_id"] = orderId

    def getOrderId(self):
        return self.__orderId

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

    def setUserId(self, userId):
        self.__userId = userId
        self.__apiParas["user_id"] = userId

    def getUserId(self):
        return self.__userId

    def getApiMethodName(self):
        return "zhima.credit.card.limit.get"

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
