# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 19:48
@month : 六月
@Author : mhm
@FileName: 3、投飞镖刺破气球.py
@Software: PyCharm
'''
'''
题目描述：气球在一个水平数轴上摆放，可以重叠，飞镖垂直投向坐标轴，使得路径上的气球都被刺破。求解最小的投飞镖次数使所有气球都被刺破。
也是计算不重叠的区间个数，不过和 Non-overlapping Intervals 的区别在于，[1, 2] 和 [2, 3] 在本题中算是重叠区间。
'''
'''
思路：
这个题是贪心算法的题目，看到这种问区间重叠情况的，一般都能想到是贪心。我们把所有的区间按照右边界进行排序，
因为每个气球都要被打破，因此排序得到的第一组数据我们一定要使用。可以想到，
只要沿着该数据最右边界的位置进行射箭一定能打破尽可能多的气球。然后依次移动射箭的位置，进行统计即可。
'''
class Solution(object):
    def findMinArrowShots(self,points):
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        curr_pos = points[0][1]
        ans = 1
        for i in range(len(points)):
            if curr_pos >= points[i][0]:
                continue
            curr_pos = points[i][1]
            ans += 1
        return ans






