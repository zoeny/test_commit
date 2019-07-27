# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 17:07
@month : 六月
@Author : mhm
@FileName: 8、子树.py
@Software: PyCharm
'''
'''
Given tree s:
     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
例子2：
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:
   4
  / \
 1   2

Return false.
输入两颗二叉树A，B，判断B是不是A的子结构。
说明：
约定空树不是任意一个树的子结构。
'''
class Solution:
    def isSameTree(self,p,q): # 判断两棵树是否想等
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

    def isSubtree(self,s,t):
        if not s or not t:
            return False
        # 借助队列来实现树的层次遍历
        queue = [s]
        while queue:
            temp = queue.pop(0)
            # 访问每个树节点，看当前节点及子孙是否满足要求
            flag = self.isSameTree(temp,t)
            if flag:
                return True
            else:
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return False














