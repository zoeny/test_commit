# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/29 15:35
@month : 六月
@Author : mhm
@FileName: 1、矩阵的最小路径和.py
@Software: PyCharm
'''
'''
给定一个包含非负整数的 m x n 网格，
请找出一条从左上角到右下角的路径，
使得路径上的数字总和为最小

说明：每次只能向下或者向右移动一步。

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小
'''
def minPathSum(grid):# 我参照别人写的，错了
    if not grid:
        return 0
    curr = [[]]
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == j ==0:
                curr[i][j] = grid[0][0]
            if i== 0 and j != 0:
                curr[i][j] = grid[i][j]+curr[i][j-1]
            if j == 0 and i != 0:
                curr[i][j] = grid[i][j]+curr[i-1][j]
            else:
                curr[i][j] = grid[i][j]+min(curr[i][j-1],curr[i-1][j])
    for x in curr:
        sum += x
    return sum

def min(grid):
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[0][0] = grid[0][0]
            elif i == 0:
                dp[i][j] = grid[i][j] + dp[i][j - 1]
            elif j == 0:
                dp[i][j] = grid[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[m - 1][n - 1]

print(min([[1,3,1],
 [1,5,1],
 [4,2,1]]))









