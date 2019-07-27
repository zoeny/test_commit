# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 9:22
@month : 六月
@Author : mhm
@FileName: 4、翻转树.py
@Software: PyCharm
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self,root):
        if root is None:
            return root
        else:
            root.right,root.left = self.invertTree(root.left),self.invertTree(root.right)
        return root









