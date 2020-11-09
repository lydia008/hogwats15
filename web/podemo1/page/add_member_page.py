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
        # sleep(3)
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.ID, "memberAdd_title").send_keys(position)
        self.find(By.ID, "memberAdd_mail").send_keys(mail)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # sleep(2)
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)
        return True

    def get_member(self, value):
        # # 验证联系人添加成功
        # contactlist = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        #
        # # 方法一：遍历
        # # titlelist = []
        # # for element in contactlist:
        # #     titlelist.append(element.get_attribute("title"))
        #
        # # 方法二：列表推导式
        # titlelist = [element.get_attribute("title") for element in contactlist]
        # print(titlelist)

        # 处理翻页问题
        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            if value in titlelist:
                return titlelist
            total_list = total_list + titlelist
            # 获取翻页
            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split("/", 1)
            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
        return total_list
