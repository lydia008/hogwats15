#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 13:24
# Author：Lydia
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 复用浏览器，chrome debugger模式
class TestDemo:
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://www.baidu.com")
        sleep(3)

    def test_weixin(self):
        self.driver.find_element(By.ID, 'menu_contacts').click()
        sleep(3)
