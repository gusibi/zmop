#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.kkcredit.abcscore.query request
:author: auto create
:date: 2017-08-22 15:59:07
'''


class ZhimaCreditKkcreditAbcscoreQueryRequest:
    def __init__(self):
        self.__age = '' # 年龄
        self.__crdAgeUnclsAvg = '' # 未销信用卡开户距今月数的平均数
        self.__gender = '' # 性别，男=1，女=0
        self.__lnizedLnitCttPpl = '' # 近90天深夜联系人
        self.__normCdtBalUsedPctAvg = '' # 当前正常的信用卡账户已用额度与可用额度之比的均值
        self.__openId = '' # 芝麻会员在商户端的身份标识。
        self.__phoneUseMth = '' # 手机注册时长
        self.__productCode = '' # 产品码
        self.__smsLonfizedSendPpl = '' # 近150天短信发送联系人
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddhhmmssSSS，后13位为自增数字。
        self.__trcLsmfiAvgPlanTotalPct = '' # 近5月套餐金额占比

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAge(self, age):
        self.__age = age
        self.__apiParas["age"] = age

    def getAge(self):
        return self.__age

    def setCrdAgeUnclsAvg(self, crdAgeUnclsAvg):
        self.__crdAgeUnclsAvg = crdAgeUnclsAvg
        self.__apiParas["crd_age_uncls_avg"] = crdAgeUnclsAvg

    def getCrdAgeUnclsAvg(self):
        return self.__crdAgeUnclsAvg

    def setGender(self, gender):
        self.__gender = gender
        self.__apiParas["gender"] = gender

    def getGender(self):
        return self.__gender

    def setLnizedLnitCttPpl(self, lnizedLnitCttPpl):
        self.__lnizedLnitCttPpl = lnizedLnitCttPpl
        self.__apiParas["lnized_lnit_ctt_ppl"] = lnizedLnitCttPpl

    def getLnizedLnitCttPpl(self):
        return self.__lnizedLnitCttPpl

    def setNormCdtBalUsedPctAvg(self, normCdtBalUsedPctAvg):
        self.__normCdtBalUsedPctAvg = normCdtBalUsedPctAvg
        self.__apiParas["norm_cdt_bal_used_pct_avg"] = normCdtBalUsedPctAvg

    def getNormCdtBalUsedPctAvg(self):
        return self.__normCdtBalUsedPctAvg

    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

    def setPhoneUseMth(self, phoneUseMth):
        self.__phoneUseMth = phoneUseMth
        self.__apiParas["phone_use_mth"] = phoneUseMth

    def getPhoneUseMth(self):
        return self.__phoneUseMth

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setSmsLonfizedSendPpl(self, smsLonfizedSendPpl):
        self.__smsLonfizedSendPpl = smsLonfizedSendPpl
        self.__apiParas["sms_lonfized_send_ppl"] = smsLonfizedSendPpl

    def getSmsLonfizedSendPpl(self):
        return self.__smsLonfizedSendPpl

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def setTrcLsmfiAvgPlanTotalPct(self, trcLsmfiAvgPlanTotalPct):
        self.__trcLsmfiAvgPlanTotalPct = trcLsmfiAvgPlanTotalPct
        self.__apiParas["trc_lsmfi_avg_plan_total_pct"] = trcLsmfiAvgPlanTotalPct

    def getTrcLsmfiAvgPlanTotalPct(self):
        return self.__trcLsmfiAvgPlanTotalPct

    def getApiMethodName(self):
        return "zhima.credit.kkcredit.abcscore.query"

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
