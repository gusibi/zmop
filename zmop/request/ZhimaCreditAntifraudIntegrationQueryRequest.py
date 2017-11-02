#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.antifraud.integration.query request
:author: auto create
:date: 2017-10-13 15:10:00
'''


class ZhimaCreditAntifraudIntegrationQueryRequest:
    def __init__(self):
        self.__address = '' # 地址信息。省+市+区/县+详细地址，长度不超过256，不要包含特殊字符，如","，"\"，"|"，"&"，"^"
        self.__bankCard = '' # 银行卡号。中国大陆银行发布的银行卡:借记卡长度19位；信用卡长度16位；各位的取值位[0,9]的整数；不含虚拟卡
        self.__certNo = '' # 证件号。证件类型、证件号、姓名三要素均为必填参数
        self.__certType = '' # 证件类型。IDENTITY_CARD标识为身份证，目前仅支持身份证类型
        self.__email = '' # 电子邮箱。合法email，字母小写，特殊符号以半角形式出现
        self.__imei = '' # 国际移动设备标志。15位长度数字
        self.__ip = '' # ip地址。以"."分割的四段Ip，如 x.x.x.x，x为[0,255]之间的整数
        self.__mac = '' # 物理地址。支持格式如下：xx:xx:xx:xx:xx:xx，xx-xx-xx-xx-xx-xx，xxxxxxxxxxxx，x取值范围[0,9]之间的整数及A，B，C，D，E，F
        self.__mobile = '' # 手机号码。中国大陆合法手机号，长度11位，不含国家代码
        self.__name = '' # 姓名。长度不超过64，姓名中不要包含特殊字符，如","，"\"，"|"，"&"，"^"
        self.__productCode = '' # 产品码。标记商户接入的具体产品；直接使用每个接口入参中示例值即可
        self.__transactionId = '' # 商户请求的唯一标志，长度64位以内字符串，仅限字母数字下划线组合。该标识作为业务调用的唯一标识，商户要保证其业务唯一性，使用相同transaction_id的查询，芝麻在一段时间内（一般为1天）返回首次查询结果，超过有效期的查询即为无效并返回异常，有效期内的重复查询不重新计费
        self.__wifimac = '' # wifi的物理地址。支持格式如下：xx:xx:xx:xx:xx:xx，xx-xx-xx-xx-xx-xx，xxxxxxxxxxxx，x取值范围[0,9]之间的整数及A，B，C，D，E，F

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAddress(self, address):
        self.__address = address
        self.__apiParas["address"] = address

    def getAddress(self):
        return self.__address

    def setBankCard(self, bankCard):
        self.__bankCard = bankCard
        self.__apiParas["bank_card"] = bankCard

    def getBankCard(self):
        return self.__bankCard

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

    def setEmail(self, email):
        self.__email = email
        self.__apiParas["email"] = email

    def getEmail(self):
        return self.__email

    def setImei(self, imei):
        self.__imei = imei
        self.__apiParas["imei"] = imei

    def getImei(self):
        return self.__imei

    def setIp(self, ip):
        self.__ip = ip
        self.__apiParas["ip"] = ip

    def getIp(self):
        return self.__ip

    def setMac(self, mac):
        self.__mac = mac
        self.__apiParas["mac"] = mac

    def getMac(self):
        return self.__mac

    def setMobile(self, mobile):
        self.__mobile = mobile
        self.__apiParas["mobile"] = mobile

    def getMobile(self):
        return self.__mobile

    def setName(self, name):
        self.__name = name
        self.__apiParas["name"] = name

    def getName(self):
        return self.__name

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def setWifimac(self, wifimac):
        self.__wifimac = wifimac
        self.__apiParas["wifimac"] = wifimac

    def getWifimac(self):
        return self.__wifimac

    def getApiMethodName(self):
        return "zhima.credit.antifraud.integration.query"

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
