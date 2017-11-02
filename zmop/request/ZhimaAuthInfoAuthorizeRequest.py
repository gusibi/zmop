#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.info.authorize request
:author: auto create
:date: 2017-04-07 10:46:17
'''


class ZhimaAuthInfoAuthorizeRequest:
    def __init__(self):
        self.__bizParams = '' # 业务扩展字段,页面授权接口需要传入auth_code,channelType,stateauth_code授权码,值取决于授权方式和身份类型PC方式,身份类型identity_type=1:{"auth_code":"M_MOBILE_APPPC"}PC方式,身份类型identity_type=2:{"auth_code":"M_APPPC_CERT"}H5方式(身份类型identity_type为任何值):{"auth_code":"M_H5"}SDK方式(身份类型identity_type为任何值):{"auth_code":"M_APPSDK"}channelType渠道类型,每个授权码支持不同的渠道类型appsdk:sdk接入apppc:商户pc页面接入api:后台api接入windows:支付宝服务窗接入app:商户app接入state是商户自定义的数据,页面授权接口会原样把这个数据返回个商户
        self.__identityParam = '' # 不同身份类型传入的参数列表,json字符串的key-value格式身份类型identityType=1:{"mobileNo":"15158657683"}身份类型identityType=2:{"certNo":"330100xxxxxxxxxxxx","name":"张三","certType":"IDENTITY_CARD"}
        self.__identityType = '' # 身份标识类型<p>1:按照手机号进行授权</p>2:按照身份证+姓名进行授权

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

    def getApiMethodName(self):
        return "zhima.auth.info.authorize"

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
