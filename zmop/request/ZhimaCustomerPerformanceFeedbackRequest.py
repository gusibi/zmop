#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.performance.feedback request
:author: auto create
:date: 2016-12-22 17:42:59
'''


class ZhimaCustomerPerformanceFeedbackRequest:
    def __init__(self):
        self.__certNo = '' # 用户证件号码
        self.__certType = '' # 证件类型
        self.__name = '' # 用户姓名
        self.__repayments = '' # 商户反馈的某用户还款计划数据，格式：[{"repayment_id": "1234","repayment_desc": "商品名称","installments": [{"installment_id": "1234","installment_amount": "1000","installment_date": "2016-09-11 12:00:00","installment_desc": "已逾期7天","installment_status": "WAITING_REPAY","currency": "CNY"}]}]

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

    def setName(self, name):
        self.__name = name
        self.__apiParas["name"] = name

    def getName(self):
        return self.__name

    def setRepayments(self, repayments):
        self.__repayments = repayments
        self.__apiParas["repayments"] = repayments

    def getRepayments(self):
        return self.__repayments

    def getApiMethodName(self):
        return "zhima.customer.performance.feedback"

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
