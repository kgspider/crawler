// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function s(t) {
    var n = "4e87183cfd3a45fe"
    var e = {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }
      , i = CryptoJS.enc.Utf8.parse(n)
      , s = CryptoJS.AES.encrypt(t, i, e)
      , r = s.toString().replace(/\//g, "_");
    return r = r.replace(/\+/g, "-"),
    r
}

console.log(s("测试"))
