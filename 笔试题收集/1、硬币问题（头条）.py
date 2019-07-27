# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/7/4 18:31
@month : 七月
@Author : mhm
@FileName: 1、硬币问题（头条）.py
@Software: PyCharm
'''
'''
题目描述：
Z国的货币系统包含面值1、4、16、64元共计4种硬币，以及面值1024元的纸币。现在小Y使用1024元的纸币购买了一件价值为N(0<N<=1024)的商品，请问最少他会收到多少硬币？
输入描述：
一行，包含一个整数N
输出描述：
一行，包含一个数，表示最少收到的硬币数
示例1：
输入：200
输出：17
解释：824 = 64x12 + 16x3 + 4x2, 12 + 3 + 2 = 17

思路分析：
第一眼瞟过去以为是一个标准的零钱凑整问题，但是立马发现硬币的面值为定值且呈倍数关系
也就是能用大面值的情况，绝对不可能去使用小面值，故贪心可解。
'''
def charge(N): # 不对
    aim = 1024 - N
    i=0
    while 64*i<=aim:
        i += 1
    aim1 = aim - 64*i
    j = 0
    while 16*j<=aim1:
        j+=1
    aim2 = aim1-16*j
    if aim2<4:
        n = aim2
    else:
        n = (aim2)//4 + (aim2)%4
    return i+j+n
print(charge(200))

def cahrge2(N):
    n = int(N)
    target = 1024 - n
    res = 0
    for val in [64,16,4,1]:
        res += target // val
        target %= val
    return res

print(cahrge2(200))















