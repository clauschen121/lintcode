#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 13:27:03
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121

# 方法一：做一个list L存放所有丑数，一个temp不断自增，在自增中查看被2,3,5整除后的余数
# 如果被符合条件，则增加该temp到数组L中，该方法过于耗时


def nthUglyNumber1(n):
    L = [1]
    temp = 2
    while len(L) < n:
        x = temp
        while x % 2 == 0:
            x = x / 2
        while x % 3 == 0:
            x = x / 3
        while x % 5 == 0:
            x = x / 5
        if x == 1:
            L.append(temp)
        temp += 1
    print(L)
    return L[n - 1]


# 方法二：参考了网上的方法，首先定义一个list L，初始值为1，再定义一个list的引脚下标，p2，p3，p5，初始为0
# 接着往list里添加元素，后面添加的最小数必然是list里之前某个元素的2,3,5倍，同时，为了避免重复添加，需要在
# 判断为某元素的x倍后，把引脚下标后移，这里要注意用if而不是elif，避免像6,12这类数重复添加
def nthUglyNumber2(n):
    L = [1]
    p2, p3, p5 = 0, 0, 0
    while len(L) < n:
        n2, n3, n5 = L[p2] * 2, L[p3] * 3, L[p5] * 5
        temp = min(n2, n3, n5)
        L.append(temp)
        if temp == n2:
            p2 += 1
        if temp == n3:
            p3 += 1
        if temp == n5:
            p5 += 1
    return L[n - 1]
