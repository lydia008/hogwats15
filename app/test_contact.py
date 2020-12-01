#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/11/16 23:53
# Author：Lydia
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWX:
    def setup(self):
        # 定义字典
        caps = {
            "platformName": "Android",
            "deviceName": "wework",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            # noReset 保留缓存， 比如登录状态
            "noReset": "True",
            # 不停止应用，直接运行测试用例
            # "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "skipServerInstallation": "true"
            # "settings[waitForIdleTimeout]": 0
        }

        # 本机ip:server端口; 建立客户端和服务端连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        name = 'lydia001'
        gender = '女'
        phonenum = '13800012301'
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 滚动查找【添加成员】
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 设置【用户名】【性别】【手机号】
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and contains(@class, 'TextView')]/..//*[@text='手机号']").send_keys(
            phonenum)
        # 点击【保存】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        sleep(2)
        print(self.driver.page_source)
        # 验证 添加成功 toast
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "添加成功" == result
