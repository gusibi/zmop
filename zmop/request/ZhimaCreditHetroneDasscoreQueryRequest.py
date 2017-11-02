#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.hetrone.dasscore.query request
:author: auto create
:date: 2017-09-07 14:52:06
'''


class ZhimaCreditHetroneDasscoreQueryRequest:
    def __init__(self):
        self.__amtBankcardTransacThreeMonths = '' # 近3月交易总金额
        self.__cntBankcardTransacTwelveMonths = '' # 近十二个月有交易的月数
        self.__cntMobileOnline = '' # 手机在网时长
        self.__contactScore = '' # 通讯录分数
        self.__existsBankcardTransacOversea = '' # 最近有无境外消费
        self.__gender = '' # 性别
        self.__openId = '' # 用户在商端的身份标识
        self.__productCode = '' # 信用产品码，对应云产品的标识
        self.__transactionId = '' # 代表一笔请求的唯一标志，该标识作为对账的关键信息，对于用户使用相同transaction_id的查询，芝麻在一天（86400秒）内返回首次查询数据，超过有效期的查询即为无效并返回异常，有效期内的反复查询不重新计费。transaction_id 推荐生成方式是：30位，（其中17位时间值（精确到毫秒）：yyyyMMddHHmmssSSS）加上（13位自增数字：1234567890123）

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAmtBankcardTransacThreeMonths(self, amtBankcardTransacThreeMonths):
        self.__amtBankcardTransacThreeMonths = amtBankcardTransacThreeMonths
        self.__apiParas["amt_bankcard_transac_three_months"] = amtBankcardTransacThreeMonths

    def getAmtBankcardTransacThreeMonths(self):
        return self.__amtBankcardTransacThreeMonths

    def setCntBankcardTransacTwelveMonths(self, cntBankcardTransacTwelveMonths):
        self.__cntBankcardTransacTwelveMonths = cntBankcardTransacTwelveMonths
        self.__apiParas["cnt_bankcard_transac_twelve_months"] = cntBankcardTransacTwelveMonths

    def getCntBankcardTransacTwelveMonths(self):
        return self.__cntBankcardTransacTwelveMonths

    def setCntMobileOnline(self, cntMobileOnline):
        self.__cntMobileOnline = cntMobileOnline
        self.__apiParas["cnt_mobile_online"] = cntMobileOnline

    def getCntMobileOnline(self):
        return self.__cntMobileOnline

    def setContactScore(self, contactScore):
        self.__contactScore = contactScore
        self.__apiParas["contact_score"] = contactScore

    def getContactScore(self):
        return self.__contactScore

    def setExistsBankcardTransacOversea(self, existsBankcardTransacOversea):
        self.__existsBankcardTransacOversea = existsBankcardTransacOversea
        self.__apiParas["exists_bankcard_transac_oversea"] = existsBankcardTransacOversea

    def getExistsBankcardTransacOversea(self):
        return self.__existsBankcardTransacOversea

    def setGender(self, gender):
        self.__gender = gender
        self.__apiParas["gender"] = gender

    def getGender(self):
        return self.__gender

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
        return "zhima.credit.hetrone.dasscore.query"

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
