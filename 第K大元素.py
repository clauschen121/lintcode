#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 17:20:06
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121

# 方法一：首先去重，然后对数组进行排序，但是答案是没有去重这一步，应该是理解问题


def kthLargestElement(k, A):
    L = list(set(A))
    L = sorted(L, reverse=True)
    return L[k - 1]
