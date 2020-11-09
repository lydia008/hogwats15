#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 15:18
# Author：Lydia
from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "monica06"
        account = "monica06"
        phonenum = "13900012306"
        position = "工程师"
        mail = "test6@qq.com"
        # assert self.main.goto_AddMember().add_member()
        addmenber = self.main.goto_AddMember()
        addmenber.add_member(username, account, phonenum, position, mail)
        assert username in addmenber.get_member()
