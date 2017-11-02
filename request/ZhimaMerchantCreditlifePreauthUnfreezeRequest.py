#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.creditlife.preauth.unfreeze request
:author: auto create
:date: 2017-08-04 10:25:40
'''


class ZhimaMerchantCreditlifePreauthUnfreezeRequest:
    def __init__(self):
        self.__payAmount = '' # 待解冻资金(元)
        self.__preAuthNo = '' # 预授权后产生的预授权号
        self.__remark = '' # 发起资金解冻原因
        self.__transactionId = '' # 交易流水号

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setPayAmount(self, payAmount):
        self.__payAmount = payAmount
        self.__apiParas["pay_amount"] = payAmount

    def getPayAmount(self):
        return self.__payAmount

    def setPreAuthNo(self, preAuthNo):
        self.__preAuthNo = preAuthNo
        self.__apiParas["pre_auth_no"] = preAuthNo

    def getPreAuthNo(self):
        return self.__preAuthNo

    def setRemark(self, remark):
        self.__remark = remark
        self.__apiParas["remark"] = remark

    def getRemark(self):
        return self.__remark

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def getApiMethodName(self):
        return "zhima.merchant.creditlife.preauth.unfreeze"

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
