#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.certification.result.sync request
:author: auto create
:date: 2017-04-20 19:49:37
'''


class ZhimaCustomerCertificationResultSyncRequest:
    def __init__(self):
        self.__bizNo = '' # 一次认证的唯一标识,在商户调用认证初始化接口的时候获取
        self.__channelStatuses = '' # 各渠道认证状态,失败原因,材料等信息
        self.__errorCode = '' # 认证失败的错误码
        self.__errorMessage = '' # 认证失败的错误信息
        self.__extBizParam = '' # 扩展业务参数
        self.__identifiedPrincipal = '' # 识别后的主体信息,入参有传就和入参的certify_identity一致
        self.__merchantId = '' # 商户id,商户在芝麻的唯一标识
        self.__passed = '' # 认证是否通过

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

    def setChannelStatuses(self, channelStatuses):
        self.__channelStatuses = channelStatuses
        self.__apiParas["channel_statuses"] = channelStatuses

    def getChannelStatuses(self):
        return self.__channelStatuses

    def setErrorCode(self, errorCode):
        self.__errorCode = errorCode
        self.__apiParas["error_code"] = errorCode

    def getErrorCode(self):
        return self.__errorCode

    def setErrorMessage(self, errorMessage):
        self.__errorMessage = errorMessage
        self.__apiParas["error_message"] = errorMessage

    def getErrorMessage(self):
        return self.__errorMessage

    def setExtBizParam(self, extBizParam):
        self.__extBizParam = extBizParam
        self.__apiParas["ext_biz_param"] = extBizParam

    def getExtBizParam(self):
        return self.__extBizParam

    def setIdentifiedPrincipal(self, identifiedPrincipal):
        self.__identifiedPrincipal = identifiedPrincipal
        self.__apiParas["identified_principal"] = identifiedPrincipal

    def getIdentifiedPrincipal(self):
        return self.__identifiedPrincipal

    def setMerchantId(self, merchantId):
        self.__merchantId = merchantId
        self.__apiParas["merchant_id"] = merchantId

    def getMerchantId(self):
        return self.__merchantId

    def setPassed(self, passed):
        self.__passed = passed
        self.__apiParas["passed"] = passed

    def getPassed(self):
        return self.__passed

    def getApiMethodName(self):
        return "zhima.customer.certification.result.sync"

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
