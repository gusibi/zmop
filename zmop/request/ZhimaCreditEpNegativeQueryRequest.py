#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.ep.negative.query request
:author: auto create
:date: 2017-05-16 15:50:38
'''


class ZhimaCreditEpNegativeQueryRequest:
    def __init__(self):
        self.__category = '' # 枚举值 1:个人 2:企业
        self.__certName = '' # 查询个人，必须填入证件号。查询企业，不需要填写证件号
        self.__certType = '' # 个人的时候必填，填入IDENTITY_CARD。目前只支持内地身份证。
        self.__dataType = '' # 枚举值 :资产冻结:zcdj资产查封:zccf欠税信息：satparty案件串联：anjianparty工商行政处罚：aicparty质检处罚：qtsparty环保处罚：epbparty
        self.__name = '' # 企业名称或个人姓名
        self.__pageNum = '' # 翻页页码
        self.__productCode = '' # 产品码
        self.__transactionId = '' # transaction_id是代表一笔请求的唯一标志，该标识作为对账的关键信息，对于用户使用相同transaction_id的查询，芝麻在一天（86400秒）内返回首次查询数据，超过有效期的查询即为无效并返回异常（错误码xxxx），有效期内的重复查询不重新计费。 transaction_id 推荐生成方式是：30位，（其中17位时间值（精确到毫秒）：yyyyMMddHHmmssSSS）加上（13位自增数字：1234567890123）

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setCategory(self, category):
        self.__category = category
        self.__apiParas["category"] = category

    def getCategory(self):
        return self.__category

    def setCertName(self, certName):
        self.__certName = certName
        self.__apiParas["cert_name"] = certName

    def getCertName(self):
        return self.__certName

    def setCertType(self, certType):
        self.__certType = certType
        self.__apiParas["cert_type"] = certType

    def getCertType(self):
        return self.__certType

    def setDataType(self, dataType):
        self.__dataType = dataType
        self.__apiParas["data_type"] = dataType

    def getDataType(self):
        return self.__dataType

    def setName(self, name):
        self.__name = name
        self.__apiParas["name"] = name

    def getName(self):
        return self.__name

    def setPageNum(self, pageNum):
        self.__pageNum = pageNum
        self.__apiParas["page_num"] = pageNum

    def getPageNum(self):
        return self.__pageNum

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
        return "zhima.credit.ep.negative.query"

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
