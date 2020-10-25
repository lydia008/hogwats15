#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 21:21
# Author：Lydia
"""
使用cookie 登录企业微信，完成导入联系人，加上断言验证
"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# shelve 数据库实现数据存储
class TestDemo:
    def setup_method(self, method):
        # options = Options()
        # options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    # shelve 方式实现登录
    def test_shelve(self):
        """
        数据存储成功后，windows电脑会生成3个cookies文件
        分别为：cookies.bak, cookies.dat, cookies.dir
        Mac电脑，生成1个文件：cookies.db
        cookie存储成功后，注释cookies,从数据库读取
        """
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853304123940'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'wMhdD3cvfBsLjqjULSsioNvCJDe7qs1oRxYxGfAyxiKiXlgTRXUaWPIbQ8czueQz'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a4095947'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324968162766'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853304123940'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1603637936, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '2e5caih'},
        #     {'domain': '.qq.com', 'expiry': 1603715461, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.788847587.1603606404'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1603628413'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '3697623621212132'},
        #     {'domain': '.qq.com', 'expiry': 1666701061, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1188152275.1603335017'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1666407027, 'httpOnly': False, 'name': '__utma', 'path': '/',
        #      'secure': False, 'value': '135912439.1188152275.1603335017.1603335017.1603335017.1'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634871017, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': '8Osue6FDKpXyqBBudvlSq0Fu6yBFVEzK2W3XyTg7IQVysM3_AC4NSHG-EPCUItakWx_oDcqWmeplZ32Wnfa_FkEjNX2lbAUo4YG6nrbeUS23QKHDUIAig40pEmiMvzYpuR_it8dFJEjjwqktTgOjQHt6OEHlclbveP15UnnoBR5CTDyUWLQLfJt-IYb0VnJyyvQ6LFRag7RnBEZHTKgn7CXzHMJFTyjHapBqJcoGPaqrW-ZPlxW_T0kFQCj5WZWsPKZJbL7FuIGbgCPxUDNh0Q'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634871027, 'httpOnly': False,
        #      'name': 'Hm_lvt_f2ba645ba13636ba52b0234381f51cbc', 'path': '/', 'secure': False, 'value': '1603335018'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1619103027, 'httpOnly': False, 'name': '__utmz', 'path': '/',
        #      'secure': False,
        #      'value': '135912439.1603335017.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635164413, 'httpOnly': False,
        #                           'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #                           'value': '1603335033,1603606404,1603628413'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1606221064, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'}]
        # shelve python 的内置模块，专门用来对数据的持久化存储的库，相当于小型的数据库
        # 可以通过key,value 把数据保存到shelve中
        # 打开数据库,读取cookie
        db = shelve.open("cookies")
        # db['cookie'] = cookies  # 数据存储后删除
        cookies = db['cookie']
        # 利用读取的cookie完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # 关闭数据库
        db.close()
        # 定位并点击”导入通讯录“按钮
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        # 定位上传按钮，上传文件用send_keys(),参数为文件的绝对路径
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            r"D:\Python\testdatas\mydatas.xlsx")
        # 验证上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert "mydatas.xlsx" == filename
        sleep(3)
        # 导入文件
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_submit').click()
        sleep(3)
        # 获取上传后的提示信息
        results = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_successImportText').text
        print(results)
        # 点击完成按钮
        btnname = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_successBtnWrap').text
        assert btnname == '完成'
        print("文件上传成功！")
