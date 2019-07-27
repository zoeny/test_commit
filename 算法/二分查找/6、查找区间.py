# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/26 9:37
@month : 六月
@Author : mhm
@FileName: 6、查找区间.py
@Software: PyCharm
'''
'''
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
# 二分法
def searchRange(nums, target):
    if target not in nums:
        return [-1,-1]
    l,h = 0,len(nums)-1
    while l<=h and l>=0 and h<=len(nums)-1:
        m = (h+l)//2
        if nums[m] == target:
            l = m
            h = m
            while l>0 and nums[l-1] == nums[l]:
                l = l - 1
            while h<len(nums)-1 and nums[h] == nums[h+1]:
                h = h+1
            return [l,h]
        else:
            if nums[m]>target:
                h = m-1
            else:
                l = l+1

print(searchRange([5,7,7,8,8,10],8))











