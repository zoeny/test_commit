# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/26 9:11
@month : 六月
@Author : mhm
@FileName: 5、寻找旋转数组的最小数字.py
@Software: PyCharm
'''
'''
Input: [3,4,5,1,2],
Output: 1
'''

def findMin(nums):
    target = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < target:
            target = nums[i]
        else:
            continue
    return target

print(findMin([4,5,6,7,0,1,2]))

# 二分法
def findMin1(nums):
    l,h = 0,len(nums)-1
    while l<h:
        m = l+(h-l)//2
        if nums[m] <= nums[h]:
            h = m
        else:
            l = m+1
    return nums[l]

print(findMin1([4,5,6,7,0,1,2]))

# 二分查找2（针对有序数组）
def findMin2(nums):
    size = len(nums)
    if size == 1:
        return nums[0]
    if size == 2:
        return min(nums[0],nums[1])
    mid = size // 2
    if nums[mid-1] > nums[mid]: # 有序数组
        return nums[mid]
    if nums[mid]<nums[-1]:
        return findMin2(nums[:mid+1])
    return findMin2(nums[mid:])

a = [4,5,6,7,0,1,2]
print(a[3]<a[-1])









