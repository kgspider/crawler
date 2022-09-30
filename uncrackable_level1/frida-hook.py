# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2022-08-29
# @Author  : 微信公众号：K哥爬虫
# @FileName: frida-hook.py
# @Software: PyCharm
# ==================================


import sys
import frida


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


with open("./frida-hook.js", "r", encoding="utf-8") as fp:
    hook_string = fp.read()

# 方式一：attach 模式，已经启动的 APP
process = frida.get_usb_device(-1).attach("Uncrackable1")
script = process.create_script(hook_string)
script.on("message", on_message)
script.load()
sys.stdin.read()

# 方式二，spawn 模式，重启 APP
# device = frida.get_usb_device(-1)
# pid = device.spawn(["owasp.mstg.uncrackable1"])
# process = device.attach(pid)
# script = process.create_script(hook_string)
# script.on("message", on_message)
# script.load()
# device.resume(pid)
# sys.stdin.read()
