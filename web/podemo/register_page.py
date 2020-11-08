#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 14:39
# Author：Lydia
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    # 传入index_page页面driver
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 注册信息
    def register_success(self):
        self.driver.find_element(By.ID, "corp_name").send_keys("Company01")
        self.driver.find_element(By.ID, "manager_name").send_keys("lydia01")
        self.driver.find_element(By.ID, "register_tel").send_keys("13900000001")
        self.driver.find_element(By.ID, "submit_btn").click()
        return True

    def register_fail(self):
        self.driver.find_element(By.ID, "corp_name").send_keys("Company01")
        self.driver.find_element(By.ID, "manager_name").send_keys("lydia01")
        self.driver.find_element(By.ID, "register_tel").send_keys("1391")
        self.driver.find_element(By.ID, "submit_btn").click()
        return True
