/* ==================================
# @Time    : 2021-12-01
# @Author  : 微信公众号：K哥爬虫
# @FileName: challenge_1.js
# @Software: PyCharm
# ================================== */

var window = {
    "document": {
        "location": {
            "href": "http://spider.wangluozhe.com/challenge/1"
        }
    },
}

var screen = {
    "availHeight": 1040
}
var document = {}
var navigator = {}
var location = {}

// 先保留原 constructor
Function.prototype.constructor_ = Function.prototype.constructor;
Function.prototype.constructor = function (a) {
    // 如果参数为 debugger，就返回空方法
    if(a == "debugger") {
        return function (){};
    }
    // 如果参数不为 debugger，还是返回原方法
    return Function.prototype.constructor_(a);
};

// 先保留原定时器
var setInterval_ = setInterval
setInterval = function (func, time){
    // 如果时间参数为 0x7d0，就返回空方法
    // 当然也可以不判断，直接返回空，有很多种写法
    if(time == 0x7d0)
    {
        return function () {};
    }
    // 如果时间参数不为 0x7d0，还是返回原方法
    return setInterval_(func, time)
}

var iｉl = 'jsjiami.com.v6'
  , iiIIilii = [iｉl, '\x73\x65\x74\x49\x6e\x74\x65\x72\x76\x61\x6c', '\x6a\x73\x6a', '\x69\x61\x6d', '\x75\x6e\x64\x65\x66\x69', '\x6e\x65\x64', '\x69\x2e\x63\x6f\x6d\x2e\x76', '\x6c\x65\x6e\x67\x74\x68', '\x70\x75\x73\x68', '\x61\x70\x70\x6c\x79', '\x62\x79\x74\x65\x64\x5f\x61\x63\x72\x61\x77\x6c\x65\x72', '\x73\x69\x67\x6e', '\x63\x72\x65\x61\x74\x65\x45\x6c\x65\x6d\x65\x6e\x74', '\x70\x61\x72\x73\x65', '\x74\x6f\x53\x74\x72\x69\x6e\x67', '\x31\x32\x33\x34\x35\x36\x37\x38\x39\x61\x62\x63\x64\x65\x66\x67\x68\x69\x67\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a', '\x66\x75\x6e\x63\x74\x69\x6f\x6e\x20\x2a\x5c\x28\x20\x2a\x5c\x29', '\x5c\x2b\x5c\x2b\x20\x2a\x28\x3f\x3a\x28\x3f\x3a\x5b\x61\x2d\x7a\x30\x2d\x39\x41\x2d\x5a\x5f\x5d\x29\x7b\x31\x2c\x38\x7d\x7c\x28\x3f\x3a\x5c\x62\x7c\x5c\x64\x29\x5b\x61\x2d\x7a\x30\x2d\x39\x5f\x5d\x7b\x31\x2c\x38\x7d\x28\x3f\x3a\x5c\x62\x7c\x5c\x64\x29\x29', '\x69\x6e\x69\x74', '\x74\x65\x73\x74', '\x63\x68\x61\x69\x6e', '\x69\x6e\x70\x75\x74', '\x72\x65\x74\x75\x72\x6e\x20\x28\x66\x75\x6e\x63\x74\x69\x6f\x6e\x28\x29\x20', '\x7b\x7d\x2e\x63\x6f\x6e\x73\x74\x72\x75\x63\x74\x6f\x72\x28\x22\x72\x65\x74\x75\x72\x6e\x20\x74\x68\x69\x73\x22\x29\x28\x20\x29', '\x63\x6f\x6e\x73\x6f\x6c\x65', '\x6c\x6f\x67', '\x77\x61\x72\x6e', '\x64\x65\x62\x75\x67', '\x69\x6e\x66\x6f', '\x65\x72\x72\x6f\x72', '\x65\x78\x63\x65\x70\x74\x69\x6f\x6e', '\x74\x72\x61\x63\x65', '\x64\x65\x66\x69\x6e\x65\x50\x72\x6f\x70\x65\x72\x74\x79', '\x63\x6f\x64\x65', '\x5f\x73\x69\x67\x6e\x61\x74\x75\x72\x65', '\x66\x75\x6e\x63\x74\x69\x6f\x6e\x20\x65\x76\x61\x6c\x28\x29\x20\x7b\x20\x5b\x6e\x61\x74\x69\x76\x65\x20\x63\x6f\x64\x65\x5d\x20\x7d', '\x66\x75\x6e\x63\x74\x69\x6f\x6e\x20\x74\x6f\x53\x74\x72\x69\x6e\x67\x28\x29\x20\x7b\x20\x5b\x6e\x61\x74\x69\x76\x65\x20\x63\x6f\x64\x65\x5d\x20\x7d', '\x67\x6e\x61\x74\x75\x72\x65\x20\x3d\x20\x77\x69\x6e\x64\x6f\x77\x2e\x62\x79\x74\x65\x64\x5f\x61\x63\x72\x61\x77\x6c\x65\x72\x28\x77\x69\x6e\x64\x6f\x77\x2e\x73\x69\x67\x6e\x28\x29\x29', '\x67\x6e\x61\x74\x75\x72\x65\x20\x3d\x20\x77\x69\x6e\x64\x6f\x77\x2e\x62\x79\x74\x65\x64\x5f\x61\x63\x72\x61\x77\x6c\x65\x72\x73\x28\x77\x69\x6e\x64\x6f\x77\x2e\x73\x69\x67\x6e\x73\x28\x29\x29', '\x61\x62\x63', '\x39\x30\x30\x31\x35\x30\x39\x38\x33\x63\x64\x32\x34\x66\x62\x30\x64\x36\x39\x36\x33\x66\x37\x64\x32\x38\x65\x31\x37\x66\x37\x32', '\x77\x69\x6e\x64\x6f\x77', '\x2e\x5f\x73\x69', '\x63\x6f\x6e\x63\x61\x74', '\x75\x73\x65\x72\x41\x67\x65\x6e\x74', '\x66\x75\x6e\x63\x74\x69\x6f\x6e\x20\x73\x65\x74\x49\x6e\x74\x65\x72\x76\x61\x6c\x28\x29\x20\x7b\x20\x5b\x6e\x61\x74\x69\x76\x65\x20\x63\x6f\x64\x65\x5d\x20\x7d', '\x63\x68\x61\x72\x43\x6f\x64\x65\x41\x74', '\x66\x72\x6f\x6d\x43\x68\x61\x72\x43\x6f\x64\x65', '\x64\x6f\x63\x75\x6d\x65\x6e\x74', '\x6c\x6f\x63\x61\x74\x69\x6f\x6e', '\x68\x72\x65\x66', '\x61\x76\x61\x69\x6c\x48\x65\x69\x67\x68\x74', '\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x41\x42\x43\x44\x45\x46', '\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x61\x62\x63\x64\x65\x66', '\x63\x68\x61\x72\x41\x74', '\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x2b\x2f', '\x67\x65\x74\x5f\x73\x69\x67\x6e', '\x73\x74\x72\x69\x6e\x67', '\x63\x6f\x6e\x73\x74\x72\x75\x63\x74\x6f\x72', '\x64\x65\x62\x75\x67\x67\x65\x72\x3b', '\x63\x6f\x75\x6e\x74\x65\x72', '\x64\x65\x62\x75', '\x67\x67\x65\x72', '\x63\x61\x6c\x6c', '\x61\x63\x74\x69\x6f\x6e', '\x73\x74\x61\x74\x65\x4f\x62\x6a\x65\x63\x74', '\x6a\x73\x6a\x69\x61\x66\x6e\x77\x6d\x69\x2e\x63\x52\x77\x64\x6f\x6d\x2e\x76\x36\x47\x4b\x62\x77\x4b\x72\x52\x46\x43\x74\x53\x43\x3d\x3d'];
var liIIIi11 = function(_0x11145e, _0x3cbe90) {
    _0x11145e = ~~'0x'['concat'](_0x11145e);
    var _0x636e4d = iiIIilii[_0x11145e];
    return _0x636e4d;
};
(function(_0x52284d, _0xfd26eb) {
    var _0x1bba22 = 0x0;
    for (_0xfd26eb = _0x52284d['shift'](_0x1bba22 >> 0x2); _0xfd26eb && _0xfd26eb !== (_0x52284d['pop'](_0x1bba22 >> 0x3) + '')['replace'](/[fnwRwdGKbwKrRFCtSC=]/g, ''); _0x1bba22++) {
        _0x1bba22 = _0x1bba22 ^ 0x661c2;
    }
}(iiIIilii, liIIIi11));
// window[liIIIi11('0')](function() {
//     var l111IlII = liIIIi11('1') + liIIIi11('2');
//     if (typeof iｉl == liIIIi11('3') + liIIIi11('4') || iｉl != l111IlII + liIIIi11('5') + l111IlII[liIIIi11('6')]) {
//         var Ilil11iI = [];
//         while (Ilil11iI[liIIIi11('6')] > -0x1) {
//             Ilil11iI[liIIIi11('7')](Ilil11iI[liIIIi11('6')] ^ 0x2);
//         }
//     }
//     iliI1lli();
// }, 0x7d0);
(function() {
    var iiIIiil = function() {
        var IllIlIlI = !![];
        return function(I1i1ii1, lI11i1lI) {
            var illIIIl = IllIlIlI ? function() {
                if (lI11i1lI) {
                    var I111lI1 = lI11i1lI[liIIIi11('8')](I1i1ii1, arguments);
                    lI11i1lI = null;
                    return I111lI1;
                }
            }
            : function() {}
            ;
            IllIlIlI = ![];
            return illIIIl;
        }
        ;
    }();
    var l1liii11 = function() {
        var ilI1ilI = !![];
        return function(iIliII1l, IlliIIi1) {
            var li11lII1 = ilI1ilI ? function() {
                if (IlliIIi1) {
                    var li11lIl1 = IlliIIi1[liIIIi11('8')](iIliII1l, arguments);
                    IlliIIi1 = null;
                    return li11lIl1;
                }
            }
            : function() {}
            ;
            ilI1ilI = ![];
            return li11lII1;
        }
        ;
    }();
    window[liIIIi11('9')] = function byted_acrawler() {
        return IIl1llI1(window.sign());
        // return IIl1llI1(window[liIIIi11('a')])
    }
    ;
    window[liIIIi11('a')] = function sign() {
        try {
            div = document[liIIIi11('b')];
            return Date[liIIIi11('c')](new Date())[liIIIi11('d')]();
        } catch (IIl1lI1i) {
            return liIIIi11('e');
        }
    }
    ;
    (function() {
        (function() {
            iiIIiil(this, function() {
                var ii1iill = new RegExp(liIIIi11('f'));
                var iliIIil = new RegExp(liIIIi11('10'),'\x69');
                var IIIi1iii = iliI1lli(liIIIi11('11'));
                if (!ii1iill[liIIIi11('12')](IIIi1iii + liIIIi11('13')) || !iliIIil[liIIIi11('12')](IIIi1iii + liIIIi11('14'))) {
                    IIIi1iii('\x30');
                } else {
                    iliI1lli();
                }
            })();
        }());
        var lliIIi1I = l1liii11(this, function() {
            var IlII1li1 = function() {};
            var IIlIIiii;
            try {
                var IiIiIlil = Function(liIIIi11('15') + liIIIi11('16') + '\x29\x3b');
                IIlIIiii = IiIiIlil();
            } catch (liilIIii) {
                IIlIIiii = window;
            }
            // if (!IIlIIiii[liIIIi11('17')]) {
            //     IIlIIiii[liIIIi11('17')] = function(IlII1li1) {
            //         var llii1li1 = {};
            //         llii1li1[liIIIi11('18')] = IlII1li1;
            //         llii1li1[liIIIi11('19')] = IlII1li1;
            //         llii1li1[liIIIi11('1a')] = IlII1li1;
            //         llii1li1[liIIIi11('1b')] = IlII1li1;
            //         llii1li1[liIIIi11('1c')] = IlII1li1;
            //         llii1li1[liIIIi11('1d')] = IlII1li1;
            //         llii1li1[liIIIi11('1e')] = IlII1li1;
            //         return llii1li1;
            //     }(IlII1li1);
            // } else {
            //     IIlIIiii[liIIIi11('17')][liIIIi11('18')] = IlII1li1;
            //     IIlIIiii[liIIIi11('17')][liIIIi11('19')] = IlII1li1;
            //     IIlIIiii[liIIIi11('17')][liIIIi11('1a')] = IlII1li1;
            //     IIlIIiii[liIIIi11('17')][liIIIi11('1b')] = IlII1li1;
            //     IIlIIiii[liIIIi11('17')][liIIIi11('1c')] = IlII1li1;
            //     IIlIIiii[liIIIi11('17')][liIIIi11('1d')] = IlII1li1;
            //     IIlIIiii[liIIIi11('17')][liIIIi11('1e')] = IlII1li1;
            // }
        });
        lliIIi1I();
        'use strict';
        var i1Iiil1 = '';
        Object[liIIIi11('1f')](window, liIIIi11('20'), {
            '\x73\x65\x74': function(iil1l1I1) {
                i1Iiil1 = iil1l1I1;
                return iil1l1I1;
            },
            '\x67\x65\x74': function() {
                return i1Iiil1;
            }
        });
    }());
    // (function() {
    //     'use strict';
    //     var i1I1i1li = '';
    //     Object[liIIIi11('1f')](window, liIIIi11('21'), {
    //         '\x73\x65\x74': function(illllli1) {
    //             i1I1i1li = illllli1;
    //             return illllli1;
    //         },
    //         '\x67\x65\x74': function() {
    //             return i1I1i1li;
    //         }
    //     });
    // }());
    var iiil1 = 0x0;
    var l11il1l1 = '';
    var ii1Ii = 0x8;
    function i1Il11i(iiIll1i) {
        return lIIiiI1l(iIIiIlli(IIl111li(iiIll1i), iiIll1i[liIIIi11('6')] * ii1Ii));
    }
    function I1lIIlil(l11l1iIi) {
        return I1i11ll(iIIiIlli(IIl111li(l11l1iIi), l11l1iIi[liIIIi11('6')] * ii1Ii));
    }
    function lllIIiI(IIi1lIil) {
        return l1IlIlIi(iIIiIlli(IIl111li(IIi1lIil), IIi1lIil[liIIIi11('6')] * ii1Ii));
    }
    function IilIlI1i(ll1l1ii1, Ilil1i11) {
        return lIIiiI1l(Iii1I1il(ll1l1ii1, Ilil1i11));
    }
    function llII11iI(IllliliI, IIIIilI) {
        return I1i11ll(Iii1I1il(IllliliI, IIIIilI));
    }
    function l11l1iil(liii1iI1, lilii111) {
        return l1IlIlIi(Iii1I1il(liii1iI1, lilii111));
    }
    (function() {
        try {
            let iI1lil1i = eval;
            if (iI1lil1i + '' == liIIIi11('22') && iI1lil1i[liIIIi11('d')]() + '' == liIIIi11('22') && iI1lil1i[liIIIi11('d')] + '' == liIIIi11('23')) {
                window[liIIIi11('20')] = liIIIi11('24');
            } else {
                window[liIIIi11('20')] = liIIIi11('25');
            }
        } catch (i1iIliIi) {
            window[liIIIi11('20')] = liIIIi11('25');
        }
    }());
    function lIliIIII() {
        return i1Il11i(liIIIi11('26')) == liIIIi11('27');
    }
    function iIIiIlli(lIliI1I1, lllI11lI) {
        lIliI1I1[lllI11lI >> 0x5] |= 0x80 << lllI11lI % 0x20;
        lIliI1I1[(lllI11lI + 0x40 >>> 0x9 << 0x4) + 0xe] = lllI11lI;
        var ill1Ill = 0x67452301;
        var iI1l1iIi = -0x10325477;
        var I1l1iI1 = -0x67452302;
        var IIlili = 0x10325476;
        for (var lii11ii = 0x0; lii11ii < lIliI1I1[liIIIi11('6')]; lii11ii += 0x10) {
            var IlIIIIl1 = ill1Ill;
            var il1I1li = iI1l1iIi;
            var lilIlIi1 = I1l1iI1;
            var lli11i1i = IIlili;
            ill1Ill = iiiIillI(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x0], 0x7, -0x28955b88);
            IIlili = iiiIillI(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x1], 0xc, -0x173848aa);
            I1l1iI1 = iiiIillI(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0x2], 0x11, 0x242070db);
            iI1l1iIi = iiiIillI(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x3], 0x16, -0x3e423112);
            ill1Ill = iiiIillI(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x4], 0x7, -0xa83f051);
            IIlili = iiiIillI(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x5], 0xc, 0x4787c62a);
            I1l1iI1 = iiiIillI(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0x6], 0x11, -0x57cfb9ed);
            iI1l1iIi = iiiIillI(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x7], 0x16, -0x2b96aff);
            ill1Ill = iiiIillI(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x8], 0x7, 0x698098d8);
            IIlili = iiiIillI(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x9], 0xc, -0x74bb0851);
            I1l1iI1 = iiiIillI(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0xa], 0x11, -0xa44f);
            iI1l1iIi = iiiIillI(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0xb], 0x16, -0x76a32842);
            ill1Ill = iiiIillI(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0xc], 0x7, 0x6b901122);
            IIlili = iiiIillI(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0xd], 0xc, -0x2678e6d);
            I1l1iI1 = iiiIillI(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0xe], 0x11, -0x5986bc72);
            iI1l1iIi = iiiIillI(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0xf], 0x16, 0x49b40821);
            ill1Ill = lillIii1(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x1], 0x5, -0x9e1da9e);
            IIlili = lillIii1(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x6], 0x9, -0x3fbf4cc0);
            I1l1iI1 = lillIii1(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0xb], 0xe, 0x265e5a51);
            iI1l1iIi = lillIii1(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x0], 0x14, -0x16493856);
            ill1Ill = lillIii1(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x5], 0x5, -0x29d0efa3);
            IIlili = lillIii1(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0xa], 0x9, 0x2441453);
            I1l1iI1 = lillIii1(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0xf], 0xe, -0x275e197f);
            iI1l1iIi = lillIii1(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x4], 0x14, -0x182c0438);
            ill1Ill = lillIii1(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x9], 0x5, 0x21e1cde6);
            IIlili = lillIii1(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0xe], 0x9, -0x3cc8f82a);
            I1l1iI1 = lillIii1(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0x3], 0xe, -0xb2af279);
            iI1l1iIi = lillIii1(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x8], 0x14, 0x455a14ed);
            ill1Ill = lillIii1(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0xd], 0x5, -0x561c16fb);
            IIlili = lillIii1(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x2], 0x9, -0x3105c08);
            I1l1iI1 = lillIii1(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0x7], 0xe, 0x676f02d9);
            iI1l1iIi = lillIii1(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0xc], 0x14, -0x72d5b376);
            ill1Ill = liIiiiiI(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x5], 0x4, -0x5c6be);
            IIlili = liIiiiiI(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x8], 0xb, -0x788e097f);
            I1l1iI1 = liIiiiiI(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0xb], 0x10, 0x6d9d6122);
            iI1l1iIi = liIiiiiI(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0xe], 0x17, -0x21ac7f4);
            ill1Ill = liIiiiiI(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x1], 0x4, -0x5b4115bc);
            IIlili = liIiiiiI(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x4], 0xb, 0x4bdecfa9);
            I1l1iI1 = liIiiiiI(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0x7], 0x10, -0x944b4a0);
            iI1l1iIi = liIiiiiI(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0xa], 0x17, -0x41404390);
            ill1Ill = liIiiiiI(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0xd], 0x4, 0x289b7ec6);
            IIlili = liIiiiiI(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x0], 0xb, -0x155ed806);
            I1l1iI1 = liIiiiiI(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0x3], 0x10, -0x2b10cf67);
            iI1l1iIi = liIiiiiI(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x6], 0x17, 0x4881d03);
            ill1Ill = liIiiiiI(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x9], 0x4, -0x262b2fc7);
            IIlili = liIiiiiI(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0xc], 0xb, -0x1924661b);
            I1l1iI1 = liIiiiiI(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0xf], 0x10, 0x1fa27cf8);
            iI1l1iIi = liIiiiiI(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x2], 0x17, -0x3b53a99b);
            ill1Ill = Ili1iIll(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x0], 0x6, -0xbd6ddbc);
            IIlili = Ili1iIll(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x7], 0xa, 0x432aff97);
            I1l1iI1 = Ili1iIll(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0xe], 0xf, -0x546bdc59);
            iI1l1iIi = Ili1iIll(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x5], 0x15, -0x36c5fc7);
            ill1Ill = Ili1iIll(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0xc], 0x6, 0x655b59c3);
            IIlili = Ili1iIll(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0x3], 0xa, -0x70f3336e);
            I1l1iI1 = Ili1iIll(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0xa], 0xf, -0x100b83);
            iI1l1iIi = Ili1iIll(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x1], 0x15, -0x7a7ba22f);
            ill1Ill = Ili1iIll(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x8], 0x6, 0x6fa87e4f);
            IIlili = Ili1iIll(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0xf], 0xa, -0x1d31920);
            I1l1iI1 = Ili1iIll(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0x6], 0xf, -0x5cfebcec);
            iI1l1iIi = Ili1iIll(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0xd], 0x15, 0x4e0811a1);
            ill1Ill = Ili1iIll(ill1Ill, iI1l1iIi, I1l1iI1, IIlili, lIliI1I1[lii11ii + 0x4], 0x6, -0x8ac817e);
            IIlili = Ili1iIll(IIlili, ill1Ill, iI1l1iIi, I1l1iI1, lIliI1I1[lii11ii + 0xb], 0xa, -0x42c50dcb);
            I1l1iI1 = Ili1iIll(I1l1iI1, IIlili, ill1Ill, iI1l1iIi, lIliI1I1[lii11ii + 0x2], 0xf, 0x2ad7d2bb);
            iI1l1iIi = Ili1iIll(iI1l1iIi, I1l1iI1, IIlili, ill1Ill, lIliI1I1[lii11ii + 0x9], 0x15, -0x14792c6f);
            ill1Ill = l111i1I(ill1Ill, IlIIIIl1);
            iI1l1iIi = l111i1I(iI1l1iIi, il1I1li);
            I1l1iI1 = l111i1I(I1l1iI1, lilIlIi1);
            IIlili = l111i1I(IIlili, lli11i1i);
        }
        return Array(ill1Ill, iI1l1iIi, I1l1iI1, IIlili);
    }
    function IlIliI1l() {
        return liIIIi11('28');
    }
    function l1Ii1ili(IIl1i1ii, lI1li11l, lIll1lIi, ilIii1, ll11l1, I111ilI1) {
        return l111i1I(Il1111lI(l111i1I(l111i1I(lI1li11l, IIl1i1ii), l111i1I(ilIii1, I111ilI1)), ll11l1), lIll1lIi);
    }
    function iiiIillI(lI1lIll, iI1I1i11, iI1IilI, IIll1Il, lIiIIi, ii1Il1Ii, illlI11l) {
        return l1Ii1ili(iI1I1i11 & iI1IilI | ~iI1I1i11 & IIll1Il, lI1lIll, iI1I1i11, lIiIIi, ii1Il1Ii, illlI11l);
    }
    function lillIii1(Il1Il11, iI1IiIi, IliilIl, i11l111I, I1II1il1, liiiIl1, ll1Il1ll) {
        return l1Ii1ili(iI1IiIi & i11l111I | IliilIl & ~i11l111I, Il1Il11, iI1IiIi, I1II1il1, liiiIl1, ll1Il1ll);
    }
    function liIiiiiI(I1ii11Il, lIiI1Ili, ii11lili, ll1liiiI, lIIIl11l, lI1II1Il, lliiiI) {
        return l1Ii1ili(lIiI1Ili ^ ii11lili ^ ll1liiiI, I1ii11Il, lIiI1Ili, lIIIl11l, lI1II1Il, lliiiI);
    }
    function iIlII1I1(l11i1iI1, Il1Iiil1) {
        return liIIIi11('29');
    }
    function Ili1iIll(ii11lIll, iIiilli1, IIIlli1, iiIl1iII, Iillilll, lIIiI1II, iiiIlIl1) {
        return l1Ii1ili(IIIlli1 ^ (iIiilli1 | ~iiIl1iII), ii11lIll, iIiilli1, Iillilll, lIIiI1II, iiiIlIl1);
    }
    function Iii1I1il(l11ll1ll, IIlii1lI) {
        var Il1IlI1i = IIl111li(l11ll1ll);
        if (Il1IlI1i[liIIIi11('6')] > 0x10)
            Il1IlI1i = iIIiIlli(Il1IlI1i, l11ll1ll[liIIIi11('6')] * ii1Ii);
        var IiiiIlII = Array(0x10)
          , llIii11l = Array(0x10);
        for (var i1liIi = 0x0; i1liIi < 0x10; i1liIi++) {
            IiiiIlII[i1liIi] = Il1IlI1i[i1liIi] ^ 0x36363636;
            llIii11l[i1liIi] = Il1IlI1i[i1liIi] ^ 0x5c5c5c5c;
        }
        var ilIl1I1i = iIIiIlli(IiiiIlII[liIIIi11('2a')](IIl111li(IIlii1lI)), 0x200 + IIlii1lI[liIIIi11('6')] * ii1Ii);
        return iIIiIlli(llIii11l[liIIIi11('2a')](ilIl1I1i), 0x200 + 0x80);
    }
    function l111i1I(IIllIi1l, IIllI1l1) {
        var IIll1I11 = (IIllIi1l & 0xffff) + (IIllI1l1 & 0xffff);
        var i1iiiiI = (IIllIi1l >> 0x10) + (IIllI1l1 >> 0x10) + (IIll1I11 >> 0x10);
        return i1iiiiI << 0x10 | IIll1I11 & 0xffff;
    }
    function IIl1llI1(Iiilii1i) {
        try {
            nav = navigator[liIIIi11('2b')];
            return i1Il11i(Iiilii1i);
        } catch (IIilIIlI) {
            return i1Il11i(IIilIIlI);
        }
    }
    (function() {
        try {
            var lI1IlIli = window[liIIIi11('0')];
            gcdw = setInterval;
            if (gcdw + '' == liIIIi11('2c') && gcdw[liIIIi11('d')]() + '' == liIIIi11('2c') && gcdw[liIIIi11('d')] + '' == liIIIi11('23')) {
                window[liIIIi11('20')] = liIIIi11('24');
            } else {
                window[liIIIi11('20')] = liIIIi11('25');
            }
        } catch (i1lIill) {
            window[liIIIi11('20')] = liIIIi11('25');
        }
    }());
    function Il1111lI(IilIiii1, iiI1i1i1) {
        return IilIiii1 << iiI1i1i1 | IilIiii1 >>> 0x20 - iiI1i1i1;
    }
    function IIl111li(lIiIIIi) {
        var IIli1i1 = Array();
        var lIliI1i1 = (0x1 << ii1Ii) - 0x1;
        for (var lIiiil1 = 0x0; lIiiil1 < lIiIIIi[liIIIi11('6')] * ii1Ii; lIiiil1 += ii1Ii)
            IIli1i1[lIiiil1 >> 0x5] |= (lIiIIIi[liIIIi11('2d')](lIiiil1 / ii1Ii) & lIliI1i1) << lIiiil1 % 0x20;
        return IIli1i1;
    }
    function l1IlIlIi(IIIiliII) {
        var I1l1III1 = '';
        var llIi1il1 = (0x1 << ii1Ii) - 0x1;
        for (var iIii1ll = 0x0; iIii1ll < IIIiliII[liIIIi11('6')] * 0x20; iIii1ll += ii1Ii)
            I1l1III1 += String[liIIIi11('2e')](IIIiliII[iIii1ll >> 0x5] >>> iIii1ll % 0x20 & llIi1il1);
        return I1l1III1;
    }
    function IIlIliii(II1, iIIiIIi1) {
        try {
            href = window[liIIIi11('2f')][liIIIi11('30')][liIIIi11('31')];
            check_screen = screen[liIIIi11('32')];
            window[liIIIi11('20')] = liIIIi11('24');
            return '';
        } catch (I1IiI1il) {
            window[liIIIi11('20')] = liIIIi11('25');
            return '';
        }
    }
    function lIIiiI1l(lilll1I1) {
        var ililI1i = iiil1 ? liIIIi11('33') : liIIIi11('34');
        var Iii1iiIl = '';
        for (var Illi1ill = 0x0; Illi1ill < lilll1I1[liIIIi11('6')] * 0x4; Illi1ill++) {
            Iii1iiIl += ililI1i[liIIIi11('35')](lilll1I1[Illi1ill >> 0x2] >> Illi1ill % 0x4 * 0x8 + 0x4 & 0xf) + ililI1i[liIIIi11('35')](lilll1I1[Illi1ill >> 0x2] >> Illi1ill % 0x4 * 0x8 & 0xf);
        }
        return Iii1iiIl;
    }
    function I1i11ll(liliII) {
        var iiiiII1I = liIIIi11('36');
        var IiilIl = '';
        for (var iliIiii1 = 0x0; iliIiii1 < liliII[liIIIi11('6')] * 0x4; iliIiii1 += 0x3) {
            var I1IlIIIi = (liliII[iliIiii1 >> 0x2] >> 0x8 * (iliIiii1 % 0x4) & 0xff) << 0x10 | (liliII[iliIiii1 + 0x1 >> 0x2] >> 0x8 * ((iliIiii1 + 0x1) % 0x4) & 0xff) << 0x8 | liliII[iliIiii1 + 0x2 >> 0x2] >> 0x8 * ((iliIiii1 + 0x2) % 0x4) & 0xff;
            for (var IIIl1ilI = 0x0; IIIl1ilI < 0x4; IIIl1ilI++) {
                if (iliIiii1 * 0x8 + IIIl1ilI * 0x6 > liliII[liIIIi11('6')] * 0x20)
                    IiilIl += l11il1l1;
                else
                    IiilIl += iiiiII1I[liIIIi11('35')](I1IlIIIi >> 0x6 * (0x3 - IIIl1ilI) & 0x3f);
            }
        }
        return IiilIl;
    }
    setInterval(function() {
        debugger ;console[liIIIi11('18')]();
    }, 0x7d0);
    window[liIIIi11('37')] = function() {
        eval(IIlIliii() + IlIliI1l() + iIlII1I1() + window[liIIIi11('20')]);
    }
    ;
    window[liIIIi11('37')]();
}());

function iliI1lli(lil1I1) {
    function lili11I(l11I11l1) {
        if (typeof l11I11l1 === liIIIi11('38')) {
            return function(lllI11i) {}
            [liIIIi11('39')](liIIIi11('3a'))[liIIIi11('8')](liIIIi11('3b'));
        } else {
            if (('' + l11I11l1 / l11I11l1)[liIIIi11('6')] !== 0x1 || l11I11l1 % 0x14 === 0x0) {
                (function() {
                    return !![];
                }
                [liIIIi11('39')](liIIIi11('3c') + liIIIi11('3d'))[liIIIi11('3e')](liIIIi11('3f')));
            } else {
                (function() {
                    return ![];
                }
                [liIIIi11('39')](liIIIi11('3c') + liIIIi11('3d'))[liIIIi11('8')](liIIIi11('40')));
            }
        }
        lili11I(++l11I11l1);
    }
    try {
        if (lil1I1) {
            return lili11I;
        } else {
            lili11I(0x0);
        }
    } catch (liIlI1il) {}
}
;iｉl = 'jsjiami.com.v6';

// function getSign(){
//     return window[liIIIi11('9')](window[liIIIi11('a')]())
// }

function getSign(){
    return window.byted_acrawler(window.sign())
}

console.log(getSign())
