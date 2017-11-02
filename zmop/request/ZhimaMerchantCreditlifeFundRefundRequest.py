#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.creditlife.fund.refund request
:author: auto create
:date: 2017-08-04 10:26:12
'''


class ZhimaMerchantCreditlifeFundRefundRequest:
    def __init__(self):
        self.__bizProduct = '' # 
        self.__outOrderNo = '' # 商户发起扣款时的订单号
        self.__payAmount = '' # 退款金额
        self.__remark = '' # 交易信息说明(退款原因)

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizProduct(self, bizProduct):
        self.__bizProduct = bizProduct
        self.__apiParas["biz_product"] = bizProduct

    def getBizProduct(self):
        return self.__bizProduct

    def setOutOrderNo(self, outOrderNo):
        self.__outOrderNo = outOrderNo
        self.__apiParas["out_order_no"] = outOrderNo

    def getOutOrderNo(self):
        return self.__outOrderNo

    def setPayAmount(self, payAmount):
        self.__payAmount = payAmount
        self.__apiParas["pay_amount"] = payAmount

    def getPayAmount(self):
        return self.__payAmount

    def setRemark(self, remark):
        self.__remark = remark
        self.__apiParas["remark"] = remark

    def getRemark(self):
        return self.__remark

    def getApiMethodName(self):
        return "zhima.merchant.creditlife.fund.refund"

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
