#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.ep.info.get request
:author: auto create
:date: 2016-05-06 11:44:47
'''


class ZhimaCreditEpInfoGetRequest:
    def __init__(self):
        self.__dataType = '' # 查询类型。1-社会信用代码；2-企业名称；3-企业注册号；4-组织机构代码。
        self.__dataValue = '' # 数据类型的对应值。
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddhhmmssSSS，后13位为自增数字。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setDataType(self, dataType):
        self.__dataType = dataType
        self.__apiParas["data_type"] = dataType

    def getDataType(self):
        return self.__dataType

    def setDataValue(self, dataValue):
        self.__dataValue = dataValue
        self.__apiParas["data_value"] = dataValue

    def getDataValue(self):
        return self.__dataValue

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
        return "zhima.credit.ep.info.get"

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
