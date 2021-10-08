CryptoJS = require("crypto-js")

const key = CryptoJS.enc.Utf8.parse("20171109124536982017110912453698");
const iv = CryptoJS.enc.Utf8.parse('2017110912453698'); //十六位十六进制数作为密钥偏移量

function getEncryptedPassword(word) {
    let srcs = CryptoJS.enc.Utf8.parse(word);
    let encrypted = CryptoJS.AES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.ciphertext.toString().toUpperCase();
}

// 测试样例
// console.log(getEncryptedPassword("123457"))
