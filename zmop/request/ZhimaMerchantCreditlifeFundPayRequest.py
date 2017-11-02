#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.creditlife.fund.pay request
:author: auto create
:date: 2017-08-04 10:26:31
'''


class ZhimaMerchantCreditlifeFundPayRequest:
    def __init__(self):
        self.__agreementNo = '' # 代扣协议号(代扣扣款时必须提供)
        self.__fundPayType = '' # 扣款类型(withholding_pay:代扣扣款,preauth_pay:预授权转支付)
        self.__goodsTitle = '' # 
        self.__goodsType = '' # 商品类型(0:虚拟物品,1:实物)
        self.__outOrderNo = '' # 商户订单号
        self.__payAmount = '' # 支付金额
        self.__preAuthNo = '' # 预授权号(付款方式为预授权转支付时必须提供)
        self.__roleId = '' # 芝麻用户id
        self.__sellerId = '' # 收款方支付宝id
        self.__transactionId = '' # 
        self.__userId = '' # 支付宝用户id（付款方id）

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAgreementNo(self, agreementNo):
        self.__agreementNo = agreementNo
        self.__apiParas["agreement_no"] = agreementNo

    def getAgreementNo(self):
        return self.__agreementNo

    def setFundPayType(self, fundPayType):
        self.__fundPayType = fundPayType
        self.__apiParas["fund_pay_type"] = fundPayType

    def getFundPayType(self):
        return self.__fundPayType

    def setGoodsTitle(self, goodsTitle):
        self.__goodsTitle = goodsTitle
        self.__apiParas["goods_title"] = goodsTitle

    def getGoodsTitle(self):
        return self.__goodsTitle

    def setGoodsType(self, goodsType):
        self.__goodsType = goodsType
        self.__apiParas["goods_type"] = goodsType

    def getGoodsType(self):
        return self.__goodsType

    def setOutOrderNo(self, outOrderNo):
        self.__outOrderNo = outOrderNo
        self.__apiParas["out_order_no"] = outOrderNo

    def getOutOrderNo(self):
        return self.__outOrderNo

    def setPayAmount(self, payAmount):
        self.__payAmount = payAmount
        self.__apiParas["pay_amount"] = payAmount

    def getPayAmount(self):
        return self.__payAmount

    def setPreAuthNo(self, preAuthNo):
        self.__preAuthNo = preAuthNo
        self.__apiParas["pre_auth_no"] = preAuthNo

    def getPreAuthNo(self):
        return self.__preAuthNo

    def setRoleId(self, roleId):
        self.__roleId = roleId
        self.__apiParas["role_id"] = roleId

    def getRoleId(self):
        return self.__roleId

    def setSellerId(self, sellerId):
        self.__sellerId = sellerId
        self.__apiParas["seller_id"] = sellerId

    def getSellerId(self):
        return self.__sellerId

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def setUserId(self, userId):
        self.__userId = userId
        self.__apiParas["user_id"] = userId

    def getUserId(self):
        return self.__userId

    def getApiMethodName(self):
        return "zhima.merchant.creditlife.fund.pay"

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
