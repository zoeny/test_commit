# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/24 10:22
@month : 六月
@Author : mhm
@FileName: 4、荷兰国旗问题.py
@Software: PyCharm
'''
'''
问题描述：
荷兰国旗包含三种颜色：红、白、蓝。
有三种颜色的球，算法的目标是将这三种球按颜色顺序正确地排列。
它其实是三向切分快速排序的一种变种，在三向切分快速排序中，
每次切分都将数组分成三个区间：
小于切分元素、等于切分元素、大于切分元素，而该算法是将数组分成三个区间：
等于红色、等于白色、等于蓝色。

只有0、1、2三种颜色
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

'''
思路: 
1）首先找出数组中的最小值的索引，然后将最小值与第一个元素交换位置。 
2）设置三个变量，一个是j表示当前指针，l表示当前还需遍历的长度，
k表示k之前的所有元素都为0.从第一个元素开始循环遍历，遇到2，则pop(j),
然后在尾部插入2，l–，遇到0则与索引值为k的元素交换。 
保证2永远在尾部，0永远在头部，1无需任何操作。

'''
# class Solution:
def sortCount(nums):
    l = len(nums)
    index = 0
    for i in range(1,l):
        if nums[i] < nums[index]:
            index = i
    nums[0],nums[index] = nums[index],nums[0]
    k = j = 1
    while j<l:
        if nums[j] == 2:
            nums.pop(j)
            nums.append(2)
            l -= 1
        elif nums[j] == 0:
            nums[k],nums[j] = nums[j],nums[k]
            k += 1
            j += 1
        else:
            j += 1
    return nums

# 方法二
def sortColors(nums):
    first,second,last = 0,0,len(nums)-1
    while second <= last:
        if nums[second] == 0:
            nums[first],nums[second] = nums[second],nums[first]
            first += 1
            second += 1
        elif nums[second] == 1:
            second += 1
        else:
            nums[last],nums[second] = nums[second],nums[last]
            last -= 1
    return nums


























