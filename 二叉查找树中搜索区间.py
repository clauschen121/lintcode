#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-28 21:29:44
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


class Solution:
    """
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        if not root:
            return []
        L = []

        def findtn(root, k1, k2):
            if not root:
                return
            if root.val <= k2 and root.val >= k1:
                L.append(root.val)
            findtn(root.left, k1, k2)
            findtn(root.right, k1, k2)
        findtn(root, k1, k2)
        return sorted(L)
