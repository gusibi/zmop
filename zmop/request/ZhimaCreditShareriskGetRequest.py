#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.sharerisk.get request
:author: auto create
:date: 2016-03-31 14:34:57
'''


class ZhimaCreditShareriskGetRequest:
    def __init__(self):
        self.__bizApplyNo = '' # 业务申请单号
        self.__bizAuthNo = '' # 授权合同编号
        self.__bizScene = '' # 业务场景[01： 申贷审批； 02： 贷后管理]
        self.__certNo = '' # 证件号码
        self.__certType = '' # 证件类型[100：身份证]
        self.__name = '' # 姓名
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddhhmmssSSS，后13位为自增数字。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizApplyNo(self, bizApplyNo):
        self.__bizApplyNo = bizApplyNo
        self.__apiParas["biz_apply_no"] = bizApplyNo

    def getBizApplyNo(self):
        return self.__bizApplyNo

    def setBizAuthNo(self, bizAuthNo):
        self.__bizAuthNo = bizAuthNo
        self.__apiParas["biz_auth_no"] = bizAuthNo

    def getBizAuthNo(self):
        return self.__bizAuthNo

    def setBizScene(self, bizScene):
        self.__bizScene = bizScene
        self.__apiParas["biz_scene"] = bizScene

    def getBizScene(self):
        return self.__bizScene

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
        return "zhima.credit.sharerisk.get"

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
