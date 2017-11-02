#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.image.upload request
:author: auto create
:date: 2017-03-02 14:53:50
'''


class ZhimaMerchantImageUploadRequest:
    def __init__(self):
        self.__imageContent = '' # 图片的二进制内容,最大支持2M，需要对图片的二进制流做Base64处理转化成字符串
        self.__imageType = '' # 芝麻二级商户图标后缀：bmp, jpg, jpeg, png, gif

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setImageContent(self, imageContent):
        self.__imageContent = imageContent
        self.__apiParas["image_content"] = imageContent

    def getImageContent(self):
        return self.__imageContent

    def setImageType(self, imageType):
        self.__imageType = imageType
        self.__apiParas["image_type"] = imageType

    def getImageType(self):
        return self.__imageType

    def getApiMethodName(self):
        return "zhima.merchant.image.upload"

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
