#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/11/4 0:38
# Author：Lydia

from appium import webdriver


class TestWework:

    def setup(self):
        # 定义字典
        caps = {
            "platformName": "Android",
            "deviceName": "wework",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "True"
        }

        # 本机ip:server端口
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
        el1.click()
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        el2.click()
