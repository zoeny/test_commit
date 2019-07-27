# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 17:34
@month : 六月
@Author : mhm
@FileName: 1、找到倒数第k个的元素.py
@Software: PyCharm
'''
# 排序 ：时间复杂度 O(NlogN)，空间复杂度 O(1)
def findKthLargest(nums,k):
    nums.sort()
    return nums[len(nums)-k]

print(findKthLargest([3,2,1,5,6,4],2))

# 快速选择
class Solution(object):
    def findKthLargest(self,nums,k):
        low,high = 0,len(nums) -1
        while low <= high:
            pivot = self.partition(nums,low,high)
            if pivot == k-1:
                return nums[pivot]
            if pivot < k-1:
                low = pivot+1
            else:
                high = pivot - 1

    def partition(self,nums,low,high):
        pivot_value = nums[high]
        index = low
        for i in range(low,high):
            if nums[i] >= pivot_value:
                nums[i],nums[index] = nums[index],nums[i]
                index += 1
        nums[index],nums[high] = nums[high],nums[index]
        return index











