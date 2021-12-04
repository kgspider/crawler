function randomString(N) {
    if (!parseInt(N, 10)) N = 6;
    var rs = Math.floor(Math.pow(36, N) * Math.random()).toString(36);
    return (Math.pow(10, N) + rs).substr(-N);
}

var h = require("node-cryptojs-aes").CryptoJS
    , p = {
    stringify: function (b) {
        var e = h.enc.Hex.parse(b.salt.toString()).toString(h.enc.Latin1);
        b = b.ciphertext.toString(h.enc.Latin1);
        return h.enc.Latin1.parse("Salted__" + e + b).toString(h.enc.Base64)
    },
    parse: function (b) {
        b = h.enc.Base64.parse(b).toString(h.enc.Latin1);
        if ("Salted__" !== b.substr(0, 8))
            throw Error("Error parsing salt");
        var e = b.substr(8, 8);
        b = b.substr(16);
        return h.lib.CipherParams.create({
            ciphertext: h.enc.Latin1.parse(b),
            salt: h.enc.Latin1.parse(e)
        })
    }
};

var e = randomString(36);

function getContent(address) {
    var b = JSON.stringify({
        "address": address,
        "ref": "",
        "uuid": "",
        "tz": "Asia/Shanghai",
        "tz_offset": 8,
        "screen": "1920x1080x24",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "cpu": 8,
        "lang": "zh"
    })
    return h.AES.encrypt(b, e, {
        format: p
    }).toString()
}

function getKey() {
    JSEncrypt = require("jsencrypt")
    var crypt = new JSEncrypt();
    var pub = [
        '-----BEGIN PUBLIC KEY-----',
        'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDVmYQhCYTnnkTPRMI5Ad3vfad9',
        'lhjzOU92FZ3reUiN/vmqP/wC1DKKExYDsqa+w5xBP0AjGkfDWk3q4PlWu0UsBGZx',
        '62Gvt0ds75u8FnmLv+ufMimF4962/9Lx7uyh9g1H3/ze5ZXscWYy3gtts9d2Ga0R',
        'pl0X49Cz0JhYYicuGwIDAQAB',
        '-----END PUBLIC KEY-----',
    ];
    crypt.setPublicKey(pub.join('\n'));
    key = crypt.encrypt(e);
    return key
}

function getContentAndKey(address) {
    result = {
        "key": getKey(),
        "content": getContent(address)
    }
    return result
}

// 测试样例
// console.log(getContentAndKey("xxxxxxxxxxxxxxxx"))
