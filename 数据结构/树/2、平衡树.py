# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 9:06
@month : 六月
@Author : mhm
@FileName: 2、平衡树.py
@Software: PyCharm
'''
# 平衡树左右子树高度差都小于等于 1
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self,root):
        if root == None:
            return True
        elif abs(self.height(root.left) - self.hight(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

def height(self,root):
    if root == None:
        return 0
    else:
        return max(self.height(root.left),self.height(root.right))+1













