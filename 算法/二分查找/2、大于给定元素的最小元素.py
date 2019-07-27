# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/25 9:06
@month : 六月
@Author : mhm
@FileName: 2、大于给定元素的最小元素.py
@Software: PyCharm
'''
'''
题目描述：给定一个有序的字符数组 letters 和
一个字符 target，要求找出 letters 中大于 target 的最小字符，如果找不到就返回第 1 个字符。

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
'''
# 二分查找
def nextGreatestLetter(letters, target):
    lo,hi = 0,len(letters)-1
    if target < letters[0] or target >= letters[-1]:
        return letters[0]
    while lo <= hi:
        mid = lo+(hi-lo)//2
        if letters[mid] <= target:
            lo = mid+1
        else:
            hi = mid-1
    return letters[lo]

# 线性扫描整个数组，如果遇到比target大的item就直接返回item，如果过程中没有遇到比target大的就说明应该返回letters[0]
def nextGreatestLetter1(letters, target):
    for letter in letters:
        if ord(letter)>ord(target):
            return letter
    return letters[0]
# ord()函数返回值是对应的十进制整数。




