# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/21 15:19
@month : 六月
@Author : mhm
@FileName: 1、树的高度.py
@Software: PyCharm
'''
# 用递归实现
# 一棵树要么是空树，要么有两个指针，每个指针指向一棵树。树是一种递归结构，很多树的问题可以使用递归来处理。
def maxDeepth(self,root):
    if root == None:
        return 0
    leftDepth = self.maxDepth(root.left)
    rightDepth = self.maxDepth(root.right)
    return max(leftDepth,rightDepth)+1







