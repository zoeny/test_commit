# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 16:42
@month : 六月
@Author : mhm
@FileName: 6、判断路径和是否等于一个数.py
@Software: PyCharm
'''
'''
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
'''
思路：两种方法
1、计算从根节点到每个叶子节点路径上的元素之和组成列表，判断目标值是否在列表中
2、由上到下递归地判断从根节点到叶子节点路径上元素之和是否等于目标值
'''
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self,root,sum): # 我写的，不知道对不对
        res = []
        left = root.val
        right = root.val
        while root.left:
            left += root.left.val
        while root.right:
            right += root.right.val
        res.append(left)
        res.append(right)
        if sum in res:
            return True
        else:
            return False

class Solution1(object):
    def hasPathSum(self,root,sum):
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)








