/* ==================================
# @Time    : 2022-08-29
# @Author  : 微信公众号：K哥爬虫
# @FileName: frida-hook.js
# @Software: PyCharm
# ================================== */


Java.perform(
    function(){
        console.log("[*] Hook begin")

        // 方法一：Hook 三个检测方法，让它们都返回 false，不再执行后续的 a 方法，就不会退出 APP 了
        // var vantagePoint = Java.use("sg.vantagepoint.a.c")
        // vantagePoint.a.implementation = function(){
        //     console.log("[*] Hook vantagepoint.a.c.a")
        //     this.a();
        //     return false;
        // }
        // vantagePoint.b.implementation = function(){
        //     console.log("[*] Hook vantagepoint.a.c.b")
        //     this.b();
        //     return false;
        // }
        // vantagePoint.c.implementation = function(){
        //     console.log("[*] Hook vantagepoint.a.c.c")
        //     this.c();
        //     return false;
        // }

        // 方法二：Hook a() 方法，置空，什么都不做，不弹出对话框，也不退出 APP
        // var mainActivity = Java.use("sg.vantagepoint.uncrackable1.MainActivity");
        // mainActivity.a.implementation = function(){
        //    console.log("[*] Hook mainActivity.a")
        // }

        // 方法三：Hook onClick() 方法，点击 OK 后不让其退出 APP
        // var mainActivity$1 = Java.use("sg.vantagepoint.uncrackable1.MainActivity$1");
        // mainActivity$1.onClick.implementation = function(){
        //     console.log("[*] Hook mainActivity$1.onClick")
        // }

        // 方法四：Hook System.exit 方法，点击 OK 后不让其退出 APP
        var javaSystem = Java.use("java.lang.System");
        javaSystem.exit.implementation = function(){
            console.log("[*] Hook system.exit")
        }

        var cryptoAES = Java.use("sg.vantagepoint.a.a");
        cryptoAES.a.implementation = function(bArr, bArr2){
            console.log("[*] Hook cryptoAES")
            var secret = "";
            var decryptValue = this.a(bArr, bArr2);
            console.log("[*] DecryptValue:", decryptValue)
            for (var i=0; i < decryptValue.length; i++){
              secret += String.fromCharCode(decryptValue[i]);
            }
            console.log("[*] Secret:", secret)
            return decryptValue;
        }
    }
)
