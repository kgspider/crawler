/* ==================================
# @Time    : 2021-12-31
# @Author  : 微信公众号：K哥爬虫
# @FileName: pedata_decrypt.js
# @Software: PyCharm
# ================================== */

var zlib = require('zlib');

function L(e, t) {
    if ("1" == t)
        return [7, 65, 75, 31, 71, 101, 57, 0];
    for (var n = [], a = 0, r = t.length; a < r; a += 2)
        n.push(e.substr(1 * t.substr(a, 2), 1).charCodeAt());
    return n
}

function Y(e, t) {
    for (var n, a = new Uint8Array(e.length), r = 0, c = e.length; r < c; r++)
        n = t[r % t.length],
            a[r] = e[r].charCodeAt() ^ n;
    return a
}

function B(e) {
    var t, n, a, r, c, u, i, o = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=", s = "", f = 0;
    e = e.replace(/[^A-Za-z0-9\+\/\=]/g, "");
    while (f < e.length)
        r = o.indexOf(e.charAt(f++)),
            c = o.indexOf(e.charAt(f++)),
            u = o.indexOf(e.charAt(f++)),
            i = o.indexOf(e.charAt(f++)),
            t = r << 2 | c >> 4,
            n = (15 & c) << 4 | u >> 2,
            a = (3 & u) << 6 | i,
            s += String.fromCharCode(t),
        64 != u && (s += String.fromCharCode(n)),
        64 != i && (s += String.fromCharCode(a));
    return s
}

function getDecryptedData(encryptedData, exor, loginToken) {
    var a = L(loginToken, exor);
    var r = Y(B(encryptedData), a)
    var decryptedData = zlib.gunzipSync(r).toString();
    return decryptedData
}

// 测试样例
// var encryptedData = "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"
// var exor = "0446092417571135"
// var loginToken = "99a401435dcb65c4008d3ad22c8cdad0c78c433465528f9a941720fa367c900c"
// console.log(getDecryptedData(encryptedData, exor, loginToken))
