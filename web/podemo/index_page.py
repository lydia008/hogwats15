#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 14:29
# Author：Lydia
from selenium.webdriver.chrome import webdriver


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("")

    def goto_login(self):
        pass

    def goto_register(self):
        pass
