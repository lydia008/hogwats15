#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/28 10:36
# Author：Lydia
from appium import webdriver

# 设置caps的值
desire_cap = {
    # 默认是Android
    "platformName": "android",
    # adb devices的sn名称
    "deviceName": "127.0.0.1:7555",
    # 包名
    "appPackage": "com.xueqiu.android",
    # activity名字
    "appActivity": ".view.WelcomeActivityAlias"
}

# 运行appium，前提是要打开appium server
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
