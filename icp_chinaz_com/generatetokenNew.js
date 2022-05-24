function generateKey() {
    var _0x5c32b4 = $("#IpValue").text();
    if (!_0x5c32b4) return "";
    var _0x2e5848 = _0x5c32b4.split(".");
    if (_0x2e5848.length != 4) return "";
    var _0x17eaf5 = _0x2e5848[3] + "." + _0x2e5848[2] + "." + _0x2e5848[1] + "." + _0x2e5848[0];
    var _0x3cbc20 = _0x17eaf5.split(".");
    var _0xaffdf = "";
    var _0x37535e = ".".charCodeAt();
    var _0x344dc3 = getRandom(10, 99);
    for (var _0x366322 = 0; _0x366322 < _0x3cbc20.length; _0x366322++) {
        var _0x15030e = 0;
        for (var _0x378993 = 0; _0x378993 < _0x3cbc20[_0x366322].length; _0x378993++) {
            var _0x52aae1 = _0x3cbc20[_0x366322].charAt(_0x378993);
            var _0x1648c2 = _0x52aae1.charCodeAt();
            _0x15030e = _0x15030e + _0x1648c2;
        }
        if (_0x366322 == _0x3cbc20.length - 1) _0x15030e = _0x15030e + _0x344dc3; else _0x15030e = _0x15030e + _0x37535e + _0x344dc3;
        _0xaffdf += _0x15030e + ",";
    }
    return encodeURIComponent(_0x344dc3 + "," + _0xaffdf.substr(0, _0xaffdf.length - 1));
}

function generateHostKey(_0x31852a) {
    if (!_0x31852a) return "";
    var _0x691267 = _0x31852a.split(".");
    if (_0x691267.length == 0) return "";
    var _0x38c6dc = "";
    for (var _0x553af4 = _0x691267.length - 1; _0x553af4 >= 0; _0x553af4--) {
        _0x38c6dc += "." + _0x691267[_0x553af4];
    }
    _0x38c6dc = _0x38c6dc.slice(1);
    var _0x341362 = _0x38c6dc.split(".");
    var _0x480f08 = "";
    var _0x1bdadb = ".".charCodeAt();
    var _0x4204f5 = getRandom(100, 999);
    for (var _0x553af4 = 0; _0x553af4 < _0x341362.length; _0x553af4++) {
        var _0xf2dc08 = 0;
        for (var _0x5b493a = 0; _0x5b493a < _0x341362[_0x553af4].length; _0x5b493a++) {
            var _0x363725 = _0x341362[_0x553af4].charAt(_0x5b493a);
            var _0x5cdfe9 = _0x363725.charCodeAt();
            _0xf2dc08 = _0xf2dc08 + _0x5cdfe9;
        }
        if (_0x553af4 == _0x341362.length - 1) _0xf2dc08 = _0xf2dc08 + _0x4204f5; else _0xf2dc08 = _0xf2dc08 + _0x1bdadb + _0x4204f5;
        _0x480f08 += "," + _0xf2dc08;
    }
    _0x480f08 = _0x480f08.slice(1);
    return _0x4204f5 + "," + _0x480f08;
}

function generateWordKey(_0x5a4116) {
    if (!_0x5a4116) return "";
    var _0x42a3ea = _0x5a4116.split("");
    var _0x2fbb00 = getRandom(100, 999);
    var _0x3da6fe = "";
    for (var _0x561235 = 0; _0x561235 < _0x42a3ea.length; _0x561235++) {
        var _0xf0c514 = _0x42a3ea[_0x561235].charCodeAt();
        var _0xe325e1 = _0xf0c514 + _0x2fbb00;
        _0x3da6fe += "," + _0xe325e1;
    }
    _0x3da6fe = _0x3da6fe.slice(1);
    return _0x2fbb00 + "," + _0x3da6fe;
}

function getRandom(_0xfffbab, _0x2b4642) {
    var _0x245c91 = _0x2b4642;
    var _0x3bc8f3 = _0xfffbab;
    if (_0x245c91 < _0x3bc8f3) {
        _0x245c91 = _0xfffbab;
        _0x3bc8f3 = _0x2b4642;
    }
    var _0x26cea3 = parseInt(Math.random() * (_0x245c91 - _0x3bc8f3 + 1) + _0x3bc8f3);
    return _0x26cea3;
};
