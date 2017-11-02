#!/usr/bin/python
# encoding=utf-8
import base64
from M2Crypto import RSA, EVP


def sign(privatekey, data):
    '''
    加签
    :param privatekey:私钥文件路径
    :param data:要加签的数据
    :return string:签名
    '''
    signEVP = EVP.load_key(privatekey)
    signEVP.sign_init()
    signEVP.sign_update(data)
    result = signEVP.sign_final()
    return base64.b64encode(result)


def verify(zmPublickey, data, signvalue):
    '''
    验签
    :param zmPublickey:公钥文件路径
    :param data:待验签的数据
    :param signvalue:签名串
    :return bool:验签结果
    '''
    rsa_pub = RSA.load_pub_key(zmPublickey)
    verifyEVP = EVP.PKey()
    verifyEVP.assign_rsa(rsa_pub)
    verifyEVP.verify_init()
    verifyEVP.verify_update(data)
    result = verifyEVP.verify_final(base64.b64decode(signvalue))
    return result


def rsaEncrypt(zmPublickey, data):
    '''
    RSA加密
    :param zmPublickey:公钥文件路径
    :param data:待加密数据
    :return string:加密结果
    '''
    rsa_pub = RSA.load_pub_key(zmPublickey)
    maxlength = getMaxEncryptBlockSize(rsa_pub)
    encrypted = ''
    while (data):
        input = data[:maxlength]
        data = data[maxlength:]
        encrypted += rsa_pub.public_encrypt(input, RSA.pkcs1_padding)
    encrypted64 = base64.b64encode(encrypted)
    return encrypted64


def rsaDecrypt(privatekey, encrypted):
    '''
    RSA解密
    :param privatekey:私钥文件路径
    :param encrypted:待解密数据
    :return string:解密结果
    '''
    rsa_pri = RSA.load_key(privatekey)
    maxlength = getMaxDecryptBlockSize(rsa_pri)
    data = base64.b64decode(encrypted)
    decrypted = ''
    while (data):
        input = data[:maxlength]
        data = data[maxlength:]
        decrypted += rsa_pri.private_decrypt(input, RSA.pkcs1_padding)
    return decrypted


def getMaxEncryptBlockSize(rsa_pub):
    '''
    :return int:加密块大小
    '''
    return rsa_pub.__len__() / 8 - 11


def getMaxDecryptBlockSize(rsa_pri):
    '''
    :return int:解密块大小
    '''
    return rsa_pri.__len__() / 8
