/*
# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-08-13
# @Author  : 微信公众号：K哥爬虫
# @FileName: youdao_encrypt.js
# @Software: PyCharm
# ==================================
*/


// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function getEncryptedParams(data, ua) {
    var bv = CryptoJS.MD5(ua).toString(),
        lts = "" + (new Date).getTime(),
        salt = lts + parseInt(10 * Math.random(), 10)
    var sign = CryptoJS.MD5('fanyideskweb' + data + salt + ']BjuETDhU)zqSxf-=B#7m').toString()
    return { bv: bv, lts: lts, salt: salt, sign: sign }
}

// var ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
// var data = "测试"
// console.log(getEncryptedParams(data, ua));