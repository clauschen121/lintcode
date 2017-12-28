#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 21:50:54
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        result = []
        def serializeTree(root):
        	if root:
        		result.append(str(root.val))
        		serializeTree(root.left)
        		serializeTree(root.right)
        	else:
        		result.append('#')
        serializeTree(root)
        return ','.join(result)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
		L = data.split(',')
		