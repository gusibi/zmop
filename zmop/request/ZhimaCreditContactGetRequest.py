#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.contact.get request
:author: auto create
:date: 2017-01-18 21:30:13
'''


class ZhimaCreditContactGetRequest:
    def __init__(self):
        self.__address = '' # 用户的地址：最多传入三组，用|分隔。地址中不能有如下特殊字符&,^,\
        self.__isOverdue = '' # 是否逾期。T表示逾期，F表示非逾期
        self.__mobile = '' # 用户手机号，最多传入三个，每个手机号之间以“|"分隔。
        self.__openId = '' # 芝麻会员在商户端的身份标识。
        self.__overdueDays = '' # 逾期天数。请输入数字。
        self.__productCode = '' # 产品码
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddhhmmssSSS，后13位为自增数字。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAddress(self, address):
        self.__address = address
        self.__apiParas["address"] = address

    def getAddress(self):
        return self.__address

    def setIsOverdue(self, isOverdue):
        self.__isOverdue = isOverdue
        self.__apiParas["is_overdue"] = isOverdue

    def getIsOverdue(self):
        return self.__isOverdue

    def setMobile(self, mobile):
        self.__mobile = mobile
        self.__apiParas["mobile"] = mobile

    def getMobile(self):
        return self.__mobile

    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

    def setOverdueDays(self, overdueDays):
        self.__overdueDays = overdueDays
        self.__apiParas["overdue_days"] = overdueDays

    def getOverdueDays(self):
        return self.__overdueDays

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
        return "zhima.credit.contact.get"

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
