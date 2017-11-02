#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.ep.watchlist.get request
:author: auto create
:date: 2017-03-30 13:57:54
'''


class ZhimaCreditEpWatchlistGetRequest:
    def __init__(self):
        self.__dataType = '' # 企业关注名单的输入类型：工商注册号（REG_NO）、组织机构代码（ORG_NO）、社会统一代码(SOCIETY_NO)、税务登记号(TAX_NO)、企业名称（COMPANY_NAME）
        self.__dataValue = '' # 企业关注名单，对应类型的数据值
        self.__productCode = '' # 产品码
        self.__transactionId = '' # transaction_id是代表一笔请求的唯一标志，该标识作为对账的关键信息，对于用户使用相同transaction_id的查询，芝麻在一天（86400秒）内返回首次查询数据，超过有效期的查询即为无效并返回异常（错误码xxxx），有效期内的重复查询不重新计费。 transaction_id 推荐生成方式是：30位，（其中17位时间值（精确到毫秒）：yyyyMMddHHmmssSSS）加上（13位自增数字：1234567890123）

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
        return "zhima.credit.ep.watchlist.get"

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
