#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.skynetrisk.get request
:author: auto create
:date: 2016-10-13 18:51:23
'''


class ZhimaCreditSkynetriskGetRequest:
    def __init__(self):
        self.__alipayLogonId = '' # 支付宝登陆号
        self.__certNo = '' # 身份证号码
        self.__contractFlag = '' # 合约外标，服务标识。签约过后将会收到含有该服务标识的邮件，或者向协同您签约的芝麻合作人员索取。
        self.__mobile = '' # 手机号码
        self.__name = '' # 姓名
        self.__principalType = '' # 主体类型和对应参数使用身份证信息查询填cert，对应cert_no和name参数必填；使用支付宝登陆账号查询填alipayLogonId，对应alipay_logon_id参数必填；使用支付宝用户ID查询填userId，对应user_id参数必填；使用手机号查询填mobile，对应mobile参数必填
        self.__productCode = '' # 产品码，固定为w1010100000000001000
        self.__transactionId = '' # transaction_id是代表一笔请求的唯一标志，该标识作为对账的关键信息，对于用户使用相同transaction_id的查询，芝麻在一天（86400秒）内返回首次查询数据，超过有效期的查询即为无效并返回异常（错误码xxxx），有效期内的重复查询不重新计费。 transaction_id 推荐生成方式是：30位，（其中17位时间值（精确到毫秒）：yyyyMMddHHmmssSSS）加上（13位自增数字：1234567890123）
        self.__userId = '' # 支付宝账号ID

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAlipayLogonId(self, alipayLogonId):
        self.__alipayLogonId = alipayLogonId
        self.__apiParas["alipay_logon_id"] = alipayLogonId

    def getAlipayLogonId(self):
        return self.__alipayLogonId

    def setCertNo(self, certNo):
        self.__certNo = certNo
        self.__apiParas["cert_no"] = certNo

    def getCertNo(self):
        return self.__certNo

    def setContractFlag(self, contractFlag):
        self.__contractFlag = contractFlag
        self.__apiParas["contract_flag"] = contractFlag

    def getContractFlag(self):
        return self.__contractFlag

    def setMobile(self, mobile):
        self.__mobile = mobile
        self.__apiParas["mobile"] = mobile

    def getMobile(self):
        return self.__mobile

    def setName(self, name):
        self.__name = name
        self.__apiParas["name"] = name

    def getName(self):
        return self.__name

    def setPrincipalType(self, principalType):
        self.__principalType = principalType
        self.__apiParas["principal_type"] = principalType

    def getPrincipalType(self):
        return self.__principalType

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

    def setUserId(self, userId):
        self.__userId = userId
        self.__apiParas["user_id"] = userId

    def getUserId(self):
        return self.__userId

    def getApiMethodName(self):
        return "zhima.credit.skynetrisk.get"

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
