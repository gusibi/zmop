#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.driver.verify request
:author: auto create
:date: 2016-08-06 15:11:41
'''


class ZhimaCreditDriverVerifyRequest:
    def __init__(self):
        self.__archiveNo = '' # 驾驶证档案编号
        self.__issueDate = '' # 初次领证日期，格式为yyyyMMdd
        self.__licenseNo = '' # 驾驶证号码
        self.__name = '' # 驾驶证上的姓名
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 芝麻业务凭证，详见https://b.zmxy.com.cn/technology/openDoc.htm?id=334
        self.__vehicleClass = '' # 准驾车型，多个车型之间以 || 隔开，如C1 || C2 || B2

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setArchiveNo(self, archiveNo):
        self.__archiveNo = archiveNo
        self.__apiParas["archive_no"] = archiveNo

    def getArchiveNo(self):
        return self.__archiveNo

    def setIssueDate(self, issueDate):
        self.__issueDate = issueDate
        self.__apiParas["issue_date"] = issueDate

    def getIssueDate(self):
        return self.__issueDate

    def setLicenseNo(self, licenseNo):
        self.__licenseNo = licenseNo
        self.__apiParas["license_no"] = licenseNo

    def getLicenseNo(self):
        return self.__licenseNo

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

    def setVehicleClass(self, vehicleClass):
        self.__vehicleClass = vehicleClass
        self.__apiParas["vehicle_class"] = vehicleClass

    def getVehicleClass(self):
        return self.__vehicleClass

    def getApiMethodName(self):
        return "zhima.credit.driver.verify"

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
