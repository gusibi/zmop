#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.credit.msxf.onlinejdscore.query request
:author: auto create
:date: 2017-08-22 17:29:40
'''


class ZhimaCreditMsxfOnlinejdscoreQueryRequest:
    def __init__(self):
        self.__allFddifDivideSixaQdHourbinAmtaorder = '' # 特殊订单金额差异占比
        self.__allFddifMinusFiveaRangeHourbinAmtaorder = '' # 短时间下单金额的差异系数
        self.__allFddifMinusTwoaSdHourbinAmtaorder = '' # 特殊时间下单金额的波动指标
        self.__allFdescMeanPayonlinepaymentAmtorder = '' # 特定支付方式金额指标
        self.__allGddescMinusLoantimenowMaxDaydiff = '' # 用户购买时间波动系数1
        self.__allGddescMinusLoantimenowMinHourdiff = '' # 用户购买时间波动系数2
        self.__allGddifDivCashondeliveryallSumPayAmtorder = '' # 用户特殊支付金额占比
        self.__allGddifDivOnlinepaymentallSumPayAmtorder = '' # 用户特殊支付金额指标
        self.__allGddifDivSportsoutdoorallNCntprdcategory = '' # 用户特殊商品差异性指标
        self.__allGddifDivideFailallNStsCntorder = '' # 用户特殊订单占比
        self.__allGddifDivideFiveeightallNHourCntorder = '' # 用户特殊时间下单量指标
        self.__allGddifDividePhonedigitalallNCntprdcategory = '' # 用户特殊商品差异性系数
        self.__allGddifMinusCaMaxProductCntaorder = '' # 用户特殊订单量指标
        self.__allGddifMinusCaSumAorderCntproduct = '' # 用户特殊订单的差异性指标
        self.__allGddifMinusCsMedianProductCntaorder = '' # 用户特殊产品之间差异系数
        self.__allGddifMinusCsSkewAorderAmtaorder = '' # 用户特殊订单下单金额异常指标
        self.__allGddifMinusSaEntropyAorderCntproduct = '' # 用户购买商品的波动性指标
        self.__allGddifMinusSaSumAorderCntproduct = '' # 用户购买商品量
        self.__allGddifMinusSaSumProductCntaorder = '' # 用户购买固定商品的稳定性
        self.__allGdescMeanProductCntaorder = '' # 用户购买固定商品的差异
        self.__allGdescMeanSorderAmtaorder = '' # 用户购买特殊订单的数量
        self.__allGdescMinCorderAmtaorder = '' # 用户特殊订单金额指标
        self.__allGdescMinPhoneSumamt = '' # 用户下单稳定性系数
        self.__allGdescMinRecaddrcitySumamt = '' # 用户购买稳定性指标
        self.__allGdescMinRecaddrprovinceAvgamt = '' # 用户下单稳定性
        self.__allGdescNormentropyPhoneCntorder = '' # 用户购物行为稳定性指标
        self.__allGdescNormentropyProductCntsorder = '' # 用户特殊购买行为稳定性指标
        self.__allGdescQlSorderAmtaorder = '' # 用户特殊订单容量指标
        self.__allTsdescAmtorderdiffAmtdiffMedian = '' # 用户下单跨度行为指标
        self.__allTsdescAmtorderdiffAmtdiffQu = '' # 用户下单跨度行为稳定性
        self.__allTsdescAmtorderdiffAmtdiffSum = '' # 用户下单跨度行为波动性
        self.__allTsdescAmtorderdiffTimediffCv = '' # 用户下单跨度特殊差异性
        self.__allTsdescAmtorderdiffTimediffQfour = '' # 用户下单跨度可靠性
        self.__allTsdescAmtorderdiffTimediffQsix = '' # 用户下单金额差异稳定度
        self.__allTsdescAmtorderdiffTimediffQu = '' # 用户下单时间稳定度
        self.__allTsdescAmtorderdiffVamtQnine = '' # 用户下单行为差异度
        self.__jdauthFddescExistChannelfinanceAuth = '' # 用户可信度指标
        self.__jdauthFddescExistLoginnameEqualPhone = '' # 用户授信稳定性指标
        self.__jdauthFddescMinusNowauthtimeSeconds = '' # 用户信用欺诈指标
        self.__jdbankcardDescDivideNOwnernameReceiver = '' # 用户信用稳定性指标
        self.__jdbankcardDescNBankphoneAuthphone = '' # 用户可信度差异
        self.__jdbankcardDescNOwnernameReceiver = '' # 用户可信度波动系数
        self.__jdbankcardDiffDivideNndBindphone = '' # 用户稳定性支付系数
        self.__jdbankcardFdescNBanknameMajorfourbanks = '' # 用户主流支付差异
        self.__jdbankcardFdescNBanknameOthers = '' # 用户支付信用系数
        self.__jdbankcardFdiffDivideAbcallCntbankname = '' # 用户支付差异系数
        self.__jdbankcardFdiffDivideCreditallCntcardtype = '' # 用户信用卡稳定性
        self.__jdbankcardFdiffDividePostallCntbankname = '' # 用户支付稳定性
        self.__jdbtGddescExtractCreditscoreBt = '' # 用户信用指标
        self.__jdbtGddiffMinusOverdraftquotaBtAmt = '' # 用户信用稳定系数
        self.__jdoneoneoneonesumGdescAmt = '' # 用户活动金额指标
        self.__jdreceivaddrDescNAddress = '' # 用户居住稳定性指标
        self.__jdreceivaddrDescNNaemail = '' # 用户收货地址差异系数
        self.__jdreceivaddrDescRateNafixphone = '' # 用户收货地址稳定性指标
        self.__jdsixoneeightsumGdescAmt = '' # 用户活动金额范围系数
        self.__jduserFddescExistWebloginnameLogname = '' # 用户注册差异性指标
        self.__jduserFddescNdCompareThreenames = '' # 用户下单时间金额总共的时间精度
        self.__jduserIsbindBothqqwechat = '' # 用户的绑定粘性指标
        self.__oneyFddifDivideSevenaRangeHourbinAmtaorder = '' # 1年内短时间金额稳定性指标
        self.__oneyFddifMinusOneaRangeHourbinAmtaorder = '' # 1年内短时间金额占比
        self.__oneyFddifMinusSixaRangeHourbinAmtaorder = '' # 1年内短时间订单金额稳定性指标
        self.__oneyFdescMeanPaycashondeliveryAmtorder = '' # 1年内特殊订单金额平均水平
        self.__oneyFdescSumMeaninvoicecontentAmtorder = '' # 1年内特殊订单金额异常指标
        self.__oneyGddifDivOnlinepaymentallSumPayAmtorder = '' # 1年内在线支付金额占比
        self.__oneyGddifMinusCaMedianAorderAmtaorder = '' # 1年内特殊订单购买能力
        self.__oneyGddifMinusCaSdAmtbinAmtaorder = '' # 1年内取消订单订单金额差异性指标
        self.__oneyGddifMinusCaSumAorderCntproduct = '' # 1年内订单数量总和差异
        self.__oneyGddifMinusSaEntropyAmtbinAmtaorder = '' # 1年内特殊订单金额波动性指标
        self.__oneyGdescCvRecaddrcityAvgamt = '' # 1年内地址差异指标
        self.__oneyGdescNormentropyAmtbinAmtsorder = '' # 1年内特殊订单金额分段差异性指标
        self.__oneyTsdescAmtorderdiffTimediffQsix = '' # 1年内订单金额特殊时间差异性系数
        self.__oneyTsdescAmtorderdiffVamtRange = '' # 1年内下单时间金额波动指标
        self.__openId = '' # 芝麻会员在商户端的身份标识。
        self.__productCode = '' # 产品码
        self.__sixmFdescCvHourCntorder = '' # 6月内特殊时间下波动性指标
        self.__sixmGddifDivOnlinepaymentallSumPayAmtorder = '' # 6月内在线支付总金额的占比
        self.__sixmGddifDivPhonedigitalallNCntprdcategory = '' # 6月内电子产品类目占比
        self.__sixmGddifDivSixmallNHourtwefourteenCntorder = '' # 6月内特殊下单量的占比
        self.__sixmGddifDivideFiveeightallNHourCntorder = '' # 6月内短时间下单占比
        self.__sixmGddifMinusCaSumAorderCntproduct = '' # 6月内异常商品占比
        self.__sixmGdescMinRecaddrcityAvgamt = '' # 6月内收货地址平均下单量的差异性指标
        self.__sixmGdescRangeRecaddrprovinceAvgamt = '' # 6月内收货地址稳定性指标
        self.__springfestivalGdescQuAamt = '' # 用户活动期间的下单系数
        self.__threemFddifMinusSevenaQdHourbinAmtaorder = '' # 3个月内特殊时段购买能力
        self.__threemGddifDivTravelrechargeallNCntprdcateg = '' # 3月内特殊用途商品占比
        self.__threemGddifDivideFailallNStsCntorder = '' # 3月内异常订单占比
        self.__threemGddifDivideNullallSumPayAmtorder = '' # 3月内金额总和异常占比
        self.__threemGdescSumSorderAmtaorder = '' # 3月内特殊订单金额指标
        self.__transactionId = '' # 商户传入的业务流水号。此字段由商户生成，需确保唯一性，用于定位每一次请求，后续按此流水进行对帐。生成规则: 固定30位数字串，前17位为精确到毫秒的时间yyyyMMddhhmmssSSS，后13位为自增数字。

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setAllFddifDivideSixaQdHourbinAmtaorder(self, allFddifDivideSixaQdHourbinAmtaorder):
        self.__allFddifDivideSixaQdHourbinAmtaorder = allFddifDivideSixaQdHourbinAmtaorder
        self.__apiParas["all_fddif_divide_sixa_qd_hourbin_amtaorder"] = allFddifDivideSixaQdHourbinAmtaorder

    def getAllFddifDivideSixaQdHourbinAmtaorder(self):
        return self.__allFddifDivideSixaQdHourbinAmtaorder

    def setAllFddifMinusFiveaRangeHourbinAmtaorder(self, allFddifMinusFiveaRangeHourbinAmtaorder):
        self.__allFddifMinusFiveaRangeHourbinAmtaorder = allFddifMinusFiveaRangeHourbinAmtaorder
        self.__apiParas["all_fddif_minus_fivea_range_hourbin_amtaorder"] = allFddifMinusFiveaRangeHourbinAmtaorder

    def getAllFddifMinusFiveaRangeHourbinAmtaorder(self):
        return self.__allFddifMinusFiveaRangeHourbinAmtaorder

    def setAllFddifMinusTwoaSdHourbinAmtaorder(self, allFddifMinusTwoaSdHourbinAmtaorder):
        self.__allFddifMinusTwoaSdHourbinAmtaorder = allFddifMinusTwoaSdHourbinAmtaorder
        self.__apiParas["all_fddif_minus_twoa_sd_hourbin_amtaorder"] = allFddifMinusTwoaSdHourbinAmtaorder

    def getAllFddifMinusTwoaSdHourbinAmtaorder(self):
        return self.__allFddifMinusTwoaSdHourbinAmtaorder

    def setAllFdescMeanPayonlinepaymentAmtorder(self, allFdescMeanPayonlinepaymentAmtorder):
        self.__allFdescMeanPayonlinepaymentAmtorder = allFdescMeanPayonlinepaymentAmtorder
        self.__apiParas["all_fdesc_mean_payonlinepayment_amtorder"] = allFdescMeanPayonlinepaymentAmtorder

    def getAllFdescMeanPayonlinepaymentAmtorder(self):
        return self.__allFdescMeanPayonlinepaymentAmtorder

    def setAllGddescMinusLoantimenowMaxDaydiff(self, allGddescMinusLoantimenowMaxDaydiff):
        self.__allGddescMinusLoantimenowMaxDaydiff = allGddescMinusLoantimenowMaxDaydiff
        self.__apiParas["all_gddesc_minus_loantimenow_max_daydiff"] = allGddescMinusLoantimenowMaxDaydiff

    def getAllGddescMinusLoantimenowMaxDaydiff(self):
        return self.__allGddescMinusLoantimenowMaxDaydiff

    def setAllGddescMinusLoantimenowMinHourdiff(self, allGddescMinusLoantimenowMinHourdiff):
        self.__allGddescMinusLoantimenowMinHourdiff = allGddescMinusLoantimenowMinHourdiff
        self.__apiParas["all_gddesc_minus_loantimenow_min_hourdiff"] = allGddescMinusLoantimenowMinHourdiff

    def getAllGddescMinusLoantimenowMinHourdiff(self):
        return self.__allGddescMinusLoantimenowMinHourdiff

    def setAllGddifDivCashondeliveryallSumPayAmtorder(self, allGddifDivCashondeliveryallSumPayAmtorder):
        self.__allGddifDivCashondeliveryallSumPayAmtorder = allGddifDivCashondeliveryallSumPayAmtorder
        self.__apiParas["all_gddif_div_cashondeliveryall_sum_pay_amtorder"] = allGddifDivCashondeliveryallSumPayAmtorder

    def getAllGddifDivCashondeliveryallSumPayAmtorder(self):
        return self.__allGddifDivCashondeliveryallSumPayAmtorder

    def setAllGddifDivOnlinepaymentallSumPayAmtorder(self, allGddifDivOnlinepaymentallSumPayAmtorder):
        self.__allGddifDivOnlinepaymentallSumPayAmtorder = allGddifDivOnlinepaymentallSumPayAmtorder
        self.__apiParas["all_gddif_div_onlinepaymentall_sum_pay_amtorder"] = allGddifDivOnlinepaymentallSumPayAmtorder

    def getAllGddifDivOnlinepaymentallSumPayAmtorder(self):
        return self.__allGddifDivOnlinepaymentallSumPayAmtorder

    def setAllGddifDivSportsoutdoorallNCntprdcategory(self, allGddifDivSportsoutdoorallNCntprdcategory):
        self.__allGddifDivSportsoutdoorallNCntprdcategory = allGddifDivSportsoutdoorallNCntprdcategory
        self.__apiParas["all_gddif_div_sportsoutdoorall_n_cntprdcategory"] = allGddifDivSportsoutdoorallNCntprdcategory

    def getAllGddifDivSportsoutdoorallNCntprdcategory(self):
        return self.__allGddifDivSportsoutdoorallNCntprdcategory

    def setAllGddifDivideFailallNStsCntorder(self, allGddifDivideFailallNStsCntorder):
        self.__allGddifDivideFailallNStsCntorder = allGddifDivideFailallNStsCntorder
        self.__apiParas["all_gddif_divide_failall_n_sts_cntorder"] = allGddifDivideFailallNStsCntorder

    def getAllGddifDivideFailallNStsCntorder(self):
        return self.__allGddifDivideFailallNStsCntorder

    def setAllGddifDivideFiveeightallNHourCntorder(self, allGddifDivideFiveeightallNHourCntorder):
        self.__allGddifDivideFiveeightallNHourCntorder = allGddifDivideFiveeightallNHourCntorder
        self.__apiParas["all_gddif_divide_fiveeightall_n_hour_cntorder"] = allGddifDivideFiveeightallNHourCntorder

    def getAllGddifDivideFiveeightallNHourCntorder(self):
        return self.__allGddifDivideFiveeightallNHourCntorder

    def setAllGddifDividePhonedigitalallNCntprdcategory(self, allGddifDividePhonedigitalallNCntprdcategory):
        self.__allGddifDividePhonedigitalallNCntprdcategory = allGddifDividePhonedigitalallNCntprdcategory
        self.__apiParas["all_gddif_divide_phonedigitalall_n_cntprdcategory"] = allGddifDividePhonedigitalallNCntprdcategory

    def getAllGddifDividePhonedigitalallNCntprdcategory(self):
        return self.__allGddifDividePhonedigitalallNCntprdcategory

    def setAllGddifMinusCaMaxProductCntaorder(self, allGddifMinusCaMaxProductCntaorder):
        self.__allGddifMinusCaMaxProductCntaorder = allGddifMinusCaMaxProductCntaorder
        self.__apiParas["all_gddif_minus_ca_max_product_cntaorder"] = allGddifMinusCaMaxProductCntaorder

    def getAllGddifMinusCaMaxProductCntaorder(self):
        return self.__allGddifMinusCaMaxProductCntaorder

    def setAllGddifMinusCaSumAorderCntproduct(self, allGddifMinusCaSumAorderCntproduct):
        self.__allGddifMinusCaSumAorderCntproduct = allGddifMinusCaSumAorderCntproduct
        self.__apiParas["all_gddif_minus_ca_sum_aorder_cntproduct"] = allGddifMinusCaSumAorderCntproduct

    def getAllGddifMinusCaSumAorderCntproduct(self):
        return self.__allGddifMinusCaSumAorderCntproduct

    def setAllGddifMinusCsMedianProductCntaorder(self, allGddifMinusCsMedianProductCntaorder):
        self.__allGddifMinusCsMedianProductCntaorder = allGddifMinusCsMedianProductCntaorder
        self.__apiParas["all_gddif_minus_cs_median_product_cntaorder"] = allGddifMinusCsMedianProductCntaorder

    def getAllGddifMinusCsMedianProductCntaorder(self):
        return self.__allGddifMinusCsMedianProductCntaorder

    def setAllGddifMinusCsSkewAorderAmtaorder(self, allGddifMinusCsSkewAorderAmtaorder):
        self.__allGddifMinusCsSkewAorderAmtaorder = allGddifMinusCsSkewAorderAmtaorder
        self.__apiParas["all_gddif_minus_cs_skew_aorder_amtaorder"] = allGddifMinusCsSkewAorderAmtaorder

    def getAllGddifMinusCsSkewAorderAmtaorder(self):
        return self.__allGddifMinusCsSkewAorderAmtaorder

    def setAllGddifMinusSaEntropyAorderCntproduct(self, allGddifMinusSaEntropyAorderCntproduct):
        self.__allGddifMinusSaEntropyAorderCntproduct = allGddifMinusSaEntropyAorderCntproduct
        self.__apiParas["all_gddif_minus_sa_entropy_aorder_cntproduct"] = allGddifMinusSaEntropyAorderCntproduct

    def getAllGddifMinusSaEntropyAorderCntproduct(self):
        return self.__allGddifMinusSaEntropyAorderCntproduct

    def setAllGddifMinusSaSumAorderCntproduct(self, allGddifMinusSaSumAorderCntproduct):
        self.__allGddifMinusSaSumAorderCntproduct = allGddifMinusSaSumAorderCntproduct
        self.__apiParas["all_gddif_minus_sa_sum_aorder_cntproduct"] = allGddifMinusSaSumAorderCntproduct

    def getAllGddifMinusSaSumAorderCntproduct(self):
        return self.__allGddifMinusSaSumAorderCntproduct

    def setAllGddifMinusSaSumProductCntaorder(self, allGddifMinusSaSumProductCntaorder):
        self.__allGddifMinusSaSumProductCntaorder = allGddifMinusSaSumProductCntaorder
        self.__apiParas["all_gddif_minus_sa_sum_product_cntaorder"] = allGddifMinusSaSumProductCntaorder

    def getAllGddifMinusSaSumProductCntaorder(self):
        return self.__allGddifMinusSaSumProductCntaorder

    def setAllGdescMeanProductCntaorder(self, allGdescMeanProductCntaorder):
        self.__allGdescMeanProductCntaorder = allGdescMeanProductCntaorder
        self.__apiParas["all_gdesc_mean_product_cntaorder"] = allGdescMeanProductCntaorder

    def getAllGdescMeanProductCntaorder(self):
        return self.__allGdescMeanProductCntaorder

    def setAllGdescMeanSorderAmtaorder(self, allGdescMeanSorderAmtaorder):
        self.__allGdescMeanSorderAmtaorder = allGdescMeanSorderAmtaorder
        self.__apiParas["all_gdesc_mean_sorder_amtaorder"] = allGdescMeanSorderAmtaorder

    def getAllGdescMeanSorderAmtaorder(self):
        return self.__allGdescMeanSorderAmtaorder

    def setAllGdescMinCorderAmtaorder(self, allGdescMinCorderAmtaorder):
        self.__allGdescMinCorderAmtaorder = allGdescMinCorderAmtaorder
        self.__apiParas["all_gdesc_min_corder_amtaorder"] = allGdescMinCorderAmtaorder

    def getAllGdescMinCorderAmtaorder(self):
        return self.__allGdescMinCorderAmtaorder

    def setAllGdescMinPhoneSumamt(self, allGdescMinPhoneSumamt):
        self.__allGdescMinPhoneSumamt = allGdescMinPhoneSumamt
        self.__apiParas["all_gdesc_min_phone_sumamt"] = allGdescMinPhoneSumamt

    def getAllGdescMinPhoneSumamt(self):
        return self.__allGdescMinPhoneSumamt

    def setAllGdescMinRecaddrcitySumamt(self, allGdescMinRecaddrcitySumamt):
        self.__allGdescMinRecaddrcitySumamt = allGdescMinRecaddrcitySumamt
        self.__apiParas["all_gdesc_min_recaddrcity_sumamt"] = allGdescMinRecaddrcitySumamt

    def getAllGdescMinRecaddrcitySumamt(self):
        return self.__allGdescMinRecaddrcitySumamt

    def setAllGdescMinRecaddrprovinceAvgamt(self, allGdescMinRecaddrprovinceAvgamt):
        self.__allGdescMinRecaddrprovinceAvgamt = allGdescMinRecaddrprovinceAvgamt
        self.__apiParas["all_gdesc_min_recaddrprovince_avgamt"] = allGdescMinRecaddrprovinceAvgamt

    def getAllGdescMinRecaddrprovinceAvgamt(self):
        return self.__allGdescMinRecaddrprovinceAvgamt

    def setAllGdescNormentropyPhoneCntorder(self, allGdescNormentropyPhoneCntorder):
        self.__allGdescNormentropyPhoneCntorder = allGdescNormentropyPhoneCntorder
        self.__apiParas["all_gdesc_normentropy_phone_cntorder"] = allGdescNormentropyPhoneCntorder

    def getAllGdescNormentropyPhoneCntorder(self):
        return self.__allGdescNormentropyPhoneCntorder

    def setAllGdescNormentropyProductCntsorder(self, allGdescNormentropyProductCntsorder):
        self.__allGdescNormentropyProductCntsorder = allGdescNormentropyProductCntsorder
        self.__apiParas["all_gdesc_normentropy_product_cntsorder"] = allGdescNormentropyProductCntsorder

    def getAllGdescNormentropyProductCntsorder(self):
        return self.__allGdescNormentropyProductCntsorder

    def setAllGdescQlSorderAmtaorder(self, allGdescQlSorderAmtaorder):
        self.__allGdescQlSorderAmtaorder = allGdescQlSorderAmtaorder
        self.__apiParas["all_gdesc_ql_sorder_amtaorder"] = allGdescQlSorderAmtaorder

    def getAllGdescQlSorderAmtaorder(self):
        return self.__allGdescQlSorderAmtaorder

    def setAllTsdescAmtorderdiffAmtdiffMedian(self, allTsdescAmtorderdiffAmtdiffMedian):
        self.__allTsdescAmtorderdiffAmtdiffMedian = allTsdescAmtorderdiffAmtdiffMedian
        self.__apiParas["all_tsdesc_amtorderdiff_amtdiff_median"] = allTsdescAmtorderdiffAmtdiffMedian

    def getAllTsdescAmtorderdiffAmtdiffMedian(self):
        return self.__allTsdescAmtorderdiffAmtdiffMedian

    def setAllTsdescAmtorderdiffAmtdiffQu(self, allTsdescAmtorderdiffAmtdiffQu):
        self.__allTsdescAmtorderdiffAmtdiffQu = allTsdescAmtorderdiffAmtdiffQu
        self.__apiParas["all_tsdesc_amtorderdiff_amtdiff_qu"] = allTsdescAmtorderdiffAmtdiffQu

    def getAllTsdescAmtorderdiffAmtdiffQu(self):
        return self.__allTsdescAmtorderdiffAmtdiffQu

    def setAllTsdescAmtorderdiffAmtdiffSum(self, allTsdescAmtorderdiffAmtdiffSum):
        self.__allTsdescAmtorderdiffAmtdiffSum = allTsdescAmtorderdiffAmtdiffSum
        self.__apiParas["all_tsdesc_amtorderdiff_amtdiff_sum"] = allTsdescAmtorderdiffAmtdiffSum

    def getAllTsdescAmtorderdiffAmtdiffSum(self):
        return self.__allTsdescAmtorderdiffAmtdiffSum

    def setAllTsdescAmtorderdiffTimediffCv(self, allTsdescAmtorderdiffTimediffCv):
        self.__allTsdescAmtorderdiffTimediffCv = allTsdescAmtorderdiffTimediffCv
        self.__apiParas["all_tsdesc_amtorderdiff_timediff_cv"] = allTsdescAmtorderdiffTimediffCv

    def getAllTsdescAmtorderdiffTimediffCv(self):
        return self.__allTsdescAmtorderdiffTimediffCv

    def setAllTsdescAmtorderdiffTimediffQfour(self, allTsdescAmtorderdiffTimediffQfour):
        self.__allTsdescAmtorderdiffTimediffQfour = allTsdescAmtorderdiffTimediffQfour
        self.__apiParas["all_tsdesc_amtorderdiff_timediff_qfour"] = allTsdescAmtorderdiffTimediffQfour

    def getAllTsdescAmtorderdiffTimediffQfour(self):
        return self.__allTsdescAmtorderdiffTimediffQfour

    def setAllTsdescAmtorderdiffTimediffQsix(self, allTsdescAmtorderdiffTimediffQsix):
        self.__allTsdescAmtorderdiffTimediffQsix = allTsdescAmtorderdiffTimediffQsix
        self.__apiParas["all_tsdesc_amtorderdiff_timediff_qsix"] = allTsdescAmtorderdiffTimediffQsix

    def getAllTsdescAmtorderdiffTimediffQsix(self):
        return self.__allTsdescAmtorderdiffTimediffQsix

    def setAllTsdescAmtorderdiffTimediffQu(self, allTsdescAmtorderdiffTimediffQu):
        self.__allTsdescAmtorderdiffTimediffQu = allTsdescAmtorderdiffTimediffQu
        self.__apiParas["all_tsdesc_amtorderdiff_timediff_qu"] = allTsdescAmtorderdiffTimediffQu

    def getAllTsdescAmtorderdiffTimediffQu(self):
        return self.__allTsdescAmtorderdiffTimediffQu

    def setAllTsdescAmtorderdiffVamtQnine(self, allTsdescAmtorderdiffVamtQnine):
        self.__allTsdescAmtorderdiffVamtQnine = allTsdescAmtorderdiffVamtQnine
        self.__apiParas["all_tsdesc_amtorderdiff_vamt_qnine"] = allTsdescAmtorderdiffVamtQnine

    def getAllTsdescAmtorderdiffVamtQnine(self):
        return self.__allTsdescAmtorderdiffVamtQnine

    def setJdauthFddescExistChannelfinanceAuth(self, jdauthFddescExistChannelfinanceAuth):
        self.__jdauthFddescExistChannelfinanceAuth = jdauthFddescExistChannelfinanceAuth
        self.__apiParas["jdauth_fddesc_exist_channelfinance_auth"] = jdauthFddescExistChannelfinanceAuth

    def getJdauthFddescExistChannelfinanceAuth(self):
        return self.__jdauthFddescExistChannelfinanceAuth

    def setJdauthFddescExistLoginnameEqualPhone(self, jdauthFddescExistLoginnameEqualPhone):
        self.__jdauthFddescExistLoginnameEqualPhone = jdauthFddescExistLoginnameEqualPhone
        self.__apiParas["jdauth_fddesc_exist_loginname_equal_phone"] = jdauthFddescExistLoginnameEqualPhone

    def getJdauthFddescExistLoginnameEqualPhone(self):
        return self.__jdauthFddescExistLoginnameEqualPhone

    def setJdauthFddescMinusNowauthtimeSeconds(self, jdauthFddescMinusNowauthtimeSeconds):
        self.__jdauthFddescMinusNowauthtimeSeconds = jdauthFddescMinusNowauthtimeSeconds
        self.__apiParas["jdauth_fddesc_minus_nowauthtime_seconds"] = jdauthFddescMinusNowauthtimeSeconds

    def getJdauthFddescMinusNowauthtimeSeconds(self):
        return self.__jdauthFddescMinusNowauthtimeSeconds

    def setJdbankcardDescDivideNOwnernameReceiver(self, jdbankcardDescDivideNOwnernameReceiver):
        self.__jdbankcardDescDivideNOwnernameReceiver = jdbankcardDescDivideNOwnernameReceiver
        self.__apiParas["jdbankcard_desc_divide_n_ownername_receiver"] = jdbankcardDescDivideNOwnernameReceiver

    def getJdbankcardDescDivideNOwnernameReceiver(self):
        return self.__jdbankcardDescDivideNOwnernameReceiver

    def setJdbankcardDescNBankphoneAuthphone(self, jdbankcardDescNBankphoneAuthphone):
        self.__jdbankcardDescNBankphoneAuthphone = jdbankcardDescNBankphoneAuthphone
        self.__apiParas["jdbankcard_desc_n_bankphone_authphone"] = jdbankcardDescNBankphoneAuthphone

    def getJdbankcardDescNBankphoneAuthphone(self):
        return self.__jdbankcardDescNBankphoneAuthphone

    def setJdbankcardDescNOwnernameReceiver(self, jdbankcardDescNOwnernameReceiver):
        self.__jdbankcardDescNOwnernameReceiver = jdbankcardDescNOwnernameReceiver
        self.__apiParas["jdbankcard_desc_n_ownername_receiver"] = jdbankcardDescNOwnernameReceiver

    def getJdbankcardDescNOwnernameReceiver(self):
        return self.__jdbankcardDescNOwnernameReceiver

    def setJdbankcardDiffDivideNndBindphone(self, jdbankcardDiffDivideNndBindphone):
        self.__jdbankcardDiffDivideNndBindphone = jdbankcardDiffDivideNndBindphone
        self.__apiParas["jdbankcard_diff_divide_nnd_bindphone"] = jdbankcardDiffDivideNndBindphone

    def getJdbankcardDiffDivideNndBindphone(self):
        return self.__jdbankcardDiffDivideNndBindphone

    def setJdbankcardFdescNBanknameMajorfourbanks(self, jdbankcardFdescNBanknameMajorfourbanks):
        self.__jdbankcardFdescNBanknameMajorfourbanks = jdbankcardFdescNBanknameMajorfourbanks
        self.__apiParas["jdbankcard_fdesc_n_bankname_majorfourbanks"] = jdbankcardFdescNBanknameMajorfourbanks

    def getJdbankcardFdescNBanknameMajorfourbanks(self):
        return self.__jdbankcardFdescNBanknameMajorfourbanks

    def setJdbankcardFdescNBanknameOthers(self, jdbankcardFdescNBanknameOthers):
        self.__jdbankcardFdescNBanknameOthers = jdbankcardFdescNBanknameOthers
        self.__apiParas["jdbankcard_fdesc_n_bankname_others"] = jdbankcardFdescNBanknameOthers

    def getJdbankcardFdescNBanknameOthers(self):
        return self.__jdbankcardFdescNBanknameOthers

    def setJdbankcardFdiffDivideAbcallCntbankname(self, jdbankcardFdiffDivideAbcallCntbankname):
        self.__jdbankcardFdiffDivideAbcallCntbankname = jdbankcardFdiffDivideAbcallCntbankname
        self.__apiParas["jdbankcard_fdiff_divide_abcall_cntbankname"] = jdbankcardFdiffDivideAbcallCntbankname

    def getJdbankcardFdiffDivideAbcallCntbankname(self):
        return self.__jdbankcardFdiffDivideAbcallCntbankname

    def setJdbankcardFdiffDivideCreditallCntcardtype(self, jdbankcardFdiffDivideCreditallCntcardtype):
        self.__jdbankcardFdiffDivideCreditallCntcardtype = jdbankcardFdiffDivideCreditallCntcardtype
        self.__apiParas["jdbankcard_fdiff_divide_creditall_cntcardtype"] = jdbankcardFdiffDivideCreditallCntcardtype

    def getJdbankcardFdiffDivideCreditallCntcardtype(self):
        return self.__jdbankcardFdiffDivideCreditallCntcardtype

    def setJdbankcardFdiffDividePostallCntbankname(self, jdbankcardFdiffDividePostallCntbankname):
        self.__jdbankcardFdiffDividePostallCntbankname = jdbankcardFdiffDividePostallCntbankname
        self.__apiParas["jdbankcard_fdiff_divide_postall_cntbankname"] = jdbankcardFdiffDividePostallCntbankname

    def getJdbankcardFdiffDividePostallCntbankname(self):
        return self.__jdbankcardFdiffDividePostallCntbankname

    def setJdbtGddescExtractCreditscoreBt(self, jdbtGddescExtractCreditscoreBt):
        self.__jdbtGddescExtractCreditscoreBt = jdbtGddescExtractCreditscoreBt
        self.__apiParas["jdbt_gddesc_extract_creditscore_bt"] = jdbtGddescExtractCreditscoreBt

    def getJdbtGddescExtractCreditscoreBt(self):
        return self.__jdbtGddescExtractCreditscoreBt

    def setJdbtGddiffMinusOverdraftquotaBtAmt(self, jdbtGddiffMinusOverdraftquotaBtAmt):
        self.__jdbtGddiffMinusOverdraftquotaBtAmt = jdbtGddiffMinusOverdraftquotaBtAmt
        self.__apiParas["jdbt_gddiff_minus_overdraftquota_bt_amt"] = jdbtGddiffMinusOverdraftquotaBtAmt

    def getJdbtGddiffMinusOverdraftquotaBtAmt(self):
        return self.__jdbtGddiffMinusOverdraftquotaBtAmt

    def setJdoneoneoneonesumGdescAmt(self, jdoneoneoneonesumGdescAmt):
        self.__jdoneoneoneonesumGdescAmt = jdoneoneoneonesumGdescAmt
        self.__apiParas["jdoneoneoneonesum_gdesc_amt"] = jdoneoneoneonesumGdescAmt

    def getJdoneoneoneonesumGdescAmt(self):
        return self.__jdoneoneoneonesumGdescAmt

    def setJdreceivaddrDescNAddress(self, jdreceivaddrDescNAddress):
        self.__jdreceivaddrDescNAddress = jdreceivaddrDescNAddress
        self.__apiParas["jdreceivaddr_desc_n_address"] = jdreceivaddrDescNAddress

    def getJdreceivaddrDescNAddress(self):
        return self.__jdreceivaddrDescNAddress

    def setJdreceivaddrDescNNaemail(self, jdreceivaddrDescNNaemail):
        self.__jdreceivaddrDescNNaemail = jdreceivaddrDescNNaemail
        self.__apiParas["jdreceivaddr_desc_n_naemail"] = jdreceivaddrDescNNaemail

    def getJdreceivaddrDescNNaemail(self):
        return self.__jdreceivaddrDescNNaemail

    def setJdreceivaddrDescRateNafixphone(self, jdreceivaddrDescRateNafixphone):
        self.__jdreceivaddrDescRateNafixphone = jdreceivaddrDescRateNafixphone
        self.__apiParas["jdreceivaddr_desc_rate_nafixphone"] = jdreceivaddrDescRateNafixphone

    def getJdreceivaddrDescRateNafixphone(self):
        return self.__jdreceivaddrDescRateNafixphone

    def setJdsixoneeightsumGdescAmt(self, jdsixoneeightsumGdescAmt):
        self.__jdsixoneeightsumGdescAmt = jdsixoneeightsumGdescAmt
        self.__apiParas["jdsixoneeightsum_gdesc_amt"] = jdsixoneeightsumGdescAmt

    def getJdsixoneeightsumGdescAmt(self):
        return self.__jdsixoneeightsumGdescAmt

    def setJduserFddescExistWebloginnameLogname(self, jduserFddescExistWebloginnameLogname):
        self.__jduserFddescExistWebloginnameLogname = jduserFddescExistWebloginnameLogname
        self.__apiParas["jduser_fddesc_exist_webloginname_logname"] = jduserFddescExistWebloginnameLogname

    def getJduserFddescExistWebloginnameLogname(self):
        return self.__jduserFddescExistWebloginnameLogname

    def setJduserFddescNdCompareThreenames(self, jduserFddescNdCompareThreenames):
        self.__jduserFddescNdCompareThreenames = jduserFddescNdCompareThreenames
        self.__apiParas["jduser_fddesc_nd_compare_threenames"] = jduserFddescNdCompareThreenames

    def getJduserFddescNdCompareThreenames(self):
        return self.__jduserFddescNdCompareThreenames

    def setJduserIsbindBothqqwechat(self, jduserIsbindBothqqwechat):
        self.__jduserIsbindBothqqwechat = jduserIsbindBothqqwechat
        self.__apiParas["jduser_isbind_bothqqwechat"] = jduserIsbindBothqqwechat

    def getJduserIsbindBothqqwechat(self):
        return self.__jduserIsbindBothqqwechat

    def setOneyFddifDivideSevenaRangeHourbinAmtaorder(self, oneyFddifDivideSevenaRangeHourbinAmtaorder):
        self.__oneyFddifDivideSevenaRangeHourbinAmtaorder = oneyFddifDivideSevenaRangeHourbinAmtaorder
        self.__apiParas["oney_fddif_divide_sevena_range_hourbin_amtaorder"] = oneyFddifDivideSevenaRangeHourbinAmtaorder

    def getOneyFddifDivideSevenaRangeHourbinAmtaorder(self):
        return self.__oneyFddifDivideSevenaRangeHourbinAmtaorder

    def setOneyFddifMinusOneaRangeHourbinAmtaorder(self, oneyFddifMinusOneaRangeHourbinAmtaorder):
        self.__oneyFddifMinusOneaRangeHourbinAmtaorder = oneyFddifMinusOneaRangeHourbinAmtaorder
        self.__apiParas["oney_fddif_minus_onea_range_hourbin_amtaorder"] = oneyFddifMinusOneaRangeHourbinAmtaorder

    def getOneyFddifMinusOneaRangeHourbinAmtaorder(self):
        return self.__oneyFddifMinusOneaRangeHourbinAmtaorder

    def setOneyFddifMinusSixaRangeHourbinAmtaorder(self, oneyFddifMinusSixaRangeHourbinAmtaorder):
        self.__oneyFddifMinusSixaRangeHourbinAmtaorder = oneyFddifMinusSixaRangeHourbinAmtaorder
        self.__apiParas["oney_fddif_minus_sixa_range_hourbin_amtaorder"] = oneyFddifMinusSixaRangeHourbinAmtaorder

    def getOneyFddifMinusSixaRangeHourbinAmtaorder(self):
        return self.__oneyFddifMinusSixaRangeHourbinAmtaorder

    def setOneyFdescMeanPaycashondeliveryAmtorder(self, oneyFdescMeanPaycashondeliveryAmtorder):
        self.__oneyFdescMeanPaycashondeliveryAmtorder = oneyFdescMeanPaycashondeliveryAmtorder
        self.__apiParas["oney_fdesc_mean_paycashondelivery_amtorder"] = oneyFdescMeanPaycashondeliveryAmtorder

    def getOneyFdescMeanPaycashondeliveryAmtorder(self):
        return self.__oneyFdescMeanPaycashondeliveryAmtorder

    def setOneyFdescSumMeaninvoicecontentAmtorder(self, oneyFdescSumMeaninvoicecontentAmtorder):
        self.__oneyFdescSumMeaninvoicecontentAmtorder = oneyFdescSumMeaninvoicecontentAmtorder
        self.__apiParas["oney_fdesc_sum_meaninvoicecontent_amtorder"] = oneyFdescSumMeaninvoicecontentAmtorder

    def getOneyFdescSumMeaninvoicecontentAmtorder(self):
        return self.__oneyFdescSumMeaninvoicecontentAmtorder

    def setOneyGddifDivOnlinepaymentallSumPayAmtorder(self, oneyGddifDivOnlinepaymentallSumPayAmtorder):
        self.__oneyGddifDivOnlinepaymentallSumPayAmtorder = oneyGddifDivOnlinepaymentallSumPayAmtorder
        self.__apiParas["oney_gddif_div_onlinepaymentall_sum_pay_amtorder"] = oneyGddifDivOnlinepaymentallSumPayAmtorder

    def getOneyGddifDivOnlinepaymentallSumPayAmtorder(self):
        return self.__oneyGddifDivOnlinepaymentallSumPayAmtorder

    def setOneyGddifMinusCaMedianAorderAmtaorder(self, oneyGddifMinusCaMedianAorderAmtaorder):
        self.__oneyGddifMinusCaMedianAorderAmtaorder = oneyGddifMinusCaMedianAorderAmtaorder
        self.__apiParas["oney_gddif_minus_ca_median_aorder_amtaorder"] = oneyGddifMinusCaMedianAorderAmtaorder

    def getOneyGddifMinusCaMedianAorderAmtaorder(self):
        return self.__oneyGddifMinusCaMedianAorderAmtaorder

    def setOneyGddifMinusCaSdAmtbinAmtaorder(self, oneyGddifMinusCaSdAmtbinAmtaorder):
        self.__oneyGddifMinusCaSdAmtbinAmtaorder = oneyGddifMinusCaSdAmtbinAmtaorder
        self.__apiParas["oney_gddif_minus_ca_sd_amtbin_amtaorder"] = oneyGddifMinusCaSdAmtbinAmtaorder

    def getOneyGddifMinusCaSdAmtbinAmtaorder(self):
        return self.__oneyGddifMinusCaSdAmtbinAmtaorder

    def setOneyGddifMinusCaSumAorderCntproduct(self, oneyGddifMinusCaSumAorderCntproduct):
        self.__oneyGddifMinusCaSumAorderCntproduct = oneyGddifMinusCaSumAorderCntproduct
        self.__apiParas["oney_gddif_minus_ca_sum_aorder_cntproduct"] = oneyGddifMinusCaSumAorderCntproduct

    def getOneyGddifMinusCaSumAorderCntproduct(self):
        return self.__oneyGddifMinusCaSumAorderCntproduct

    def setOneyGddifMinusSaEntropyAmtbinAmtaorder(self, oneyGddifMinusSaEntropyAmtbinAmtaorder):
        self.__oneyGddifMinusSaEntropyAmtbinAmtaorder = oneyGddifMinusSaEntropyAmtbinAmtaorder
        self.__apiParas["oney_gddif_minus_sa_entropy_amtbin_amtaorder"] = oneyGddifMinusSaEntropyAmtbinAmtaorder

    def getOneyGddifMinusSaEntropyAmtbinAmtaorder(self):
        return self.__oneyGddifMinusSaEntropyAmtbinAmtaorder

    def setOneyGdescCvRecaddrcityAvgamt(self, oneyGdescCvRecaddrcityAvgamt):
        self.__oneyGdescCvRecaddrcityAvgamt = oneyGdescCvRecaddrcityAvgamt
        self.__apiParas["oney_gdesc_cv_recaddrcity_avgamt"] = oneyGdescCvRecaddrcityAvgamt

    def getOneyGdescCvRecaddrcityAvgamt(self):
        return self.__oneyGdescCvRecaddrcityAvgamt

    def setOneyGdescNormentropyAmtbinAmtsorder(self, oneyGdescNormentropyAmtbinAmtsorder):
        self.__oneyGdescNormentropyAmtbinAmtsorder = oneyGdescNormentropyAmtbinAmtsorder
        self.__apiParas["oney_gdesc_normentropy_amtbin_amtsorder"] = oneyGdescNormentropyAmtbinAmtsorder

    def getOneyGdescNormentropyAmtbinAmtsorder(self):
        return self.__oneyGdescNormentropyAmtbinAmtsorder

    def setOneyTsdescAmtorderdiffTimediffQsix(self, oneyTsdescAmtorderdiffTimediffQsix):
        self.__oneyTsdescAmtorderdiffTimediffQsix = oneyTsdescAmtorderdiffTimediffQsix
        self.__apiParas["oney_tsdesc_amtorderdiff_timediff_qsix"] = oneyTsdescAmtorderdiffTimediffQsix

    def getOneyTsdescAmtorderdiffTimediffQsix(self):
        return self.__oneyTsdescAmtorderdiffTimediffQsix

    def setOneyTsdescAmtorderdiffVamtRange(self, oneyTsdescAmtorderdiffVamtRange):
        self.__oneyTsdescAmtorderdiffVamtRange = oneyTsdescAmtorderdiffVamtRange
        self.__apiParas["oney_tsdesc_amtorderdiff_vamt_range"] = oneyTsdescAmtorderdiffVamtRange

    def getOneyTsdescAmtorderdiffVamtRange(self):
        return self.__oneyTsdescAmtorderdiffVamtRange

    def setOpenId(self, openId):
        self.__openId = openId
        self.__apiParas["open_id"] = openId

    def getOpenId(self):
        return self.__openId

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setSixmFdescCvHourCntorder(self, sixmFdescCvHourCntorder):
        self.__sixmFdescCvHourCntorder = sixmFdescCvHourCntorder
        self.__apiParas["sixm_fdesc_cv_hour_cntorder"] = sixmFdescCvHourCntorder

    def getSixmFdescCvHourCntorder(self):
        return self.__sixmFdescCvHourCntorder

    def setSixmGddifDivOnlinepaymentallSumPayAmtorder(self, sixmGddifDivOnlinepaymentallSumPayAmtorder):
        self.__sixmGddifDivOnlinepaymentallSumPayAmtorder = sixmGddifDivOnlinepaymentallSumPayAmtorder
        self.__apiParas["sixm_gddif_div_onlinepaymentall_sum_pay_amtorder"] = sixmGddifDivOnlinepaymentallSumPayAmtorder

    def getSixmGddifDivOnlinepaymentallSumPayAmtorder(self):
        return self.__sixmGddifDivOnlinepaymentallSumPayAmtorder

    def setSixmGddifDivPhonedigitalallNCntprdcategory(self, sixmGddifDivPhonedigitalallNCntprdcategory):
        self.__sixmGddifDivPhonedigitalallNCntprdcategory = sixmGddifDivPhonedigitalallNCntprdcategory
        self.__apiParas["sixm_gddif_div_phonedigitalall_n_cntprdcategory"] = sixmGddifDivPhonedigitalallNCntprdcategory

    def getSixmGddifDivPhonedigitalallNCntprdcategory(self):
        return self.__sixmGddifDivPhonedigitalallNCntprdcategory

    def setSixmGddifDivSixmallNHourtwefourteenCntorder(self, sixmGddifDivSixmallNHourtwefourteenCntorder):
        self.__sixmGddifDivSixmallNHourtwefourteenCntorder = sixmGddifDivSixmallNHourtwefourteenCntorder
        self.__apiParas["sixm_gddif_div_sixmall_n_hourtwefourteen_cntorder"] = sixmGddifDivSixmallNHourtwefourteenCntorder

    def getSixmGddifDivSixmallNHourtwefourteenCntorder(self):
        return self.__sixmGddifDivSixmallNHourtwefourteenCntorder

    def setSixmGddifDivideFiveeightallNHourCntorder(self, sixmGddifDivideFiveeightallNHourCntorder):
        self.__sixmGddifDivideFiveeightallNHourCntorder = sixmGddifDivideFiveeightallNHourCntorder
        self.__apiParas["sixm_gddif_divide_fiveeightall_n_hour_cntorder"] = sixmGddifDivideFiveeightallNHourCntorder

    def getSixmGddifDivideFiveeightallNHourCntorder(self):
        return self.__sixmGddifDivideFiveeightallNHourCntorder

    def setSixmGddifMinusCaSumAorderCntproduct(self, sixmGddifMinusCaSumAorderCntproduct):
        self.__sixmGddifMinusCaSumAorderCntproduct = sixmGddifMinusCaSumAorderCntproduct
        self.__apiParas["sixm_gddif_minus_ca_sum_aorder_cntproduct"] = sixmGddifMinusCaSumAorderCntproduct

    def getSixmGddifMinusCaSumAorderCntproduct(self):
        return self.__sixmGddifMinusCaSumAorderCntproduct

    def setSixmGdescMinRecaddrcityAvgamt(self, sixmGdescMinRecaddrcityAvgamt):
        self.__sixmGdescMinRecaddrcityAvgamt = sixmGdescMinRecaddrcityAvgamt
        self.__apiParas["sixm_gdesc_min_recaddrcity_avgamt"] = sixmGdescMinRecaddrcityAvgamt

    def getSixmGdescMinRecaddrcityAvgamt(self):
        return self.__sixmGdescMinRecaddrcityAvgamt

    def setSixmGdescRangeRecaddrprovinceAvgamt(self, sixmGdescRangeRecaddrprovinceAvgamt):
        self.__sixmGdescRangeRecaddrprovinceAvgamt = sixmGdescRangeRecaddrprovinceAvgamt
        self.__apiParas["sixm_gdesc_range_recaddrprovince_avgamt"] = sixmGdescRangeRecaddrprovinceAvgamt

    def getSixmGdescRangeRecaddrprovinceAvgamt(self):
        return self.__sixmGdescRangeRecaddrprovinceAvgamt

    def setSpringfestivalGdescQuAamt(self, springfestivalGdescQuAamt):
        self.__springfestivalGdescQuAamt = springfestivalGdescQuAamt
        self.__apiParas["springfestival_gdesc_qu_aamt"] = springfestivalGdescQuAamt

    def getSpringfestivalGdescQuAamt(self):
        return self.__springfestivalGdescQuAamt

    def setThreemFddifMinusSevenaQdHourbinAmtaorder(self, threemFddifMinusSevenaQdHourbinAmtaorder):
        self.__threemFddifMinusSevenaQdHourbinAmtaorder = threemFddifMinusSevenaQdHourbinAmtaorder
        self.__apiParas["threem_fddif_minus_sevena_qd_hourbin_amtaorder"] = threemFddifMinusSevenaQdHourbinAmtaorder

    def getThreemFddifMinusSevenaQdHourbinAmtaorder(self):
        return self.__threemFddifMinusSevenaQdHourbinAmtaorder

    def setThreemGddifDivTravelrechargeallNCntprdcateg(self, threemGddifDivTravelrechargeallNCntprdcateg):
        self.__threemGddifDivTravelrechargeallNCntprdcateg = threemGddifDivTravelrechargeallNCntprdcateg
        self.__apiParas["threem_gddif_div_travelrechargeall_n_cntprdcateg"] = threemGddifDivTravelrechargeallNCntprdcateg

    def getThreemGddifDivTravelrechargeallNCntprdcateg(self):
        return self.__threemGddifDivTravelrechargeallNCntprdcateg

    def setThreemGddifDivideFailallNStsCntorder(self, threemGddifDivideFailallNStsCntorder):
        self.__threemGddifDivideFailallNStsCntorder = threemGddifDivideFailallNStsCntorder
        self.__apiParas["threem_gddif_divide_failall_n_sts_cntorder"] = threemGddifDivideFailallNStsCntorder

    def getThreemGddifDivideFailallNStsCntorder(self):
        return self.__threemGddifDivideFailallNStsCntorder

    def setThreemGddifDivideNullallSumPayAmtorder(self, threemGddifDivideNullallSumPayAmtorder):
        self.__threemGddifDivideNullallSumPayAmtorder = threemGddifDivideNullallSumPayAmtorder
        self.__apiParas["threem_gddif_divide_nullall_sum_pay_amtorder"] = threemGddifDivideNullallSumPayAmtorder

    def getThreemGddifDivideNullallSumPayAmtorder(self):
        return self.__threemGddifDivideNullallSumPayAmtorder

    def setThreemGdescSumSorderAmtaorder(self, threemGdescSumSorderAmtaorder):
        self.__threemGdescSumSorderAmtaorder = threemGdescSumSorderAmtaorder
        self.__apiParas["threem_gdesc_sum_sorder_amtaorder"] = threemGdescSumSorderAmtaorder

    def getThreemGdescSumSorderAmtaorder(self):
        return self.__threemGdescSumSorderAmtaorder

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def getApiMethodName(self):
        return "zhima.credit.msxf.onlinejdscore.query"

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
