#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.collection.support request
:author: auto create
:date: 2016-07-12 11:18:06
'''


class ZhimaCreditCollectionSupportRequest:
    def __init__(self):
        self.__certNo = '' # 证件号码。当前仅支持身份证。请输入身份证号码
        self.__certType = '' # 证件类型。当前只支持身份证：IDENTITY_CARD
        self.__name = '' # 要查询的用户姓名
        self.__numberStatus = '' # 使用过的无效联系号码及状态列表。每一项格式为：${号码}|${状态};${号码}|${状态}。例如：18604020393|A;18604020394|B
        self.__productCode = '' # 云产品id
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddhhmmssSSS，后13位为自增数字。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setCertNo(self, certNo):
        self.__certNo = certNo
        self.__apiParas["cert_no"] = certNo

    def getCertNo(self):
        return self.__certNo

    def setCertType(self, certType):
        self.__certType = certType
        self.__apiParas["cert_type"] = certType

    def getCertType(self):
        return self.__certType

    def setName(self, name):
        self.__name = name
        self.__apiParas["name"] = name

    def getName(self):
        return self.__name

    def setNumberStatus(self, numberStatus):
        self.__numberStatus = numberStatus
        self.__apiParas["number_status"] = numberStatus

    def getNumberStatus(self):
        return self.__numberStatus

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
        return "zhima.credit.collection.support"

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
