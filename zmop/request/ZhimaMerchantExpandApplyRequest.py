#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.expand.apply request
:author: auto create
:date: 2017-05-16 11:44:21
'''


class ZhimaMerchantExpandApplyRequest:
    def __init__(self):
        self.__aliasName = '' # 浙江飞猪网络技术有限公司，企业别称请填写【飞猪】
        self.__alipayWindowName = '' # 为用户提供服务的支付宝服务窗名称，如有请填写支付宝服务窗，微信公众号，网站地址，应用名称必须是4选1
        self.__appName = '' # 为用户提供服务的手机应用，如有请填写支付宝服务窗，微信公众号，网站地址，应用名称必须是4选1
        self.__applyMemo = '' # 用于记录本次提交信息中，那些字段有所调整
        self.__bizScene = '' # 签约芝麻信用产品的用途，最多5个场景，ISV可以自定义
        self.__dataFeedbackContractEmail = '' # 数据反馈联系人邮箱地址(使用芝麻信用评分、行业关注名单时，联动解决数据问题的接口人。)
        self.__dataFeedbackContractMobile = '' # 数据反馈联系人手机号码(使用芝麻信用评分、行业关注名单时，联动解决数据问题的接口人。)
        self.__dataFeedbackContractName = '' # 数据反馈联系人姓名(使用芝麻信用评分、行业关注名单时，联动解决数据问题的接口人。)
        self.__logoImage = '' # 商户logo的图片内容，把图片的二进制转化成String传递过来，最大2M
        self.__logoImageType = '' # 商户图标类型，只支持如下格式：bmp, jpg, jpeg, png, gif
        self.__majorContractEmail = '' # 主要联系人邮箱地址(联系人将用于接收重要通知，如签约进度、技术集成、合同到期等)
        self.__majorContractMobile = '' # 主要联系人手机号码(联系人将用于接收重要通知，如签约进度、技术集成、合同到期等)
        self.__majorContractName = '' # 主要联系人姓名(联系人将用于接收重要通知，如签约进度、技术集成、合同到期等)
        self.__objectionContractEmail = '' # 异议处理联系人邮箱地址(用户对所披露的负面信息存在异议时，联动核查的接口人)
        self.__objectionContractMobile = '' # 异议处理联系人手机号码(用户对所披露的负面信息存在异议时，联动核查的接口人)
        self.__objectionContractName = '' # 异议处理联系人姓名(用户对所披露的负面信息存在异议时，联动核查的接口人)
        self.__oneLevelMcc = '' # 芝麻特定的商户一级行业归属，比如生活行业，金融行业，政府行业
        self.__qualificationImage = '' # 商户业务许可证图片内容，把图片的二进制转化成String传递过来，最大2M
        self.__qualificationImageType = '' # 商户业务许可证图片类型，只支持如下格式：bmp, jpg, jpeg, png, gif
        self.__serviceContractEmail = '' # 服务联动联系人邮箱地址(联动解决用户服务相关问题的接口人。比如用户投诉或出现重大服务事件时，可以协调解决问题的联系人)
        self.__serviceContractMobile = '' # 服务联动联系人手机号码(联动解决用户服务相关问题的接口人。比如用户投诉或出现重大服务事件时，可以协调解决问题的联系人)
        self.__serviceContractName = '' # 服务联动联系人姓名(联动解决用户服务相关问题的接口人。比如用户投诉或出现重大服务事件时，可以协调解决问题的联系人)
        self.__twoLevelMcc = '' # 芝麻特有的商户二级行业归属，比如汽车服务
        self.__webchatAmount = '' # 用户提供服务的微信公众号，如有请填写支付宝服务窗，微信公众号，网站地址，应用名称必须是4选1
        self.__websitUrl = '' # 为用户提供服务的网站，如有请填写支付宝服务窗，微信公众号，网站地址，应用名称必须是4选1

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAliasName(self, aliasName):
        self.__aliasName = aliasName
        self.__apiParas["alias_name"] = aliasName

    def getAliasName(self):
        return self.__aliasName

    def setAlipayWindowName(self, alipayWindowName):
        self.__alipayWindowName = alipayWindowName
        self.__apiParas["alipay_window_name"] = alipayWindowName

    def getAlipayWindowName(self):
        return self.__alipayWindowName

    def setAppName(self, appName):
        self.__appName = appName
        self.__apiParas["app_name"] = appName

    def getAppName(self):
        return self.__appName

    def setApplyMemo(self, applyMemo):
        self.__applyMemo = applyMemo
        self.__apiParas["apply_memo"] = applyMemo

    def getApplyMemo(self):
        return self.__applyMemo

    def setBizScene(self, bizScene):
        self.__bizScene = bizScene
        self.__apiParas["biz_scene"] = bizScene

    def getBizScene(self):
        return self.__bizScene

    def setDataFeedbackContractEmail(self, dataFeedbackContractEmail):
        self.__dataFeedbackContractEmail = dataFeedbackContractEmail
        self.__apiParas["data_feedback_contract_email"] = dataFeedbackContractEmail

    def getDataFeedbackContractEmail(self):
        return self.__dataFeedbackContractEmail

    def setDataFeedbackContractMobile(self, dataFeedbackContractMobile):
        self.__dataFeedbackContractMobile = dataFeedbackContractMobile
        self.__apiParas["data_feedback_contract_mobile"] = dataFeedbackContractMobile

    def getDataFeedbackContractMobile(self):
        return self.__dataFeedbackContractMobile

    def setDataFeedbackContractName(self, dataFeedbackContractName):
        self.__dataFeedbackContractName = dataFeedbackContractName
        self.__apiParas["data_feedback_contract_name"] = dataFeedbackContractName

    def getDataFeedbackContractName(self):
        return self.__dataFeedbackContractName

    def setLogoImage(self, logoImage):
        self.__logoImage = logoImage
        self.__apiParas["logo_image"] = logoImage

    def getLogoImage(self):
        return self.__logoImage

    def setLogoImageType(self, logoImageType):
        self.__logoImageType = logoImageType
        self.__apiParas["logo_image_type"] = logoImageType

    def getLogoImageType(self):
        return self.__logoImageType

    def setMajorContractEmail(self, majorContractEmail):
        self.__majorContractEmail = majorContractEmail
        self.__apiParas["major_contract_email"] = majorContractEmail

    def getMajorContractEmail(self):
        return self.__majorContractEmail

    def setMajorContractMobile(self, majorContractMobile):
        self.__majorContractMobile = majorContractMobile
        self.__apiParas["major_contract_mobile"] = majorContractMobile

    def getMajorContractMobile(self):
        return self.__majorContractMobile

    def setMajorContractName(self, majorContractName):
        self.__majorContractName = majorContractName
        self.__apiParas["major_contract_name"] = majorContractName

    def getMajorContractName(self):
        return self.__majorContractName

    def setObjectionContractEmail(self, objectionContractEmail):
        self.__objectionContractEmail = objectionContractEmail
        self.__apiParas["objection_contract_email"] = objectionContractEmail

    def getObjectionContractEmail(self):
        return self.__objectionContractEmail

    def setObjectionContractMobile(self, objectionContractMobile):
        self.__objectionContractMobile = objectionContractMobile
        self.__apiParas["objection_contract_mobile"] = objectionContractMobile

    def getObjectionContractMobile(self):
        return self.__objectionContractMobile

    def setObjectionContractName(self, objectionContractName):
        self.__objectionContractName = objectionContractName
        self.__apiParas["objection_contract_name"] = objectionContractName

    def getObjectionContractName(self):
        return self.__objectionContractName

    def setOneLevelMcc(self, oneLevelMcc):
        self.__oneLevelMcc = oneLevelMcc
        self.__apiParas["one_level_mcc"] = oneLevelMcc

    def getOneLevelMcc(self):
        return self.__oneLevelMcc

    def setQualificationImage(self, qualificationImage):
        self.__qualificationImage = qualificationImage
        self.__apiParas["qualification_image"] = qualificationImage

    def getQualificationImage(self):
        return self.__qualificationImage

    def setQualificationImageType(self, qualificationImageType):
        self.__qualificationImageType = qualificationImageType
        self.__apiParas["qualification_image_type"] = qualificationImageType

    def getQualificationImageType(self):
        return self.__qualificationImageType

    def setServiceContractEmail(self, serviceContractEmail):
        self.__serviceContractEmail = serviceContractEmail
        self.__apiParas["service_contract_email"] = serviceContractEmail

    def getServiceContractEmail(self):
        return self.__serviceContractEmail

    def setServiceContractMobile(self, serviceContractMobile):
        self.__serviceContractMobile = serviceContractMobile
        self.__apiParas["service_contract_mobile"] = serviceContractMobile

    def getServiceContractMobile(self):
        return self.__serviceContractMobile

    def setServiceContractName(self, serviceContractName):
        self.__serviceContractName = serviceContractName
        self.__apiParas["service_contract_name"] = serviceContractName

    def getServiceContractName(self):
        return self.__serviceContractName

    def setTwoLevelMcc(self, twoLevelMcc):
        self.__twoLevelMcc = twoLevelMcc
        self.__apiParas["two_level_mcc"] = twoLevelMcc

    def getTwoLevelMcc(self):
        return self.__twoLevelMcc

    def setWebchatAmount(self, webchatAmount):
        self.__webchatAmount = webchatAmount
        self.__apiParas["webchat_amount"] = webchatAmount

    def getWebchatAmount(self):
        return self.__webchatAmount

    def setWebsitUrl(self, websitUrl):
        self.__websitUrl = websitUrl
        self.__apiParas["websit_url"] = websitUrl

    def getWebsitUrl(self):
        return self.__websitUrl

    def getApiMethodName(self):
        return "zhima.merchant.expand.apply"

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
