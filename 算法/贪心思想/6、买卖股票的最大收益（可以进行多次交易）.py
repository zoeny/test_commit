# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/26 10:30
@month : 六月
@Author : mhm
@FileName: 6、买卖股票的最大收益（可以进行多次交易）.py
@Software: PyCharm
'''
'''
题目描述：可以进行多次交易，多次交易之间不能交叉进行，可以进行多次交易。
对于 [a, b, c, d]，如果有 a <= b <= c <= d ，那么最大收益为 d - a。
而 d - a = (d - c) + (c - b) + (b - a) ，因此当访问到一个 prices[i] 且 prices[i] - prices[i-1] > 0，那么就把 prices[i] - prices[i-1] 添加到收益中。
'''

'''
分析和例子：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。 
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [7,1,5,3,6,4] 
输出: 7 
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。 
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

输入: [1,2,3,4,5] 
输出: 4 
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。 
注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。 
因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

输入: [7,6,4,3,1] 
输出: 0 
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
# 方法1
def maxProfit(price):
    sum = 0
    for i in range(len(price)-1,0,-1):
        if price[i]<=price[i-1]:
            continue
        else:
            sum += price[i]-price[i-1]
    return sum

# 方法2
def maxProfit(price):
    profit = 0
    i = 0
    while i<len(price)-1:
        minimum = price[i]
        j = i+1
        if price[i]>=price[j]:
            minimum = min(price[j],minimum)
            i += 1
        else:
            while j<=len(price)-1:
                if j == len(price)-1:
                    profit+=price[j]-minimum
                    return profit
                elif price[j]<=price[j+1]:
                    j+=1
                else:
                    profit+=price[j]-minimum
                    i = j+1
                    break
    return profit











