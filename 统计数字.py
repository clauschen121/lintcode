#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 17:16:32
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121
from functools import reduce

# 计算数字k在0到n中的出现的次数，k可能是0~9的一个值
# 样例
# 例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1,
# 10, 11, 12)


# 方法一：过于耗时，没有对list进行优化选择，同时用了较多的高阶函数，导致耗时很长
def digitCounts1(k, n):
    # 先得到一个关于n的list
    L1 = list(range(n + 1))
    # 把数字转化为字符串
    L2 = map(str, L1)
    # 把'11','123'这类字符串转化为('1','1')('1','2','3')这样的字符串
    L3 = map(list, L2)
    # 把L3里面的字符串合并起来得到一个拆分后的list
    L4 = reduce((lambda x, y: x + y), L3)
    # 获取L4里面所有与k相等的字符串，并保留,其余的过滤掉
    L5 = list(filter(lambda x: x == str(k), L4))
    return len(L5)

# 方法二：通过数学方法对比每一位上的数字和k的大小，再来判断会产生多少种组合可能，比如3在3253中出现的次数
# 首先和最高位比较，可能产生253+1种可能，然后和2对比，会额外产生3*100种可能，再和5对比，会产生（32+1）*10种可能
# 再和3对比，会产生（325+1）*1种可能，最后累加，还要考虑k=0的情况，需要减掉首位为0的情况。
# 该方法在运算复杂度上较优，无论n有多大，耗时不会太大


def digitCounts2(k, n):
    str1 = str(n)
    z = 0
    num = k
    lenth = len(str1) - 1

    for k, v in enumerate(str1):
        if int(v) > num:
            if k == 0:
                z = z + pow(10, lenth - int(k))
            else:
                z = z + (int(str1[:k]) + 1) * pow(10, lenth - int(k))
        elif int(v) == num:
            if k == 0 and k == lenth:
                z = 1
            elif k == 0:
                z = z + int(str1[(k + 1):]) + 1
            elif k == lenth:
                z = z + 1 + (int(str1[:k]) + 0) * pow(10, lenth - int(k))
            else:
                z = z + int(str1[(k + 1):]) + 1 + \
                    (int(str1[:k]) + 0) * pow(10, lenth - int(k))
        else:
            if k == 0:
                z = z
            else:
                z = z + (int(str1[:k]) + 0) * pow(10, lenth - int(k))
    if num == 0:
        for i in range(1, lenth + 1):
            z = z - pow(10, i)
    return z

# 网上找到的方法，原理同2方法类似，但是做了函数优化，耗时较少，但是没考虑k=0的情况


def digitCounts3(k, n):
    i = 1
    t = 10**i
    count = 0
    while int(n / (t / 10)):  # n不为0的情况
        num_cur = (n % t - n % (t / 10)) / (t / 10)
        if int(n / t) != 0 or (int(n / t) == 0 and k != 0):
            if k == num_cur:
                count += int(n / t) * (t / 10) + n % (t / 10) + 1
            elif k < num_cur:
                count += int(n / t) * (t / 10) + t / 10
            else:
                count += int(n / t) * (t / 10)
        else:  # k == 0且当前为最高位数字
            if i == 1:  # 最高位为个位
                count = 1
        i = i + 1
        t = 10**i
    if n == 0 and k == 0:
        count = 1
    return int(count)

# 网上找到的方法，原理同1方法类似，巧妙的运用了字符串拼接，然后再用count方法去找字符串里匹配的数字
# 对方法一做了极大的优化，但是由于还是拼接字符串，当n很大时，耗时明显高于方法二


def digitCounts4(k, n):
    L = ''.join([str(i) for i in range(n + 1)])
    c = L.count(str(k))
    return c
