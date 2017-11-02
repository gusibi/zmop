#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.engine.organizationauth request
:author: auto create
:date: 2017-07-05 10:31:00
'''


class ZhimaAuthEngineOrganizationauthRequest:
    def __init__(self):
        self.__bizParams = '' # 授权码入参，1). 若identity_Type=2时，{"auth_code":"M_P_COMPANY_CERT"} 2). 若identity_Type=5时，{"auth_code":"M_P_COMPANY_UID"}
        self.__identityParam = '' # 证件号目前支持2种：a. 工商注册号：NATIONAL_LEGAL  b. 社会统一信用代码 : NATIONAL_LEGAL_MERGE1). 若identity_type=2时：identity_param={\"certNo\":\"440000400004160\",\"certType\":\"NATIONAL_LEGAL\",\"name\":\"中国移动通信集团广东有限公司\"}"2). 若identity_type=5时：identity_param={\"userId\":\"2088xxxxxx\"}"
        self.__identityType = '' # 用户身份标识类型：5： userId入参的类型标识；2： 证件号和姓名的入参的类型标识

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizParams(self, bizParams):
        self.__bizParams = bizParams
        self.__apiParas["biz_params"] = bizParams

    def getBizParams(self):
        return self.__bizParams

    def setIdentityParam(self, identityParam):
        self.__identityParam = identityParam
        self.__apiParas["identity_param"] = identityParam

    def getIdentityParam(self):
        return self.__identityParam

    def setIdentityType(self, identityType):
        self.__identityType = identityType
        self.__apiParas["identity_type"] = identityType

    def getIdentityType(self):
        return self.__identityType

    def getApiMethodName(self):
        return "zhima.auth.engine.organizationauth"

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
