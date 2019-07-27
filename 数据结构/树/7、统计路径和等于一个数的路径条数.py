# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 16:53
@month : 六月
@Author : mhm
@FileName: 7、统计路径和等于一个数的路径条数.py
@Software: PyCharm
'''
'''
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
路径不一定以 root 开头，也不一定以 leaf 结尾，但是必须连续。
'''
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathForm(self,root,val):
        if root == None:
            return 0
        return 1 if root.val == val else 0 + self.pathForm(root.left, val - root.val) + self.pathForm(root.right, val - root.val)

    def pathSum(self,root,sum):
        if root == None:
            return 0
        else:
            return self.pathForm(root,sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)










