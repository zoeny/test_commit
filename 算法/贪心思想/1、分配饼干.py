# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 19:25
@month : 六月
@Author : mhm
@FileName: 1、分配饼干.py
@Software: PyCharm
'''
'''
例子：
输入: [1,2], [1,2,3]

输出: 2

解释:
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.

例子2：输入: [1,2,3], [1,1]

输出: 1

解释:
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。
'''
# 如果按顺序某个孩子可以被满足，那么就满足他，这里就是贪心的体现
class Solution:
    def findContentChildren(self,g,s):
        self.i,self.j = 0,0
        self.item = 0
        g.sort()
        s.sort()
        if (g != None and s != None and len(g) != 0 and len(s)!=0):
            for self.item in range(len(s)):
                if g[0] < s[self.item]:
                    self.i += 1
                    del g[0]
                if len(g) == 0:
                    break
            return self.i
        return 0

class Solution2(object):
    def findCountChildren(self,g,s):
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child















