#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date ：2020/10/17 17:09
# Author：Lydia

import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    # 资源准备
    def setup_class(self):
        print("计算开始")
        # 实例化被测类
        self.calc = Calculator()

    # 资源销毁
    def teardown_class(self):
        print("计算结束")

    # 加法
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-1, -1, -2],
        [1, 0, 1]
    ], ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    # 减法
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 0], [200, 100, 100], [0.2, 0.1, 0.1], [-1, -1, 0], [0, 0, 0]
    ], ids=['int_case', 'bignum_case', 'float_case', 'Minus_case', 'zero_case'])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    # 乘法
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [200, 100, 20000], [0.2, 1, 0.2], [-1, -1, 1], [0, 0, 0]
    ], ids=['int_case', 'bignum_case', 'float_case', 'Minus_case', 'zero_case'])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    # 除法
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [200, 100, 2], [0.2, 1, 0.2], [-1, -1, 1], [5, 0, '除数不能为0']
    ], ids=['int_case', 'bignum_case', 'float_case', 'Minus_case', 'zero_case'])
    def test_div(self, a, b, expect):
        if b == 0:
            print("除数不能为0！")
        else:
            result = self.calc.div(a, b)
            assert result == expect


if __name__ == '__main__':
    pytest.main(['test_calc.py'])
