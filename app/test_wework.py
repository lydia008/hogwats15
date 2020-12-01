#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/11/4 0:38
# Author：Lydia
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:

    def setup_class(self):
        # 定义字典
        caps = {
            "platformName": "Android",
            "deviceName": "wework",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            # noReset 保留缓存， 比如登录状态
            "noReset": "True",
            # 不停止应用，直接运行测试用例
            "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "skipServerInstallation": "true"
            # "settings[waitForIdleTimeout]": 0
        }

        # 本机ip:server端口; 建立客户端和服务端连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()

    def test_a(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()

    # 外出打卡
    def test_case01(self):
        # 点击工作台
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滑动找到[打卡]
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # setting
        self.driver.update_settings({"waitForIdleTimeout": 0})
        # 点击外出打卡
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 点击打卡
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # sleep(3)
        # assert "外出打卡成功" in self.driver.page_source
        # 显示等待
        WebDriverWait(self.driver, 10).until(lambda x: ("外出打卡成功" in x.page_source))

    def teardown_class(self):
        self.driver.quit()
