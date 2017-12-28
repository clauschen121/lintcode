#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 17:38:14
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


def mergeSortedArray(A, B):
    return sorted(A + B)

A = [1]
B = [1]
print(mergeSortedArray(A, B))
