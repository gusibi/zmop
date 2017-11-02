#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.enterprise.apply request
:author: auto create
:date: 2017-05-27 10:05:51
'''


class ZhimaMerchantEnterpriseApplyRequest:
    def __init__(self):
        self.__aliasName = '' # 商户别名
        self.__alipayWindowName = '' # 为用户提供服务的支付宝服务窗名称，如有请填写 支付宝服务窗，微信公众号，网站地址，应用名称必须是4选1
        self.__appName = '' # 为用户提供服务的手机应用，如有请填写 支付宝服务窗，微信公众号，网站地址，应用名称必须是4选1
        self.__applyMemo = '' # 用于记录本次提交信息中，那些字段有所调整
        self.__authLetterUrl = '' # 业务授权书url，请通过zhima.merchant.image.upload上传文件；在商户类型为政府机构或者事业单位时，与证照图片二选一；在商户类型为企业时，与法人信息二选一
        self.__bizScene = '' # 签约芝麻信用产品的用途，最多5个场景，ISV可以自定义
        self.__companyAddress = '' # 企业地址
        self.__companyName = '' # 企业名称
        self.__dataFeedbackContractEmail = '' # 数据反馈联系人邮箱地址(使用芝麻信用评分、行业关注名单时，联动解决数据问题的接口人。)
        self.__dataFeedbackContractMobile = '' # 数据反馈联系人手机号码(使用芝麻信用评分、行业关注名单时，联动解决数据问题的接口人。)
        self.__dataFeedbackContractName = '' # 数据反馈联系人姓名(使用芝麻信用评分、行业关注名单时，联动解决数据问题的接口人。)
        self.__endBusinessDate = '' # 证照结束日期9999-12-31   代表长期
        self.__legalCertNo = '' # 法人身份证号码在商户类型为企业时，与业务授权书二选一
        self.__legalCertNoBackImageUrl = '' # 法人身份证反面图片url请通过zhima.merchant.image.upload上传文件;在商户类型为企业时，与业务授权书二选一
        self.__legalCertNoFrontImageUrl = '' # 法人身份证正面图片url请通过zhima.merchant.image.upload上传文件;在商户类型为企业时，与业务授权书二选一
        self.__legalCertValidEndDate = '' # 法人身份证有效期结束日期;在商户类型为企业时，与业务授权书二选一
        self.__legalCertValidStartDate = '' # 法人身份证有效期开始日期;在商户类型为企业时，与业务授权书二选一
        self.__legalName = '' # 法人姓名在商户类型为企业时，与业务授权书二选一
        self.__licenseImageUrl = '' # 证照图片url，请通过zhima.merchant.image.upload上传对应证照类型的图片，在商户类型为政府机构或者事业单位时，与业务授权书二选一
        self.__licenseNo = '' # 证照号码
        self.__licenseType = '' # 证照类型：1:普通营业执照2:多证合一3:组织结构代码证4:其他证照company_type=1时，证照类型只能选择1和2；company_type=2,3时，证照类型只能选择3和4
        self.__logoImage = '' # 芝麻二级商户图标的二进制流,最大100K(80*80),需要对图片的二进制流做Base64处理转化成字符串
        self.__logoImageType = '' # 芝麻二级商户图标后缀：bmp, jpg, jpeg, png, gif
        self.__majorContractEmail = '' # 主要联系人邮箱地址(联系人将用于接收重要通知，如签约进度、技术集成、合同到期等)
        self.__majorContractMobile = '' # 主要联系人手机号码(联系人将用于接收重要通知，如签约进度、技术集成、合同到期等)
        self.__majorContractName = '' # 主要联系人姓名(联系人将用于接收重要通知，如签约进度、技术集成、合同到期等)
        self.__merchantType = '' # 商户类型1:企业2:政府机构3:事业单位
        self.__objectionContractEmail = '' # 异议处理联系人邮箱地址(用户对所披露的负面信息存在异议时，联动核查的接口人)
        self.__objectionContractMobile = '' # 异议处理联系人手机号码(用户对所披露的负面信息存在异议时，联动核查的接口人)
        self.__objectionContractName = '' # 异议处理联系人姓名(用户对所披露的负面信息存在异议时，联动核查的接口人)
        self.__oneLevelMcc = '' # 芝麻商户一级行业归属，芝麻提供
        self.__organizationImageUrl = '' # 组织结构代码证图片url,营业执照时普通类型时(废弃)
        self.__organizationNo = '' # 组织机构代码，营业执照时普通类型时(废弃)
        self.__outOrderNo = '' # 外部订单号
        self.__proxyCertNo = '' # 代理人身份证号码(废弃)
        self.__proxyCertNoBackImageUrl = '' # 代理人身份证反面图片url(废弃)
        self.__proxyCertNoFrontImageUrl = '' # 代理人身份证正面图片url(废弃)
        self.__proxyCertValidEndDate = '' # 代理人身份证有效期结束日期(废弃)
        self.__proxyCertValidStartDate = '' # 代理人身份证有效期开始日期(废弃)
        self.__proxyMandateUrl = '' # 代理人委托书url地址(废弃)
        self.__proxyName = '' # 代理人姓名(废弃)
        self.__qualificationImageUrl = '' # 业务许可证图片url请通过zhima.merchant.image.upload上传文件
        self.__serviceContractEmail = '' # 服务联动联系人邮箱地址(联动解决用户服务相关问题的接口人。比如用户投诉或出现重大服务事件时，可以协调解决问题的联系人)
        self.__serviceContractMobile = '' # 服务联动联系人手机号码(联动解决用户服务相关问题的接口人。比如用户投诉或出现重大服务事件时，可以协调解决问题的联系人)
        self.__serviceContractName = '' # 服务联动联系人姓名(联动解决用户服务相关问题的接口人。比如用户投诉或出现重大服务事件时，可以协调解决问题的联系人)
        self.__startBusinessDate = '' # 证照开始日期
        self.__twoLevelMcc = '' # 芝麻商户二级行业归属，芝麻提供
        self.__webchatAmount = '' # 用户提供服务的微信公众号，如有请填写 支付宝服务窗，微信公众号，网站地址，应用名称必须是4选1
        self.__websitUrl = '' # 为用户提供服务的网站，如有请填写 支付宝服务窗，微信公众号，网站地址，应用名称必须是4选1

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

    def setAuthLetterUrl(self, authLetterUrl):
        self.__authLetterUrl = authLetterUrl
        self.__apiParas["auth_letter_url"] = authLetterUrl

    def getAuthLetterUrl(self):
        return self.__authLetterUrl

    def setBizScene(self, bizScene):
        self.__bizScene = bizScene
        self.__apiParas["biz_scene"] = bizScene

    def getBizScene(self):
        return self.__bizScene

    def setCompanyAddress(self, companyAddress):
        self.__companyAddress = companyAddress
        self.__apiParas["company_address"] = companyAddress

    def getCompanyAddress(self):
        return self.__companyAddress

    def setCompanyName(self, companyName):
        self.__companyName = companyName
        self.__apiParas["company_name"] = companyName

    def getCompanyName(self):
        return self.__companyName

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

    def setEndBusinessDate(self, endBusinessDate):
        self.__endBusinessDate = endBusinessDate
        self.__apiParas["end_business_date"] = endBusinessDate

    def getEndBusinessDate(self):
        return self.__endBusinessDate

    def setLegalCertNo(self, legalCertNo):
        self.__legalCertNo = legalCertNo
        self.__apiParas["legal_cert_no"] = legalCertNo

    def getLegalCertNo(self):
        return self.__legalCertNo

    def setLegalCertNoBackImageUrl(self, legalCertNoBackImageUrl):
        self.__legalCertNoBackImageUrl = legalCertNoBackImageUrl
        self.__apiParas["legal_cert_no_back_image_url"] = legalCertNoBackImageUrl

    def getLegalCertNoBackImageUrl(self):
        return self.__legalCertNoBackImageUrl

    def setLegalCertNoFrontImageUrl(self, legalCertNoFrontImageUrl):
        self.__legalCertNoFrontImageUrl = legalCertNoFrontImageUrl
        self.__apiParas["legal_cert_no_front_image_url"] = legalCertNoFrontImageUrl

    def getLegalCertNoFrontImageUrl(self):
        return self.__legalCertNoFrontImageUrl

    def setLegalCertValidEndDate(self, legalCertValidEndDate):
        self.__legalCertValidEndDate = legalCertValidEndDate
        self.__apiParas["legal_cert_valid_end_date"] = legalCertValidEndDate

    def getLegalCertValidEndDate(self):
        return self.__legalCertValidEndDate

    def setLegalCertValidStartDate(self, legalCertValidStartDate):
        self.__legalCertValidStartDate = legalCertValidStartDate
        self.__apiParas["legal_cert_valid_start_date"] = legalCertValidStartDate

    def getLegalCertValidStartDate(self):
        return self.__legalCertValidStartDate

    def setLegalName(self, legalName):
        self.__legalName = legalName
        self.__apiParas["legal_name"] = legalName

    def getLegalName(self):
        return self.__legalName

    def setLicenseImageUrl(self, licenseImageUrl):
        self.__licenseImageUrl = licenseImageUrl
        self.__apiParas["license_image_url"] = licenseImageUrl

    def getLicenseImageUrl(self):
        return self.__licenseImageUrl

    def setLicenseNo(self, licenseNo):
        self.__licenseNo = licenseNo
        self.__apiParas["license_no"] = licenseNo

    def getLicenseNo(self):
        return self.__licenseNo

    def setLicenseType(self, licenseType):
        self.__licenseType = licenseType
        self.__apiParas["license_type"] = licenseType

    def getLicenseType(self):
        return self.__licenseType

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

    def setMerchantType(self, merchantType):
        self.__merchantType = merchantType
        self.__apiParas["merchant_type"] = merchantType

    def getMerchantType(self):
        return self.__merchantType

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

    def setOrganizationImageUrl(self, organizationImageUrl):
        self.__organizationImageUrl = organizationImageUrl
        self.__apiParas["organization_image_url"] = organizationImageUrl

    def getOrganizationImageUrl(self):
        return self.__organizationImageUrl

    def setOrganizationNo(self, organizationNo):
        self.__organizationNo = organizationNo
        self.__apiParas["organization_no"] = organizationNo

    def getOrganizationNo(self):
        return self.__organizationNo

    def setOutOrderNo(self, outOrderNo):
        self.__outOrderNo = outOrderNo
        self.__apiParas["out_order_no"] = outOrderNo

    def getOutOrderNo(self):
        return self.__outOrderNo

    def setProxyCertNo(self, proxyCertNo):
        self.__proxyCertNo = proxyCertNo
        self.__apiParas["proxy_cert_no"] = proxyCertNo

    def getProxyCertNo(self):
        return self.__proxyCertNo

    def setProxyCertNoBackImageUrl(self, proxyCertNoBackImageUrl):
        self.__proxyCertNoBackImageUrl = proxyCertNoBackImageUrl
        self.__apiParas["proxy_cert_no_back_image_url"] = proxyCertNoBackImageUrl

    def getProxyCertNoBackImageUrl(self):
        return self.__proxyCertNoBackImageUrl

    def setProxyCertNoFrontImageUrl(self, proxyCertNoFrontImageUrl):
        self.__proxyCertNoFrontImageUrl = proxyCertNoFrontImageUrl
        self.__apiParas["proxy_cert_no_front_image_url"] = proxyCertNoFrontImageUrl

    def getProxyCertNoFrontImageUrl(self):
        return self.__proxyCertNoFrontImageUrl

    def setProxyCertValidEndDate(self, proxyCertValidEndDate):
        self.__proxyCertValidEndDate = proxyCertValidEndDate
        self.__apiParas["proxy_cert_valid_end_date"] = proxyCertValidEndDate

    def getProxyCertValidEndDate(self):
        return self.__proxyCertValidEndDate

    def setProxyCertValidStartDate(self, proxyCertValidStartDate):
        self.__proxyCertValidStartDate = proxyCertValidStartDate
        self.__apiParas["proxy_cert_valid_start_date"] = proxyCertValidStartDate

    def getProxyCertValidStartDate(self):
        return self.__proxyCertValidStartDate

    def setProxyMandateUrl(self, proxyMandateUrl):
        self.__proxyMandateUrl = proxyMandateUrl
        self.__apiParas["proxy_mandate_url"] = proxyMandateUrl

    def getProxyMandateUrl(self):
        return self.__proxyMandateUrl

    def setProxyName(self, proxyName):
        self.__proxyName = proxyName
        self.__apiParas["proxy_name"] = proxyName

    def getProxyName(self):
        return self.__proxyName

    def setQualificationImageUrl(self, qualificationImageUrl):
        self.__qualificationImageUrl = qualificationImageUrl
        self.__apiParas["qualification_image_url"] = qualificationImageUrl

    def getQualificationImageUrl(self):
        return self.__qualificationImageUrl

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

    def setStartBusinessDate(self, startBusinessDate):
        self.__startBusinessDate = startBusinessDate
        self.__apiParas["start_business_date"] = startBusinessDate

    def getStartBusinessDate(self):
        return self.__startBusinessDate

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
        return "zhima.merchant.enterprise.apply"

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
