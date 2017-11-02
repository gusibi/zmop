#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.contract.initialize request
:author: auto create
:date: 2017-09-19 14:41:27
'''


class ZhimaCustomerContractInitializeRequest:
    def __init__(self):
        self.__contractFile = '' # 合约内容，PDF文件流，BASE64编码
        self.__contractName = '' # 合约名称，展示给签约方
        self.__productCode = '' # 芝麻认证产品码,示例值为真实的产品码

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setContractFile(self, contractFile):
        self.__contractFile = contractFile
        self.__apiParas["contract_file"] = contractFile

    def getContractFile(self):
        return self.__contractFile

    def setContractName(self, contractName):
        self.__contractName = contractName
        self.__apiParas["contract_name"] = contractName

    def getContractName(self):
        return self.__contractName

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def getApiMethodName(self):
        return "zhima.customer.contract.initialize"

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
