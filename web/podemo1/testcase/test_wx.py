#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 15:18
# Author：Lydia
from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "monica32"
        account = "monica32"
        phonenum = "13900012332"
        position = "工程师"
        mail = "test32@qq.com"
        # assert self.main.goto_AddMember().add_member()
        addmember = self.main.goto_AddMember()
        addmember.add_member(username, account, phonenum, position, mail)
        assert username in addmember.get_member(username)
