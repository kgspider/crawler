// 获取 black_box 参数

function oQ0OQ(Q0o0, o0OQ) {
    return Q0o0 < o0OQ;
}

function O000O(Q0o0, o0OQ) {
    return Q0o0 >> o0OQ;
}

function Qo0oo(Q0o0, o0OQ) {
    return Q0o0 | o0OQ;
}

function OOO0Q(Q0o0, o0OQ) {
    return Q0o0 << o0OQ;
}

function OooQo(Q0o0, o0OQ) {
    return Q0o0 & o0OQ;
}

function Oo0OO(Q0o0, o0OQ) {
    return Q0o0 + o0OQ;
}

var oQoo0 = {};
oQoo0["_keyStr"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
oQoo0["encode"] = function QQQ0(Q0o0) {
        var o0OQ = 62;
        while (o0OQ) {
            switch (o0OQ) {
                case 116 + 13 - 65: {
                    var Q000;
                    var Q00O;
                    var OQO0 = 0;
                    o0OQ = 65;
                    break;
                }
                case 118 + 8 - 63: {
                    var QQoO;
                    var oQOQ;
                    var ooQQ;
                    o0OQ = 64;
                    break;
                }
                case 94 + 8 - 40: {
                    var ooO0 = "";
                    var QQOQ;
                    var QOo0;
                    o0OQ = 63;
                    break;
                }
                case 122 + 6 - 63: {
                    Q0o0 = oQoo0["_utf8_encode"](Q0o0);
                    var Q0oO = 9;
                    while (Q0oO) {
                        switch (Q0oO) {
                            case 59 + 11 - 60: {
                                QQOQ = Q0o0["charCodeAt"](OQO0++),
                                    QOo0 = Q0o0["charCodeAt"](OQO0++),
                                    QQoO = Q0o0["charCodeAt"](OQO0++),
                                    oQOQ = O000O(QQOQ, 2),
                                    ooQQ = Qo0oo(OOO0Q(OooQo(QQOQ, 3), 4), O000O(QOo0, 4)),
                                    Q000 = Qo0oo(OOO0Q(OooQo(QOo0, 15), 2), O000O(QQoO, 6)),
                                    Q00O = OooQo(QQoO, 63);
                                if (isNaN(QOo0)) {
                                    Q000 = Q00O = 64;
                                } else if (isNaN(QQoO)) {
                                    Q00O = 64;
                                }
                                Q0oO = 11;
                                break;
                            }
                            case 50 + 15 - 56: {
                                Q0oO = oQ0OQ(OQO0, Q0o0["length"]) ? 10 : 0;
                                break;
                            }
                            case 95 + 5 - 89: {
                                ooO0 = Oo0OO(Oo0OO(Oo0OO(Oo0OO(ooO0, this["_keyStr"]["charAt"](oQOQ)), this["_keyStr"]["charAt"](ooQQ)), this["_keyStr"]["charAt"](Q000)), this["_keyStr"]["charAt"](Q00O));
                                Q0oO = 9;
                                break;
                            }
                        }
                    }
                    return ooO0;
                }
            }
        }
    };
oQoo0["_utf8_encode"] = function oOQ0(Q0o0) {
    Q0o0 = Q0o0["replace"](/\r\n/g, "");
    var o0OQ = "";
    for (var Q000 = 0; oQ0OQ(Q000, Q0o0["length"]); Q000++) {
        var Q00O = Q0o0["charCodeAt"](Q000);
        if (oQ0OQ(Q00O, 128)) {
            o0OQ += String["fromCharCode"](Q00O);
        } else if (Q0OQO(Q00O, 127) && oQ0OQ(Q00O, 2048)) {
            o0OQ += String["fromCharCode"](Qo0oo(O000O(Q00O, 6), 192)),
                o0OQ += String["fromCharCode"](Qo0oo(OooQo(Q00O, 63), 128));
        } else {
            o0OQ += String["fromCharCode"](Qo0oo(O000O(Q00O, 12), 224)),
                o0OQ += String["fromCharCode"](Qo0oo(OooQo(O000O(Q00O, 6), 63), 128)),
                o0OQ += String["fromCharCode"](Qo0oo(OooQo(Q00O, 63), 128));
        }
    }
    return o0OQ;
}

function OOoO0() {
    var tokens = "e0ia+fB5zvGuTjFDgcKahQwg2UEH8b0k7EK/Ukt4KwzyCbpm11jjy8Au64MC6s7HvLRacUxd7ka4AdDidJmYAA==";
    var version = "+X+3JWoUVBc12xtmgMpwzjAone3cp6/4QuFj7oWKNk+C4tqy4un/e29cODlhRmDy";
    var Oo0O0 = {};
    Oo0O0["blackBox"] = {};
    Oo0O0["blackBox"]["v"] = version;
    Oo0O0["blackBox"]["os"] = "web";
    Oo0O0["blackBox"]["it"] = parseInt(Math.random() * 100000);
    Oo0O0["blackBox"]["t"] = tokens;
    return oQoo0["encode"](JSON.stringify(Oo0O0["blackBox"]));
}

// 测试样例
// console.log(OOoO0())
