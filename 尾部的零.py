#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 16:45:33
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


# 设计一个算法，计算出n阶乘中尾部零的个数
# 样例
# 11! = 39916800，因此应该返回 2


def trailingZeros(n):
    # write your code here, try to do it without arithmetic operators.
    # 主要是计算5的个数，如果遇到25,75,125这种，还要考虑5*5*n或者5*5*5*n的2n或者3n的值，可以通过while循环记录下来
    y = x = n // 5
    z = 0
    while x >= 5:
        x = x // 5
        z = x + z
    return y + z

# 如果使用原始阶乘的定义方式去计算，当阶乘稍微大点，就会非常耗时
