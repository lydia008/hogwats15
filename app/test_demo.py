#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/11/3 0:00
# Author：Lydia
from appium import webdriver

desire_cap = {
    "platformName": "android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    # 设置为True 后第一次关闭弹框后，后台将记住不再提示
    "noReset": True
}

# 固定连接
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
# 隐式等待
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el3.click()
