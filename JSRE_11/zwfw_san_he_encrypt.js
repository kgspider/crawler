isNotNull = function (obj) {
    if (obj === undefined || obj === null || obj == "null" || obj === "" || obj == "undefined")
        return false;
    return true;
};

function getDecryptedParameters(__signature) {
    var sig = "";
    var chars = "0123456789abcdef";
    if (!isNotNull(__signature)) {
        var curTime = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "" + Date.parse(new Date());
        sig = chars.charAt(parseInt(Math.random() * (15 - 15 + 1) + 10)) + chars.charAt(curTime.length) + "" + curTime;
    } else {
        sig = __signature;
    }

    var key = "";
    var keyIndex = -1;
    for (var i = 0; i < 6; i++) {
        var c = sig.charAt(keyIndex + 1);
        key += c;
        keyIndex = chars.indexOf(c);
        if (keyIndex < 0 || keyIndex >= sig.length) {
            keyIndex = i;
        }
    }

    var timestamp = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "_" + key + "_" + Date.parse(new Date());
    var t = timestamp;
    //LEx.azdg.encrypt(timestamp,key);
    t = t.replace(/\+/g, "_");
    return {"s": sig, "t": t};
}

// 测试样例
// console.log(getDecryptedParameters("c988121626057020055"))
