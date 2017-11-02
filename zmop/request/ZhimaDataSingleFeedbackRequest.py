#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.data.single.feedback request
:author: auto create
:date: 2017-09-06 13:16:35
'''


class ZhimaDataSingleFeedbackRequest:
    def __init__(self):
        self.__bizExtParams = '' # 扩展参数
        self.__data = '' # 反馈的json格式的数据内容
        self.__identity = '' # 主键使用反馈字段进行组合，也可以使用反馈的某个单字段（确保主键稳定，而且可以很好的区分不同的数据）。例如order_no#pay_month或者order_no#bill_month组合，对于一个order_no只会有一条数据的情况，直接使用order_no作为主键
        self.__typeId = '' # 芝麻系统中配置的值，由芝麻信用提供，需要匹配，测试反馈和正式反馈使用不同的TYPE_ID

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizExtParams(self, bizExtParams):
        self.__bizExtParams = bizExtParams
        self.__apiParas["biz_ext_params"] = bizExtParams

    def getBizExtParams(self):
        return self.__bizExtParams

    def setData(self, data):
        self.__data = data
        self.__apiParas["data"] = data

    def getData(self):
        return self.__data

    def setIdentity(self, identity):
        self.__identity = identity
        self.__apiParas["identity"] = identity

    def getIdentity(self):
        return self.__identity

    def setTypeId(self, typeId):
        self.__typeId = typeId
        self.__apiParas["type_id"] = typeId

    def getTypeId(self):
        return self.__typeId

    def getApiMethodName(self):
        return "zhima.data.single.feedback"

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
