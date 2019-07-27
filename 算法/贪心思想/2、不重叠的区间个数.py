# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 19:37
@month : 六月
@Author : mhm
@FileName: 2、不重叠的区间个数.py
@Software: PyCharm
'''
# 题目描述：计算让一组区间不重叠所需要移除的区间个数。
'''
提示：
先计算最多能组成的不重叠区间个数，然后用区间总个数减去不重叠区间的个数。
在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，那么后面能够选择的区间个数也就越大。
按区间的结尾进行排序，每次选择结尾最小，并且和前一个区间不重叠的区间。
'''
class Interval(object):
    def __init__(self,s=0,e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self,intervals):
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start)
        last = 0
        res = 0
        for i in range(1,len(intervals)):
            if intervals[last].end > intervals[i].start:
                if intervals[i].end < intervals[last].end:
                    last = i
                res += 1
            else:
                last = i
        return res

















