var CryptoJS = require('crypto-js');


o = {
    keyHex: CryptoJS.enc.Utf8.parse(Object({
        NODE_ENV: "production",
        VUE_APP_BASE_API: "/pro-api",
        VUE_APP_CONSTRUCTION_API: "/pro-api-construction",
        VUE_APP_DEV_FILE_PREVIEW: "/lyjcdFileView/onlinePreview",
        VUE_APP_FILE_ALL_PATH: "http://www.lyjcd.cn:8089",
        VUE_APP_FILE_PREFIX: "/mygroup",
        VUE_APP_LAND_API: "/pro-api-land",
        VUE_APP_PREVIEW_PREFIX: "/lyjcdFileView",
        VUE_APP_PROCUREMENT_API: "/pro-api-procurement",
        VUE_APP_WINDOW_TITLE: "金昌市公共资源交易网",
        BASE_URL: "/"
    }).VUE_APP_CUSTOM_KEY || "54367819"),
    ivHex: CryptoJS.enc.Utf8.parse(Object({
        NODE_ENV: "production",
        VUE_APP_BASE_API: "/pro-api",
        VUE_APP_CONSTRUCTION_API: "/pro-api-construction",
        VUE_APP_DEV_FILE_PREVIEW: "/lyjcdFileView/onlinePreview",
        VUE_APP_FILE_ALL_PATH: "http://www.lyjcd.cn:8089",
        VUE_APP_FILE_PREFIX: "/mygroup",
        VUE_APP_LAND_API: "/pro-api-land",
        VUE_APP_PREVIEW_PREFIX: "/lyjcdFileView",
        VUE_APP_PROCUREMENT_API: "/pro-api-procurement",
        VUE_APP_WINDOW_TITLE: "金昌市公共资源交易网",
        BASE_URL: "/"
    }).VUE_APP_CUSTOM_IV || "54367819")
};

function Public(t) {
    return CryptoJS.DES.encrypt(t, o.keyHex, {
        iv: o.ivHex,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).ciphertext.toString()
}


//console.log(c('ZBGG'))