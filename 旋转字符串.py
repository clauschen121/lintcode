#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-28 19:13:00
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


def rotateString(str, offset):
    # write your code here
    a1 = str[:len(str) - offset]
    a2 = str[len(str) - offset:]
    str = a2 + a1
    print(str)


def rotateString2(str, offset):
    if not offset:
        return
    if not str:
        return

    n = len(str)
    offset = offset % n

    for i in range(offset):
        t = str.pop()
        str.insert(0, t)
    print(str)


s = ['a', 'b', 'c', 'd', 'e', 'f']
rotateString(s, 4)
rotateString2(s, 4)
