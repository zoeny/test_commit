# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/18 12:36
@month : 六月
@Author : mhm
@FileName: 1、有序数组的TWO SUM.py
@Software: PyCharm
'''

'''双指针主要用于遍历数组，两个指针指向不同的元素，从而协同完成任务。'''
# 题目描述：在有序数组中找出两个数，使它们的和为 target。
'''
分析：使用双指针，一个指针指向值较小的元素，一个指针指向值较大的元素。指向较小元素的指针从头向尾遍历，指向较大元素的指针从尾向头遍历。
如果两个指针指向元素的和 sum == target，那么得到要求的结果；
如果 sum > target，移动较大的元素，使 sum 变小一些；
如果 sum < target，移动较小的元素，使 sum 变大一些。
'''
def two_Sum(num,target):
    i,j = 0,len(num)-1
    while i<j:
        sum = num[i]+num[j]
        if sum == target:
            return [num[i],num[j]]
        elif sum < target:
            i += 1
        else:
            j -= 1
# print(two_Sum([2,4,6,8,3],9))





