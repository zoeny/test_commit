# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 10:11
@month : 六月
@Author : mhm
@FileName: 2、强盗抢劫（198）.py
@Software: PyCharm
'''
'''
题目描述：抢劫一排住户，但是不能抢邻近的住户，求最大抢劫量。
定义 dp 数组用来存储最大的抢劫量，其中 dp[i] 表示抢到第 i 个住户时的最大抢劫量。
由于不能抢劫邻近住户，如果抢劫了第 i -1 个住户，那么就不能再抢劫第 i 个住户，所以
dp[i] = max(dp[i-2]+nums[i],dp[i-1]

输入: [1,2,3,1] 
输出: 4 
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。 
偷窃到的最高金额 = 1 + 3 = 4 。 
输入: [2,7,9,3,1] 
输出: 12 
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。 
偷窃到的最高金额 = 2 + 9 + 1 = 12 。
'''
# 递归方法
def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    else:
        q = rob(nums[:-1])
        p = rob(nums[:-2])
        return max(q,p+nums[-1])

# 方法二：递推
def rob2(nums):
    r = {}
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        return max(nums)
    else:
        r[0] = nums[0]
        r[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            r[i] = max(r[i-1],r[i-2]+nums[i])
    return r[len(nums)-1]

# 动态规划
def rob3(nums):
    last,now = 0,0
    for i in nums:
        last, now = now, max(last + i, now)
    return now

print(rob3([2,7,9,3,1]))





