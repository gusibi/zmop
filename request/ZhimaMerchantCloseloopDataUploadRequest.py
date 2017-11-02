#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.closeloop.data.upload request
:author: auto create
:date: 2017-06-14 16:58:00
'''


class ZhimaMerchantCloseloopDataUploadRequest:
    def __init__(self):
        self.__bizExtParams = '' # 扩展参数
        self.__columns = '' # 单条数据的数据列，多个列以逗号隔开。
        self.__file = '' # 传入的json格式的文件，其中{"records":  是每个文件的固定开头。
        self.__fileCharset = '' # 是传入文件的数据编码，如果文件格式是UTF-8，则填写UTF-8，如果文件格式是GBK，则填写GBK
        self.__primaryKeyColumns = '' # 主键列使用反馈字段进行组合，也可以使用反馈的某个单字段（确保主键稳定，而且可以很好的区分不同的数据）。例如order_no,pay_month或者order_no,bill_month组合，对于一个order_no只会有一条数据的情况，直接使用order_no作为主键列
        self.__records = '' # 文件数据记录条数
        self.__sceneCode = '' # 场景码，用于标识上传的文件的用途，不同的场景码，file中的json格式不一样

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

    def setColumns(self, columns):
        self.__columns = columns
        self.__apiParas["columns"] = columns

    def getColumns(self):
        return self.__columns

    def setFile(self, file):
        self.__file = file
        self.__fileParas["file"] = file

    def getFile(self):
        return self.__file

    def setFileCharset(self, fileCharset):
        self.__fileCharset = fileCharset
        self.__apiParas["file_charset"] = fileCharset

    def getFileCharset(self):
        return self.__fileCharset

    def setPrimaryKeyColumns(self, primaryKeyColumns):
        self.__primaryKeyColumns = primaryKeyColumns
        self.__apiParas["primary_key_columns"] = primaryKeyColumns

    def getPrimaryKeyColumns(self):
        return self.__primaryKeyColumns

    def setRecords(self, records):
        self.__records = records
        self.__apiParas["records"] = records

    def getRecords(self):
        return self.__records

    def setSceneCode(self, sceneCode):
        self.__sceneCode = sceneCode
        self.__apiParas["scene_code"] = sceneCode

    def getSceneCode(self):
        return self.__sceneCode

    def getApiMethodName(self):
        return "zhima.merchant.closeloop.data.upload"

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
