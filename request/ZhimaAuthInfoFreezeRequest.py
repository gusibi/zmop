#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.info.freeze request
:author: auto create
:date: 2016-03-31 14:34:57
'''


class ZhimaAuthInfoFreezeRequest:
    def __init__(self):
        self.__bizNo = '' # 用户在商户处申请业务的唯一识别码;\n每个申请仅对应一条冻结记录，若存在相同流水号的冻结周期将覆盖
        self.__bizParams = '' # 扩展字段，json字符串的key-value格式
        self.__bizType = '' # 申请原因001: 贷款申请中, 002:信用卡申请中, 003:租车申请中, 004:信贷服务期内, 005:信贷逾期中
        self.__endDate = '' # 冻结结束时间，若该时间减去冻结开始时间的差值大于冻结周期，则该时间将赋值冻结开始时间+冻结周期
        self.__openId = '' # 用户在商端的身份标识
        self.__startDate = '' # 冻结开始时间，若该时间早于系统当前时间，则会取当前时间作为冻结开始时间

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizNo(self, bizNo):
        self.__bizNo = bizNo
        self.__apiParas["biz_no"] = bizNo

    def getBizNo(self):
        return self.__bizNo

    def setBizParams(self, bizParams):
        self.__bizParams = bizParams
        self.__apiParas["biz_params"] = bizParams

    def getBizParams(self):
        return self.__bizParams

    def setBizType(self, bizType):
        self.__bizType = bizType
        self.__apiParas["biz_type"] = bizType

    def getBizType(self):
        return self.__bizType

    def setEndDate(self, endDate):
        self.__endDate = endDate
        self.__apiParas["end_date"] = endDate

    def getEndDate(self):
        return self.__endDate

    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

    def setStartDate(self, startDate):
        self.__startDate = startDate
        self.__apiParas["start_date"] = startDate

    def getStartDate(self):
        return self.__startDate

    def getApiMethodName(self):
        return "zhima.auth.info.freeze"

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
