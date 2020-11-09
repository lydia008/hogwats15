#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 15:14
# Author：Lydia
from time import sleep
from selenium.webdriver.common.by import By

from web.podemo1.page.base_page import BasePage


class AddMembersPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    # 添加联系人
    def add_member(self, username, account, phonenum, position, mail):
        # username = "monica05"
        # account = "monica05"
        # phonenum = "13900012305"
        # position = "工程师"
        # mail = "test5@qq.com"
        sleep(3)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(account)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.driver.find_element(By.ID, "memberAdd_title").send_keys(position)
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys(mail)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(2)
        return True

    def get_member(self):
        # 验证联系人添加成功
        contactlist = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

        # 方法一：遍历
        # titlelist = []
        # for element in contactlist:
        #     titlelist.append(element.get_attribute("title"))

        # 方法二：列表推导式
        titlelist = [element.get_attribute("title") for element in contactlist]
        return titlelist
