#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-28 20:36:02
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


def fizzBuzz(n):
    # write your code here
    L = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            L.append('fizz buzz')
        elif i % 3 == 0:
            L.append('fizz')
        elif i % 5 == 0:
            L.append('buzz')
        else:
            L.append(str(i))
    return L

print(fizzBuzz(6))
