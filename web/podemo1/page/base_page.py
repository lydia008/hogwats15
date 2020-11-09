#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/11/9 14:02
# Author：Lydia
"""
base_page 解决driver 传递的问题
"""
# 基类: 最基本的方法, driver实例化, find() 等
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    driver: WebDriver
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        # 第一次初始化
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        else:
            # 进行页面跳转的操作
            self.driver = driver
        # base_url 打开某个页面
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
