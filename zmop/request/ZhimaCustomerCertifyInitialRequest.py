#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.certify.initial request
:author: auto create
:date: 2017-06-19 11:23:32
'''


class ZhimaCustomerCertifyInitialRequest:
    def __init__(self):
        self.__bizParams = '' # 业务扩展参数入参，传递方式例如{"xx":"xxxxx"};针对KBA的认证方式需要关注，biz_params中需要传入入参：{"verifyScene":"向芝麻申请获得的scene值"}
        self.__contractFlag = '' # 与芝麻信用签订的合约外标，即使合约改签或续签该值不会发生变化。请联系技术支持
        self.__identityParam = '' # 不同身份类型的参数列表，json字符串的key-value格式：如：当identity_type= "BY_CERTNO_AND_NAME";时identity_param={"certNo":"xxx","name":"张三","certType":"IDENTITY_CARD","mobileNo":"13901234567"};或者当identity_type= "BY_MOBILE_NO";时identity_param={"mobileNo":"13901234567"};或者当identify_type="BY_CERT_IMAGE"identity_param={"frontCertImage":"oioiweroeworewoiho2323","backCertImage":"dsrrwerewew"}
        self.__identityType = '' # 身份标识类型（后续可以扩展）：BY_CERTNO_AND_NAME:按照身份证+姓名（手机号可选）进行身份识别BY_MOBILE_NO:按照手机号进行身份识别BY_CERT_IMAGE: 根据证件图片识别
        self.__pageUrl = '' # 商户页面回调地址，芝麻认证完成后通过此url地址回传给商户认证的结果；SDK模式接入的场景为非必填项，其他渠道类型的必填项；
        self.__productCode = '' # 当前使用的产品码
        self.__schemaUrl = '' # 商户App的回调地址，通过商户App发起人脸核身的芝麻认证时必传；其他场景为非必填项；
        self.__sourceType = '' # 请求来源类型，为比填项， 例如h5, pc , app, sdk,window；1.h5 ：商户H5端接入芝麻应用的场景；2.pc：商户pc端接入芝麻认证的场景；3.app：商户app应用接入芝麻认证的场景；4.sdk：商户调用芝麻的sdk进行芝麻认证的场景:5.window：服务窗进行芝麻认证的场景；
        self.__state = '' # 芝麻认证过程中的冗余字段，在认证申请时传入，在结果页面回调中原样透传给商户端。支持json格式。【建议使用方式】用于商户端唯一标记发起认证的用户信息，在接收到芝麻信用认证结果回调后确定用户
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddhhmmssSSS，后13位为自增数字。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizParams(self, bizParams):
        self.__bizParams = bizParams
        self.__apiParas["biz_params"] = bizParams

    def getBizParams(self):
        return self.__bizParams

    def setContractFlag(self, contractFlag):
        self.__contractFlag = contractFlag
        self.__apiParas["contract_flag"] = contractFlag

    def getContractFlag(self):
        return self.__contractFlag

    def setIdentityParam(self, identityParam):
        self.__identityParam = identityParam
        self.__apiParas["identity_param"] = identityParam

    def getIdentityParam(self):
        return self.__identityParam

    def setIdentityType(self, identityType):
        self.__identityType = identityType
        self.__apiParas["identity_type"] = identityType

    def getIdentityType(self):
        return self.__identityType

    def setPageUrl(self, pageUrl):
        self.__pageUrl = pageUrl
        self.__apiParas["page_url"] = pageUrl

    def getPageUrl(self):
        return self.__pageUrl

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setSchemaUrl(self, schemaUrl):
        self.__schemaUrl = schemaUrl
        self.__apiParas["schema_url"] = schemaUrl

    def getSchemaUrl(self):
        return self.__schemaUrl

    def setSourceType(self, sourceType):
        self.__sourceType = sourceType
        self.__apiParas["source_type"] = sourceType

    def getSourceType(self):
        return self.__sourceType

    def setState(self, state):
        self.__state = state
        self.__apiParas["state"] = state

    def getState(self):
        return self.__state

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def getApiMethodName(self):
        return "zhima.customer.certify.initial"

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
