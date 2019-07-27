# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 9:14
@month : 六月
@Author : mhm
@FileName: 3、计算两节点的最长路径.py
@Software: PyCharm
'''
'''
Input:

         1
        / \
       2  3
      / \
     4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
'''
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self,root):
        self.temp = 0
        def depth(p):
            if not p:
                return 0
            left,right = depth(p.left),depth(p.right)
            self.temp = max(self.temp,left+right)
            return 1+max(left,right)
        depth(root)
        return self.temp














