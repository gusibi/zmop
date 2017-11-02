#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.profile.status.feedback request
:author: auto create
:date: 2016-03-31 14:36:04
'''


class ZhimaProfileStatusFeedbackRequest:
    def __init__(self):
        self.__bizNo = '' # 业务号
        self.__bizType = '' # 业务类型
        self.__dataSource = '' # 当前为BANK或者ACCUFUND
        self.__itemCode = '' # 数据抓取code
        self.__memo = '' # 更新备注
        self.__orgCode = '' # 数据采集机构
        self.__status = '' # 数据状态

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

    def setBizType(self, bizType):
        self.__bizType = bizType
        self.__apiParas["biz_type"] = bizType

    def getBizType(self):
        return self.__bizType

    def setDataSource(self, dataSource):
        self.__dataSource = dataSource
        self.__apiParas["data_source"] = dataSource

    def getDataSource(self):
        return self.__dataSource

    def setItemCode(self, itemCode):
        self.__itemCode = itemCode
        self.__apiParas["item_code"] = itemCode

    def getItemCode(self):
        return self.__itemCode

    def setMemo(self, memo):
        self.__memo = memo
        self.__apiParas["memo"] = memo

    def getMemo(self):
        return self.__memo

    def setOrgCode(self, orgCode):
        self.__orgCode = orgCode
        self.__apiParas["org_code"] = orgCode

    def getOrgCode(self):
        return self.__orgCode

    def setStatus(self, status):
        self.__status = status
        self.__apiParas["status"] = status

    def getStatus(self):
        return self.__status

    def getApiMethodName(self):
        return "zhima.profile.status.feedback"

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
