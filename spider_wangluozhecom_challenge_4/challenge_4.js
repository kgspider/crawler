/* ==================================
# @Time    : 2021-12-13
# @Author  : 微信公众号：K哥爬虫
# @FileName: challenge_4.js
# @Software: PyCharm
# ================================== */

var CryptoJS = require('crypto-js')

let date = Date.parse(new Date());
window = {};

let key_tmp = date * 1234;
// let key_tmp = date * 1244;
let iv_tmp = date * 4321;
// let iv_tmp = date * 4311;

const key = CryptoJS.enc.Utf8.parse(key_tmp);
var iv = CryptoJS.enc.Utf8.parse(iv_tmp);
(function tmp(date, key, iv) {
    function Encrypt(word) {
        let srcs = CryptoJS.enc.Utf8.parse(word);
        let encrypted = CryptoJS.AES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return encrypted.ciphertext.toString().toUpperCase();
    }

    window.sign = Encrypt(date);
})(date, key, iv);

function getSign() {
    return window.sign
}

// 测试输出
// console.log(getSign())
