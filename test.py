#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 17:53:19
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


def serialize(root):
    # write your code here
    L = 'a'.join([str(i) for i in root])
    return L


def deserialize(data):
	L = data.split('a')
	return L

d1 = [1, 2, 3, '#', 5, 1, 5]

data = serialize(d1)
print(deserialize(data))
