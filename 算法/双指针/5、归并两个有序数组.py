# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/18 15:50
@month : 六月
@Author : mhm
@FileName: 5、归并两个有序数组.py
@Software: PyCharm
'''
# 题目描述：把归并结果存到第一个数组上
# 需要从尾开始遍历，否则在 nums1 上归并得到的值会覆盖还未进行归并比较的值。
'''
eg:Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
'''
def merge(num1,num2):
    m,n = len(num1)-1,len(num2)-1
    while n < m and n >= 0:
        if num2[n] > num1[m]:
            num1[m] = num2[n]
            m -= 1
            n -= 1
    num1.sort()
    return num1
print(merge([1,2,3,0,0,0],[2,5,6]))

def merge1(nums1,m,nums2,n):
    index1,index2 = m - 1,n-1
    indexmerge = m+n-1
    while index1>=0 or index2 >= 0:
        if index1 < 0:
            nums1[indexmerge] = nums2[index2]
            indexmerge -= 1
            index2 -= 1
        elif index2 < 0:
            nums1[indexmerge] = nums1[index1]
            index1 -= 1
            indexmerge -= 1
        elif nums1[index1] > nums2[index2]:
            nums1[indexmerge] = nums1[index1]
            index1 -= 1
            indexmerge -= 1
        else:
            nums1[indexmerge] = nums2[index2]
            index2 -= 1
            indexmerge -= 1
    return nums1

print(merge1([1,2,3,0,0,0],3,[2,5,6],3))












