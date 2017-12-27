#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 17:53:19
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121
from functools import reduce


# def digitCounts1(k, n):
#     # 先得到一个关于n的list
#     L1 = list(range(n + 1))
#     # 把数字转化为字符串
#     L2 = map(str, L1)
#     # 把'11','123'这类字符串转化为('1','1')('1','2','3')这样的字符串
#     L3 = map(list, L2)
#     # 把L3里面的字符串合并起来得到一个拆分后的list
#     L4 = reduce((lambda x, y: x + y), L3)
#     # 获取L4里面所有与k相等的字符串，并保留,其余的过滤掉
#     L5 = list(filter(lambda x: x == str(k), L4))
#     return len(L5)
# print(digitCounts1(0, 201))

# str = '201'
# z = 0
# num = 0
# lenth = len(str) - 1

# for k, v in enumerate(str):
#     if int(v) > num:
#         if k == 0:
#             z = z + pow(10, lenth - int(k))
#         else:
#             z = z + (int(str[:k]) + 1) * pow(10, lenth - int(k))
#     elif int(v) == num:
#         if k == 0:
#             z = z + int(str[(k + 1):]) + 1
#         elif k == lenth:
#             z = z + 1 + (int(str[:k]) + 0) * pow(10, lenth - int(k))
#         else:
#             z = z + int(str[(k + 1):]) + 1 + \
#                 (int(str[:k]) + 0) * pow(10, lenth - int(k))
#     else:
#         if k == 0:
#             z = z
#         else:
#             z = z + (int(str[:k]) + 0) * pow(10, lenth - int(k))
# if num == 0:
#     for i in range(1, lenth + 1):
#         z = z - pow(10, i)
print('耗时')
