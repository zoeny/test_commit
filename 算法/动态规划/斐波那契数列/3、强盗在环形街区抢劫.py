# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 11:00
@month : 六月
@Author : mhm
@FileName: 3、强盗在环形街区抢劫.py
@Software: PyCharm
'''
'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），
然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

思路
如果数量小于3个，那么只能偷一个，选最大的即可
对于其他情况，偷不偷第一个和最后一个房子只有3种可能，因为是个圈，
偷了第一个，第二个房子和最后一个房子不能偷，nums[2:-1]随意偷
偷了最后一个，倒数第二个房子和第一个房子不能偷，nums[1:-2]随意偷
两个都没偷 ，nums[1:-1]随意偷

计算3种情况的最大值，选出最大的那个
对于以上3种情况，因为有些地方不能偷，所以圈被不能偷的地方切成了线
对于线的情况，用动态规划即可
dp[i]储存偷了第i个房子时能偷到的最高金额，因为不能偷相邻的，所以只有两种情况，
1，偷了第i和i-2个，不能偷第i-1个
2，偷了第i和i-3个，不能偷第i-1个和第i-2个
'''
def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums)<= 3:
        return max(nums)
    a = nums[0]+f(nums[2:-1])
    b = nums[-1]+f.nums[1:-2]
    c = f(nums[1:-1])
    return max(a,b,c)

def f(nums):
    dp = [0]*len(nums)
    if len(nums)<=2:
        return max(nums)
    dp[2] = nums[2]+nums[0]
    dp[1] = nums[1]
    dp[0] = nums[0]
    for i in range(3,len(nums)):
        dp[i] = nums[i]+max(dp[i-2],dp[i-3])
    return max(dp[-1],dp[-2])

# 方法2
'''
这道题是在打家劫舍那道题的基础上添加了增加了限定条件，也就是把房屋连成一个圈，不能同时打劫第一个和最后一个，那么就可以分别求出，没有第一个房子时能偷到的金额最大值，
和没有最后一个房子时能偷到的最大值。比较这两个中间较大的一个，即可。
'''
def rob2(nums):
    def sub_rob(nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[len(nums)-1]
    n = len(nums)
    if n<0:
        return 0
    if n<=2:
        return max(nums)
    return max(sub_rob(nums[1:]),sub_rob(nums[:-1]))







