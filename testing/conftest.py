#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/31 18:47
# Author：Lydia
from typing import List

import pytest


# @pytest.fixture()
# def login():
#     # setup 操作
#     print("登录操作")
#     # yield 相当于return 操作
#     yield ['tom', '123456']
#     # teardown 操作
#     print("登出操作")

# login param 用法
@pytest.fixture(scope="function", params=['tom', 'lydia'])
def login(request):
    # setup 操作
    print("登录操作")
    username = request.param
    # yield 相当于return 操作
    yield username
    # teardown 操作
    print("登出操作")


@pytest.fixture(scope='session', autouse=True)
def conn_db():
    print("完成 数据库连接")
    yield "database"
    print("关闭 数据库连接")


# 中文转换
# pytest test_calc.py -m div -vs 执行打div标签的用例
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(type(items))
    # 调整执行顺序
    items.reverse
    # 调整编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # 加入标签
        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item._nodeid:
            item.add_marker(pytest.mark.div)
