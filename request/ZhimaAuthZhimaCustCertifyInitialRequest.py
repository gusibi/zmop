#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.zhima.cust.certify.initial request
:author: auto create
:date: 2016-03-31 14:34:57
'''


class ZhimaAuthZhimaCustCertifyInitialRequest:
    def __init__(self):
        self.__bizParams = '' # 业务扩展属性：来源类型source_type必传，比如：1.web场景中，传入{“source_type”:"pc"}2.移动端场景中，传入{“source_type”:"h5"}
        self.__contractFlag = '' # 与芝麻信用签订的合约外标，即使合约改签或续签该值不会发生变化
        self.__identityParam = '' # 不同身份类型的参数列表，json字符串的key-value格式：如：identity_type= "CERT_AND_MOBILE";identity_param={"certNo":"xxx", "name":"张三", "certType":"IDENTITY_CARD"};
        self.__identityType = '' # 身份标识类型（后续可以扩展）：BY_CERTNO_AND_NAME:按照身份证+姓名（+手机号）进行授权
        self.__productCode = '' # 当前使用的产品码
        self.__state = '' # 芝麻认证过程中的冗余字段，在认证申请时传入，在结果页面回调中原样透传给商户端。【建议使用方式】用于商户端唯一标记发起认证的用户信息，在接收到芝麻信用认证结果回调后确定用户
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间

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

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

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
        return "zhima.auth.zhima.cust.certify.initial"

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
