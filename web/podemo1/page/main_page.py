#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 15:14
# Author：Lydia
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.podemo1.page.add_member_page import AddMembersPage
from web.podemo1.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # # 复用浏览器
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # 添加联系人
    def goto_AddMember(self):
        # click addmember
        # 点击【首页】，添加联系人
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # 点击【通讯录】
        self.find(By.ID, "menu_contacts").click()
        # 第二种定位ID写法用CSS_SELECTOR/#
        # self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        # sleep(2)
        # 点击【添加成员】按钮
        # self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        # 显示等待
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")

        # element: WebElement = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # 显示等待
        # element = self.wait_for_click(locator)
        # element.click()

        # 解决添加操作员按钮无效问题
        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMembersPage(self.driver)
