#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/31 17:05
# Author：Lydia

# 使用装饰器，不可以使用yield 返回的参数值
# @pytest.mark.usefixtures("login")
# def test_case0():
#     # 返回调用的方法
#     print(login)
#     print("用例0")


# 使用fixture 函数名字传参，可以使用yield 值
import pytest


@pytest.mark.run(order=2)
def test_case1(login):
    print(login)
    print("用例1")


@pytest.mark.run(order=3)
def test_case2():
    print("用例2")


# fixture 传入的顺序是执行的顺序
@pytest.mark.run(order=1)
def test_case3(login, conn_db):
    print(conn_db)
    print("用例3")
