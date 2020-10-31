#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/31 18:47
# Author：Lydia
import pytest


# @pytest.fixture(autouse=True, scope="function")
@pytest.fixture(scope="function")
def login():
    # setup 操作
    print("登录操作")
    # yield 相当于return 操作
    yield ['tom', '123456']
    # teardown 操作
    print("登出操作")


# @pytest.fixture(autouse=True)
@pytest.fixture()
def conn_db():
    print("完成 数据库连接")
    return "database"
