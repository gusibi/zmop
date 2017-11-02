#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.ep.lawsuit.detail.get request
:author: auto create
:date: 2016-05-06 11:44:57
'''


class ZhimaCreditEpLawsuitDetailGetRequest:
    def __init__(self):
        self.__lawsuitId = '' # 涉诉ID
        self.__lawsuitType = '' # 涉诉类型。cpws-裁判文书; zxgg-执行公告; sxgg-失信公告; ktgg-开庭公告; fygg-法院公告; ajlc-案件流程信息; bgt-曝光台。
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddhhmmssSSS，后13位为自增数字。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setLawsuitId(self, lawsuitId):
        self.__lawsuitId = lawsuitId
        self.__apiParas["lawsuit_id"] = lawsuitId

    def getLawsuitId(self):
        return self.__lawsuitId

    def setLawsuitType(self, lawsuitType):
        self.__lawsuitType = lawsuitType
        self.__apiParas["lawsuit_type"] = lawsuitType

    def getLawsuitType(self):
        return self.__lawsuitType

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
        return "zhima.credit.ep.lawsuit.detail.get"

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
