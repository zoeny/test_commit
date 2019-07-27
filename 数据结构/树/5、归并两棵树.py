# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 11:17
@month : 六月
@Author : mhm
@FileName: 5、归并两棵树.py
@Software: PyCharm
'''
'''
合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。

思路：
考虑当两个结点合并时，如果这两个结点都存在，
那么直接值相加，如果有一个不存在，直接返回另一个就好了。
'''
def TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self,t1,t2):
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1













