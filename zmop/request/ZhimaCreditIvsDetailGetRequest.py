#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.ivs.detail.get request
:author: auto create
:date: 2016-07-29 18:46:29
'''


class ZhimaCreditIvsDetailGetRequest:
    def __init__(self):
        self.__address = '' # 用户地址，最多输入三个，多个地址之间用|分隔，如 杭州市西湖区天目山路266号|杭州市西湖区万塘路999号。备注：证件号、姓名、手机号、地址、银行卡、电子邮箱至少传其中两项
        self.__bankCard = '' # 银行卡号，最多输入两个，多个银行卡号之间用|分隔，如602436748024138|622536748024139。备注：证件号、姓名、手机号、地址、银行卡、电子邮箱至少传其中两项
        self.__certNo = '' # 证件号。备注：证件号、姓名、手机号、地址、银行卡、电子邮箱必须传其中两项
        self.__certType = '' # 证件类型。备注：证件号、姓名、手机号、地址、银行卡、电子邮箱至少传其中两项
        self.__email = '' # 电子邮箱，最多传入两个，多个邮箱之间用|分隔，如jnlxhy@alitest.com|john.sss@alitest.com。备注：证件号、姓名、手机号、地址、银行卡、电子邮箱必至少传其中两项
        self.__imei = '' # 国际移动设备标志
        self.__imsi = '' # 国际移动用户识别码
        self.__ip = '' # ip地址
        self.__mac = '' # 物理地址
        self.__mobile = '' # 手机号，最多传入三个，多个手机号之间用|分隔，如15256797367|18669152789。备注：证件号、姓名、手机号、地址、银行卡、电子邮箱至少传其中两项
        self.__name = '' # 姓名。备注：证件号、姓名、手机号、地址、银行卡、电子邮箱至少传其中两项
        self.__productCode = '' # 产品码
        self.__transactionId = '' # transaction_id是代表一笔请求的唯一标志，该标识作为对账的关键信息，对于用户使用相同transaction_id的查询，芝麻在一天（86400秒）内返回首次查询数据，超过有效期的查询即为无效并返回异常（错误码xxxx），有效期内的重复查询不重新计费。 transaction_id 推荐生成方式是：30位，（其中17位时间值（精确到毫秒）：yyyyMMddHHmmssSSS）加上（13位自增数字：1234567890123）
        self.__wifimac = '' # wifi的物理地址

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

    def setImsi(self, imsi):
        self.__imsi = imsi
        self.__apiParas["imsi"] = imsi

    def getImsi(self):
        return self.__imsi

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
        return "zhima.credit.ivs.detail.get"

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
