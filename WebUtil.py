#!/usr/bin/python
# encoding=utf-8
import requests as requests
from urllib import quote


def buildQueryWithoutEncode(params):
    return buildQuery(params, False)


def buildQueryWithEncode(params):
    return buildQuery(params, True)


def buildQuery(params, needEncode):
    '''
    将params组合成key1=value1&key2=value2字符串
    :param params:字典
    :param needEncode:value是否需要encode
    :return string
    '''
    if not type(params) == dict:
        return False

    params_data = ''
    for (key, value) in params.iteritems():
        if checkEmpty(value):
            value = bool(needEncode) and quote(value) or value
            params_data = params_data + key + '=' + value + '&'
    params_data = params_data[:-1]
    return params_data


def checkEmpty(value):
    '''
    校验值非空
    :return bool: 非空则为true
    '''
    if bool(value.strip()):
        return True
    return False

def curl(url, postdata):
    '''
    post请求
    :param url: 请求地址
    :param postdata: 请求参数
    :return mixed: 返回值
    :raise 响应异常
    '''
    if "file" in postdata:
        file = {'file': postdata["file"]}
        postdata.pop("file")
        response = requests.post(url, data=postdata, files=file)
    else:
        response = requests.post(url, postdata)
    if response.status_code == 200:
        return response.content
    else:
        raise ValueError("ResponseCodeError: %i - %s" % (response.status_code, response.content))
