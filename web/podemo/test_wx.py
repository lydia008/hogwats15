#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/25 14:45
# Author：Lydia
from web.podemo.index_page import IndexPage


class TestWX:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        # 链式调用
        # assert self.index.goto_login().goto_register().register()
        #  assert True == self.index.goto_register().register()
        assert self.index.goto_register().register()
