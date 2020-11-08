#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 14:29
# Author：Lydia
from selenium import webdriver
from selenium.webdriver.common.by import By

from web.podemo.login_page import LoginPage
from web.podemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    # 进入登录页面
    def goto_login(self):
        # click 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return login_page 页面
        return LoginPage(self.driver)

    # 注册页面
    def goto_register(self):
        # click signup
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn")
        return RegisterPage(self.driver)
