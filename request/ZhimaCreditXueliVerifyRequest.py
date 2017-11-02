#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.xueli.verify request
:author: auto create
:date: 2016-07-08 10:08:01
'''


class ZhimaCreditXueliVerifyRequest:
    def __init__(self):
        self.__certNo = '' # 证件号码，暂时只支持身份证号
        self.__certType = '' # 证件类型，暂时支持身份证
        self.__collegeName = '' # 院校名称
        self.__educationCategory = '' # 学历类别：普通，研究生，成人，高等教育自学考试，网络教育，开放教育，不详
        self.__educationDegree = '' # 学历层次：博士研究生，硕士研究生，研究生班，第二学士学位，本科，高升本，专升本，第二本科专科，专科(高职)，第二专科，夜大电大函大普通班，大学
        self.__graduateYear = '' # 毕业年份，格式为四位数的年份，如2018
        self.__name = '' # 姓名
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddHHmmssSSS，后13位为自增数字。

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

    def setCollegeName(self, collegeName):
        self.__collegeName = collegeName
        self.__apiParas["college_name"] = collegeName

    def getCollegeName(self):
        return self.__collegeName

    def setEducationCategory(self, educationCategory):
        self.__educationCategory = educationCategory
        self.__apiParas["education_category"] = educationCategory

    def getEducationCategory(self):
        return self.__educationCategory

    def setEducationDegree(self, educationDegree):
        self.__educationDegree = educationDegree
        self.__apiParas["education_degree"] = educationDegree

    def getEducationDegree(self):
        return self.__educationDegree

    def setGraduateYear(self, graduateYear):
        self.__graduateYear = graduateYear
        self.__apiParas["graduate_year"] = graduateYear

    def getGraduateYear(self):
        return self.__graduateYear

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
        return "zhima.credit.xueli.verify"

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
