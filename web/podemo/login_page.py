#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 14:34
# Author：Lydia
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo.register_page import RegisterPage


class LoginPage:
    # driver 是由index_page 传入; 并指定driver类型(import) remote
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 扫码
    def scan(self):
        pass

    # 进入到注册页面
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return RegisterPage(self.driver)
