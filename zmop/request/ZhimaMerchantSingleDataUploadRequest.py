#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.single.data.upload request
:author: auto create
:date: 2017-07-10 21:31:09
'''


class ZhimaMerchantSingleDataUploadRequest:
    def __init__(self):
        self.__bizExtParams = '' # 公用回传参数，这个字段由商户传入，系统透传给商户，便于商户做逻辑关联，请使用json格式。
        self.__data = '' # 传入的json数据，商户通过json格式将数据传给芝麻 ， json中的字段可以通过如下步骤获取：首先调用zhima.merchant.data.upload.initialize接口获取数据模板，该接口会返回一个数据模板文件的url地址，如：http://zmxymerchant-prod.oss-cn-shenzhen.zmxy.com.cn/openApi/openDoc/信用护航-负面记录和信用足迹商户数据模板V1.0.xlsx，该数据模板文件详细列出了需要传入的字段，及各字段的要求，data中的各字段就是该文件中列出的字段编码。
        self.__primaryKeys = '' # 主键列使用传入字段进行组合，也可以使用传入的某个单字段（确保主键稳定，而且可以很好的区分不同的数据）。例如order_no,pay_month或者order_no,bill_month组合，对于一个order_no只会有一条数据的情况，直接使用order_no作为主键列
        self.__sceneCode = '' # 场景码，每个场景码对应的数据模板不一样，请使用zhima.merchant.data.upload.initialize接口获取场景码对应的数据模板。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizExtParams(self, bizExtParams):
        self.__bizExtParams = bizExtParams
        self.__apiParas["biz_ext_params"] = bizExtParams

    def getBizExtParams(self):
        return self.__bizExtParams

    def setData(self, data):
        self.__data = data
        self.__apiParas["data"] = data

    def getData(self):
        return self.__data

    def setPrimaryKeys(self, primaryKeys):
        self.__primaryKeys = primaryKeys
        self.__apiParas["primary_keys"] = primaryKeys

    def getPrimaryKeys(self):
        return self.__primaryKeys

    def setSceneCode(self, sceneCode):
        self.__sceneCode = sceneCode
        self.__apiParas["scene_code"] = sceneCode

    def getSceneCode(self):
        return self.__sceneCode

    def getApiMethodName(self):
        return "zhima.merchant.single.data.upload"

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
