#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/31 19:15
# Author：Lydia
import pytest


@pytest.fixture(autouse=True)
def conn_db():
    print("完成 数据库连接aaa")
    yield "database"
    print("关闭 数据库连接aaa")
