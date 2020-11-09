#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 15:14
# Author：Lydia
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.podemo1.page.add_member_page import AddMembersPage


class MainPage:
    # 复用浏览器
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def add_member(self):
        pass

    # 添加联系人
    def goto_AddMember(self):
        # click addmember
        # 点击【首页】，添加联系人
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # 点击【通讯录】
        self.driver.find_element(By.ID, "menu_contacts").click()
        # 第二种定位ID写法用CSS_SELECTOR/#
        # self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        sleep(2)
        # 点击【添加成员】按钮
        self.driver.find_element(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()

        return AddMembersPage(self.driver)
