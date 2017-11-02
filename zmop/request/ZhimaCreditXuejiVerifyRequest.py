#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.xueji.verify request
:author: auto create
:date: 2016-08-06 15:11:11
'''


class ZhimaCreditXuejiVerifyRequest:
    def __init__(self):
        self.__collegeName = '' # 院校名称
        self.__educationCategory = '' # 输入为数字：1：表示普通全日制；2：表示硕士或者博士研究生；5：表示成人教育；6：表示高等教育自学考试；7：表示网络教育；8：表示开放教育；9：表示不详
        self.__educationDegree = '' # 学历层次：博士、硕士、本科、专科、成人。
        self.__enrollmentYear = '' # 入学年份，格式为四位数的年份，如2013
        self.__graduateYear = '' # 毕业年份，格式为四位数的年份，如2018
        self.__openId = '' # 芝麻会员在商户端的身份标识
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddHHmmssSSS，后13位为自增数字。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
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

    def setEnrollmentYear(self, enrollmentYear):
        self.__enrollmentYear = enrollmentYear
        self.__apiParas["enrollment_year"] = enrollmentYear

    def getEnrollmentYear(self):
        return self.__enrollmentYear

    def setGraduateYear(self, graduateYear):
        self.__graduateYear = graduateYear
        self.__apiParas["graduate_year"] = graduateYear

    def getGraduateYear(self):
        return self.__graduateYear

    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

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
        return "zhima.credit.xueji.verify"

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
