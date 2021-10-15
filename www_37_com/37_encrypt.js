/*
# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-08-20
# @Author  : 微信公众号：K哥爬虫
# @FileName: 37_encrypt.js
# @Software: PyCharm
# ==================================
*/

var ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
function __rsa(str) {
    var out, i, len;
    var c1, c2, c3;
    len = str.length;
    i = 0;
    out = "";
    while (i < len) {
        c1 = str.charCodeAt(i++) & 0xff;
        if (i == len) {
            out += ch.charAt(c1 >> 2);
            out += ch.charAt((c1 & 0x3) << 4);
            out += "==";
            break
        }
        c2 = str.charCodeAt(i++);
        if (i == len) {
            out += ch.charAt(c1 >> 2);
            out += ch.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4));
            out += ch.charAt((c2 & 0xF) << 2);
            out += "=";
            break
        }
        c3 = str.charCodeAt(i++);
        out += ch.charAt(c1 >> 2);
        out += ch.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4));
        out += ch.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >> 6));
        out += ch.charAt(c3 & 0x3F)
    }
    return out
}

function getEncryptedPassword(a) {
    var maxPos = ch.length - 2
      , w = [];
    for (i = 0; i < 15; i++) {
        w.push(ch.charAt(Math.floor(Math.random() * maxPos)));
        if (i === 7) {
            w.push(a.substr(0, 3))
        }
        if (i === 12) {
            w.push(a.substr(3))
        }
    }
    return __rsa(w.join(""))
}

// 测试样例
// console.log(getEncryptedPassword("34343434"))
