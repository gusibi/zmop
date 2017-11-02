#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.vehicle.verify request
:author: auto create
:date: 2016-08-06 15:11:27
'''


class ZhimaCreditVehicleVerifyRequest:
    def __init__(self):
        self.__engineNo = '' # 发动机号码。vin与engine_no至少包含一项
        self.__owner = '' # 所有人，支持个人和机构
        self.__plateNo = '' # 车牌号
        self.__productCode = '' # 产品码
        self.__registerDate = '' # 注册日期，格式yyyyMMdd
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddHHmmssSSS，后13位为自增数字。
        self.__vehicleBrand = '' # 车辆品牌（行驶证中中文部分）
        self.__vehicleSeries = '' # 车辆型号（行驶证中英文部分）
        self.__vin = '' # 车辆识别代号。vin与engine_no至少包含一项

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setEngineNo(self, engineNo):
        self.__engineNo = engineNo
        self.__apiParas["engine_no"] = engineNo

    def getEngineNo(self):
        return self.__engineNo

    def setOwner(self, owner):
        self.__owner = owner
        self.__apiParas["owner"] = owner

    def getOwner(self):
        return self.__owner

    def setPlateNo(self, plateNo):
        self.__plateNo = plateNo
        self.__apiParas["plate_no"] = plateNo

    def getPlateNo(self):
        return self.__plateNo

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setRegisterDate(self, registerDate):
        self.__registerDate = registerDate
        self.__apiParas["register_date"] = registerDate

    def getRegisterDate(self):
        return self.__registerDate

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def setVehicleBrand(self, vehicleBrand):
        self.__vehicleBrand = vehicleBrand
        self.__apiParas["vehicle_brand"] = vehicleBrand

    def getVehicleBrand(self):
        return self.__vehicleBrand

    def setVehicleSeries(self, vehicleSeries):
        self.__vehicleSeries = vehicleSeries
        self.__apiParas["vehicle_series"] = vehicleSeries

    def getVehicleSeries(self):
        return self.__vehicleSeries

    def setVin(self, vin):
        self.__vin = vin
        self.__apiParas["vin"] = vin

    def getVin(self):
        return self.__vin

    def getApiMethodName(self):
        return "zhima.credit.vehicle.verify"

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
