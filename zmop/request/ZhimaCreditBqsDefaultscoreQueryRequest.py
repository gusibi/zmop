#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.bqs.defaultscore.query request
:author: auto create
:date: 2017-09-07 14:55:48
'''


class ZhimaCreditBqsDefaultscoreQueryRequest:
    def __init__(self):
        self.__acceptPercentApply = '' # 申请事件通过比率
        self.__age = '' # 年龄
        self.__applyHour = '' # 申请时间（小时，0-23）
        self.__applyPartnerTypeCount = '' # 多头申请商户类型数量
        self.__blackCount = '' # 黑名单命中个数
        self.__callActiveArea = '' # 本人主要通话活动区域在几线城市
        self.__contactExcludedCount = '' # 排除被叫电话很短的联系人个数
        self.__contactsActiveArea = '' # 朋友圈活动区域在几线城市
        self.__deviceCount = '' # 关联设备数量
        self.__gender = '' # 性别
        self.__gpsCityCount = '' # GPS城市数量
        self.__inactiveDays = '' # 全天未使用通话和短信功能天数
        self.__ipCityCount = '' # IP城市数量
        self.__loanAppCount = '' # 设备中借贷app数量
        self.__mobile = '' # 手机号
        self.__multiapplyCount = '' # 多头申请商户数量
        self.__nightCalls = '' # 夜间通话次数
        self.__noneMobileCount = '' # 联系人中非手机个数
        self.__onlyTerminCount = '' # 仅有被叫联系人个数
        self.__openDays = '' # 入网时长
        self.__openId = '' # 用户在商端的身份标识
        self.__phoneDays = '' # 该用户第一次事件距今时间
        self.__productCode = '' # 信用产品码，对应云产品的标识
        self.__provinceId = '' # 省份代码
        self.__rejectPercentApply = '' # 申请事件拒绝比率
        self.__sumInfoCostMoney = '' # 话费消费总金额
        self.__topContact = '' # 最常用联系人，多个用逗号分隔
        self.__transactionId = '' # 代表一笔请求的唯一标志，该标识作为对账的关键信息，对于用户使用相同transaction_id的查询，芝麻在一天（86400秒）内返回首次查询数据，超过有效期的查询即为无效并返回异常，有效期内的反复查询不重新计费。transaction_id 推荐生成方式是：30位，（其中17位时间值（精确到毫秒）：yyyyMMddHHmmssSSS）加上（13位自增数字：1234567890123）
        self.__whiteGrade = '' # 白名单等级
        self.__workCityCount = '' # 上班时间手机号关联城市数量

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAcceptPercentApply(self, acceptPercentApply):
        self.__acceptPercentApply = acceptPercentApply
        self.__apiParas["accept_percent_apply"] = acceptPercentApply

    def getAcceptPercentApply(self):
        return self.__acceptPercentApply

    def setAge(self, age):
        self.__age = age
        self.__apiParas["age"] = age

    def getAge(self):
        return self.__age

    def setApplyHour(self, applyHour):
        self.__applyHour = applyHour
        self.__apiParas["apply_hour"] = applyHour

    def getApplyHour(self):
        return self.__applyHour

    def setApplyPartnerTypeCount(self, applyPartnerTypeCount):
        self.__applyPartnerTypeCount = applyPartnerTypeCount
        self.__apiParas["apply_partner_type_count"] = applyPartnerTypeCount

    def getApplyPartnerTypeCount(self):
        return self.__applyPartnerTypeCount

    def setBlackCount(self, blackCount):
        self.__blackCount = blackCount
        self.__apiParas["black_count"] = blackCount

    def getBlackCount(self):
        return self.__blackCount

    def setCallActiveArea(self, callActiveArea):
        self.__callActiveArea = callActiveArea
        self.__apiParas["call_active_area"] = callActiveArea

    def getCallActiveArea(self):
        return self.__callActiveArea

    def setContactExcludedCount(self, contactExcludedCount):
        self.__contactExcludedCount = contactExcludedCount
        self.__apiParas["contact_excluded_count"] = contactExcludedCount

    def getContactExcludedCount(self):
        return self.__contactExcludedCount

    def setContactsActiveArea(self, contactsActiveArea):
        self.__contactsActiveArea = contactsActiveArea
        self.__apiParas["contacts_active_area"] = contactsActiveArea

    def getContactsActiveArea(self):
        return self.__contactsActiveArea

    def setDeviceCount(self, deviceCount):
        self.__deviceCount = deviceCount
        self.__apiParas["device_count"] = deviceCount

    def getDeviceCount(self):
        return self.__deviceCount

    def setGender(self, gender):
        self.__gender = gender
        self.__apiParas["gender"] = gender

    def getGender(self):
        return self.__gender

    def setGpsCityCount(self, gpsCityCount):
        self.__gpsCityCount = gpsCityCount
        self.__apiParas["gps_city_count"] = gpsCityCount

    def getGpsCityCount(self):
        return self.__gpsCityCount

    def setInactiveDays(self, inactiveDays):
        self.__inactiveDays = inactiveDays
        self.__apiParas["inactive_days"] = inactiveDays

    def getInactiveDays(self):
        return self.__inactiveDays

    def setIpCityCount(self, ipCityCount):
        self.__ipCityCount = ipCityCount
        self.__apiParas["ip_city_count"] = ipCityCount

    def getIpCityCount(self):
        return self.__ipCityCount

    def setLoanAppCount(self, loanAppCount):
        self.__loanAppCount = loanAppCount
        self.__apiParas["loan_app_count"] = loanAppCount

    def getLoanAppCount(self):
        return self.__loanAppCount

    def setMobile(self, mobile):
        self.__mobile = mobile
        self.__apiParas["mobile"] = mobile

    def getMobile(self):
        return self.__mobile

    def setMultiapplyCount(self, multiapplyCount):
        self.__multiapplyCount = multiapplyCount
        self.__apiParas["multiapply_count"] = multiapplyCount

    def getMultiapplyCount(self):
        return self.__multiapplyCount

    def setNightCalls(self, nightCalls):
        self.__nightCalls = nightCalls
        self.__apiParas["night_calls"] = nightCalls

    def getNightCalls(self):
        return self.__nightCalls

    def setNoneMobileCount(self, noneMobileCount):
        self.__noneMobileCount = noneMobileCount
        self.__apiParas["none_mobile_count"] = noneMobileCount

    def getNoneMobileCount(self):
        return self.__noneMobileCount

    def setOnlyTerminCount(self, onlyTerminCount):
        self.__onlyTerminCount = onlyTerminCount
        self.__apiParas["only_termin_count"] = onlyTerminCount

    def getOnlyTerminCount(self):
        return self.__onlyTerminCount

    def setOpenDays(self, openDays):
        self.__openDays = openDays
        self.__apiParas["open_days"] = openDays

    def getOpenDays(self):
        return self.__openDays

    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

    def setPhoneDays(self, phoneDays):
        self.__phoneDays = phoneDays
        self.__apiParas["phone_days"] = phoneDays

    def getPhoneDays(self):
        return self.__phoneDays

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setProvinceId(self, provinceId):
        self.__provinceId = provinceId
        self.__apiParas["province_id"] = provinceId

    def getProvinceId(self):
        return self.__provinceId

    def setRejectPercentApply(self, rejectPercentApply):
        self.__rejectPercentApply = rejectPercentApply
        self.__apiParas["reject_percent_apply"] = rejectPercentApply

    def getRejectPercentApply(self):
        return self.__rejectPercentApply

    def setSumInfoCostMoney(self, sumInfoCostMoney):
        self.__sumInfoCostMoney = sumInfoCostMoney
        self.__apiParas["sum_info_cost_money"] = sumInfoCostMoney

    def getSumInfoCostMoney(self):
        return self.__sumInfoCostMoney

    def setTopContact(self, topContact):
        self.__topContact = topContact
        self.__apiParas["top_contact"] = topContact

    def getTopContact(self):
        return self.__topContact

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def setWhiteGrade(self, whiteGrade):
        self.__whiteGrade = whiteGrade
        self.__apiParas["white_grade"] = whiteGrade

    def getWhiteGrade(self):
        return self.__whiteGrade

    def setWorkCityCount(self, workCityCount):
        self.__workCityCount = workCityCount
        self.__apiParas["work_city_count"] = workCityCount

    def getWorkCityCount(self):
        return self.__workCityCount

    def getApiMethodName(self):
        return "zhima.credit.bqs.defaultscore.query"

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
