#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.borrow.scan request
:author: auto create
:date: 2016-07-18 16:38:23
'''


class ZhimaCustomerBorrowScanRequest:
    def __init__(self):
        self.__goodsId = '' # 
        self.__productCode = '' # 
        self.__scenceCode = '' # 
        self.__shopCode = '' # 

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setGoodsId(self, goodsId):
        self.__goodsId = goodsId
        self.__apiParas["goods_id"] = goodsId

    def getGoodsId(self):
        return self.__goodsId

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setScenceCode(self, scenceCode):
        self.__scenceCode = scenceCode
        self.__apiParas["scence_code"] = scenceCode

    def getScenceCode(self):
        return self.__scenceCode

    def setShopCode(self, shopCode):
        self.__shopCode = shopCode
        self.__apiParas["shop_code"] = shopCode

    def getShopCode(self):
        return self.__shopCode

    def getApiMethodName(self):
        return "zhima.customer.borrow.scan"

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
