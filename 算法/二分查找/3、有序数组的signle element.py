# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/25 9:21
@month : 六月
@Author : mhm
@FileName: 3、有序数组的signle element.py
@Software: PyCharm
'''
'''
题目描述：一个有序数组只有一个数不出现两次，找出这个数。
要求以 O(logN) 时间复杂度进行求解，因此不能遍历数组并进行异或操作来求解，这么做的时间复杂度为 O(N)。
Input: [1, 1, 2, 3, 3, 4, 4, 8, 8]
Output: 2
'''
# 二分查找
def singleNonDuplicate(nums):
    l,h = 0,len(nums)-1
    while l<h:
        m = l+(h-l)//2
        if m % 2 == 1:
            m -= 1 # 保证 l/h/m 都在偶数位，使得查找区间大小一直都是奇数
        if nums[m] == nums[m+1]:
            l = m+2
        else:
            h = m
    return nums[l]

# 异或
def singleNonDuplicate1(nums):
    i = 0
    for num in nums:
        i ^= num
    return i
print(singleNonDuplicate1([1,1,2,3,3,4,4,8,8]))


