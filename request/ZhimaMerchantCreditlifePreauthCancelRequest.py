#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.creditlife.preauth.cancel request
:author: auto create
:date: 2017-08-04 10:25:57
'''


class ZhimaMerchantCreditlifePreauthCancelRequest:
    def __init__(self):
        self.__outOrderNo = '' # 待解冻预授权冻结资金订单号，或解冻请求流水号
        self.__preAuthNo = '' # 预授权号
        self.__remark = '' # 取消预授权冻结资金原因

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setOutOrderNo(self, outOrderNo):
        self.__outOrderNo = outOrderNo
        self.__apiParas["out_order_no"] = outOrderNo

    def getOutOrderNo(self):
        return self.__outOrderNo

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

    def getApiMethodName(self):
        return "zhima.merchant.creditlife.preauth.cancel"

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
