# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/26 10:12
@month : 六月
@Author : mhm
@FileName: 5、买股票最大的收益.py
@Software: PyCharm
'''
'''
题目描述：一次股票交易包含买入和卖出，只进行一次交易，求最大收益。
只要记录前面的最小价格，将这个最小价格作为买入价格，然后将当前的价格作为售出价格，查看当前收益是不是最大收益。
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。 
注意你不能在买入股票前卖出股票。

输入: [7,1,5,3,6,4] 
输出: 5 
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。 
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

输入: [7,6,4,3,1] 
输出: 0 
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

def maxProfit(price): # 我的
    cur_price = min(price)
    min_index = price.index(cur_price)
    new = price[min_index:]
    sale_price = max(new)
    return sale_price - cur_price

def maxPrice1(price):
    if not price:
        return 0
    l = []
    for i in range(len(price)):
        for j in range(i+1,len(price)):
            if price[j] > price[i]:
                l.append(price[j]-price[i])
    if not l:
        return 0
    else:
        return max(l)

'''
思路三：
是不是在最低点买入，最高点卖出收益最大？回答是肯定的，那么找到最低点，
最高点，看看先后顺序，不合理，找第二高的点....不要把问题想复杂；
我们就假设第一个点为最低点，同时也是最高点，从头开始移动最高点，
同时记录每个点对应的收益，只留下最大的，如果移动到的点比最低点还低，
是时候考虑换个最低点了，然后继续刚才的操作，最后得到的就是最大收益
'''
def maxPrice(prices):
    if not prices:
        return 0
    low = prices[0]
    profit = 0
    for i in prices:
        if i - low>profit:
            profit = i-low
        if i<low:
            low=i
    return profit

