/*
# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-09-07
# @Author  : 微信公众号：K哥爬虫
# @FileName: xinshangmeng_encrypt.js
# @Software: PyCharm
# ==================================
*/

function getEncryptedPassword(a, b, c) {
    // a: 用户名, b: 密码, c: 验证码
    function d(a) {
        return n(e(o(m(a + "{1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss}")), 32))
    }

    function e(a, b) {
        for (var c = 1732584193, d = -271733879, e = -1732584194, f = 271733878, l = 0; l < a.length; l += 16) {
            var m = c
                , n = d
                , o = e
                , p = f;
            c = g(c, d, e, f, a[l + 0], 7, -680876936),
                f = g(f, c, d, e, a[l + 1], 12, -389564586),
                e = g(e, f, c, d, a[l + 2], 17, 606105819),
                d = g(d, e, f, c, a[l + 3], 22, -1044525330),
                c = g(c, d, e, f, a[l + 4], 7, -176418897),
                f = g(f, c, d, e, a[l + 5], 12, 1200080426),
                e = g(e, f, c, d, a[l + 6], 17, -1473231341),
                d = g(d, e, f, c, a[l + 7], 22, -45705983),
                c = g(c, d, e, f, a[l + 8], 7, 1770035416),
                f = g(f, c, d, e, a[l + 9], 12, -1958414417),
                e = g(e, f, c, d, a[l + 10], 17, -42063),
                d = g(d, e, f, c, a[l + 11], 22, -1990404162),
                c = g(c, d, e, f, a[l + 12], 7, 1804603682),
                f = g(f, c, d, e, a[l + 13], 12, -40341101),
                e = g(e, f, c, d, a[l + 14], 17, -1502002290),
                d = g(d, e, f, c, a[l + 15], 22, 1236535329),
                c = h(c, d, e, f, a[l + 1], 5, -165796510),
                f = h(f, c, d, e, a[l + 6], 9, -1069501632),
                e = h(e, f, c, d, a[l + 11], 14, 643717713),
                d = h(d, e, f, c, a[l + 0], 20, -373897302),
                c = h(c, d, e, f, a[l + 5], 5, -701558691),
                f = h(f, c, d, e, a[l + 10], 9, 38016083),
                e = h(e, f, c, d, a[l + 15], 14, -660478335),
                d = h(d, e, f, c, a[l + 4], 20, -405537848),
                c = h(c, d, e, f, a[l + 9], 5, 568446438),
                f = h(f, c, d, e, a[l + 14], 9, -1019803690),
                e = h(e, f, c, d, a[l + 3], 14, -187363961),
                d = h(d, e, f, c, a[l + 8], 20, 1163531501),
                c = h(c, d, e, f, a[l + 13], 5, -1444681467),
                f = h(f, c, d, e, a[l + 2], 9, -51403784),
                e = h(e, f, c, d, a[l + 7], 14, 1735328473),
                d = h(d, e, f, c, a[l + 12], 20, -1926607734),
                c = i(c, d, e, f, a[l + 5], 4, -378558),
                f = i(f, c, d, e, a[l + 8], 11, -2022574463),
                e = i(e, f, c, d, a[l + 11], 16, 1839030562),
                d = i(d, e, f, c, a[l + 14], 23, -35309556),
                c = i(c, d, e, f, a[l + 1], 4, -1530992060),
                f = i(f, c, d, e, a[l + 4], 11, 1272893353),
                e = i(e, f, c, d, a[l + 7], 16, -155497632),
                d = i(d, e, f, c, a[l + 10], 23, -1094730640),
                c = i(c, d, e, f, a[l + 13], 4, 681279174),
                f = i(f, c, d, e, a[l + 0], 11, -358537222),
                e = i(e, f, c, d, a[l + 3], 16, -722521979),
                d = i(d, e, f, c, a[l + 6], 23, 76029189),
                c = i(c, d, e, f, a[l + 9], 4, -640364487),
                f = i(f, c, d, e, a[l + 12], 11, -421815835),
                e = i(e, f, c, d, a[l + 15], 16, 530742520),
                d = i(d, e, f, c, a[l + 2], 23, -995338651),
                c = j(c, d, e, f, a[l + 0], 6, -198630844),
                f = j(f, c, d, e, a[l + 7], 10, 1126891415),
                e = j(e, f, c, d, a[l + 14], 15, -1416354905),
                d = j(d, e, f, c, a[l + 5], 21, -57434055),
                c = j(c, d, e, f, a[l + 12], 6, 1700485571),
                f = j(f, c, d, e, a[l + 3], 10, -1894986606),
                e = j(e, f, c, d, a[l + 10], 15, -1051523),
                d = j(d, e, f, c, a[l + 1], 21, -2054922799),
                c = j(c, d, e, f, a[l + 8], 6, 1873313359),
                f = j(f, c, d, e, a[l + 15], 10, -30611744),
                e = j(e, f, c, d, a[l + 6], 15, -1560198380),
                d = j(d, e, f, c, a[l + 13], 21, 1309151649),
                c = j(c, d, e, f, a[l + 4], 6, -145523070),
                f = j(f, c, d, e, a[l + 11], 10, -1120210379),
                e = j(e, f, c, d, a[l + 2], 15, 718787259),
                d = j(d, e, f, c, a[l + 9], 21, -343485551),
                c = k(c, m),
                d = k(d, n),
                e = k(e, o),
                f = k(f, p)
        }
        return new Array(c, d, e, f)
    }

    function f(a, b, c, d, e, f) {
        return k(l(k(k(b, a), k(d, f)), e), c)
    }

    function g(a, b, c, d, e, g, h) {
        return f(b & c | ~b & d, a, b, e, g, h)
    }

    function h(a, b, c, d, e, g, h) {
        return f(b & d | c & ~d, a, b, e, g, h)
    }

    function i(a, b, c, d, e, g, h) {
        return f(b ^ c ^ d, a, b, e, g, h)
    }

    function j(a, b, c, d, e, g, h) {
        return f(c ^ (b | ~d), a, b, e, g, h)
    }

    function k(a, b) {
        var c = (65535 & a) + (65535 & b);
        return (a >> 16) + (b >> 16) + (c >> 16) << 16 | 65535 & c
    }

    function l(a, b) {
        return a << b | a >>> 32 - b
    }

    function m(a) {
        for (var b = a.length, c = new Array(b), d = 0; d < b; d++) {
            var e = a.charCodeAt(d);
            c[d] = 255 & e
        }
        return c
    }

    function n(a) {
        for (var b = "0123456789abcdef", c = "", d = 0; d < 4 * a.length; d++)
            c += b.charAt(a[d >> 2] >> d % 4 * 8 + 4 & 15) + b.charAt(a[d >> 2] >> d % 4 * 8 & 15);
        return c
    }

    function o(a) {
        for (var b = 1 + (a.length + 8 >> 6), c = new Array(16 * b), d = 0; d < 16 * b; d++)
            c[d] = 0;
        for (var e = 0; e < a.length; e++)
            c[e >> 2] |= (255 & a[e]) << e % 4 * 8;
        return c[e >> 2] |= 128 << e % 4 * 8,
            c[16 * b - 2] = 8 * a.length,
            c
    }

    c.hex_md5 = d
    b = d(d(b) + c);
    return b
}

// 测试样例
// console.log(getEncryptedPassword('123123', '1231234', '6798'))
