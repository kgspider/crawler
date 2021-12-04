// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function getEncryptedPassword(password, peEnSeed) {
    var pwd = CryptoJS.enc.Utf8.parse(CryptoJS.MD5(password));
    var key = CryptoJS.enc.Utf8.parse(peEnSeed);
    var iv = CryptoJS.enc.Utf8.parse("0123456789012345");
    var encrypted = CryptoJS.AES.encrypt(pwd, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    return pwd ? key ? encodeURIComponent(encrypted.toString()) : pwd : ""
}

// 测试样例
var password = "123456"
var peEnSeed = "2F63CCD861E4397F1C2181006904BAB2"
console.log(getEncryptedPassword(password, peEnSeed))
