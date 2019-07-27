# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/29 14:08
@month : 六月
@Author : mhm
@FileName: 6、循环数组中比当前元素大的下一个元素.py
@Software: PyCharm
'''
'''
找出一个数组中每个数字的下一个更大的数字，可以看做是循环数组。

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，
这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
'''
def nextGreat(nums):
    if not nums:
        return nums
    max_element = max(nums)
    stack = list()
    res = [-1 for i in range(len(nums))]

    for i, x in enumerate(nums):

        if not stack or nums[stack[-1]] >= x:
            stack.append(i)
        else:
            # print stack, res
            while (stack and nums[stack[-1]] < x):
                res[stack[-1]] = x
                stack.pop()
            if x != max_element:  # 最大的不用放进栈，直接默认-1就好
                stack.append(i)

    # print stack, res
    if stack:  # 还有需要循环搜索的元素
        for i, x in enumerate(nums):
            if not stack:
                break
            while stack and x > nums[stack[-1]]:
                res[stack[-1]] = x
                stack.pop()
    return res


# 方法二
def nextGreat1(nums):
    _len = len(nums)
    res = [-1]*_len
    for i in range(_len):
        for j in range(i+1,_len*2):
            if nums[j%_len] > nums[i]:
                res[i] = nums[j%_len]
                break
    return res

# 方法三：单调递减栈
def nextGreat2(nums):
    res = [-1]*len(nums)
    stack = []
    for i in range(len(nums))*2:
        while stack and (nums[stack[-1]]<nums[i]):
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res

























