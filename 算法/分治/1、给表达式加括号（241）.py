# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 9:49
@month : 六月
@Author : mhm
@FileName: 1、给表达式加括号（241）.py
@Software: PyCharm
'''
'''
分治算法的基本思想是将一个规模为N的问题分解为K个规模较小的子问题，这些子问题相互独立且与原问题性质相同。求出子问题的解，就可得到原问题的解。
即一种分目标完成程序算法，简单问题可用二分法完成。
分治算法解决的经典问题：
    （1）二分搜索
　　（2）大整数乘法
　　（3）Strassen矩阵乘法
　　（4）棋盘覆盖
　　（5）合并排序
　　（6）快速排序
　　（7）线性时间选择
　　（8）最接近点对问题
　　（9）循环赛日程表
     (10) 汉诺塔问题
Input: "2-1-1".
((2-1)-1) = 0
(2-(1-1)) = 2
Output : [0, 2]
'''
# 方法1：递归
def diffWayToCompute(input):
    def dfs(s,cache):
        ops = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y}
        if not cache.has_key(s):
            ret = []
            for k,v in enumerate(s):
                if v in '+-*':
                    for left in dfs(s[:k],cache):
                        for right in dfs(s[k+1:],cache):
                            ret.append(ops[v](left,right))
            if not ret:
                ret.append(int(s))
            cache[s] = ret
        return cache[s]
    return dfs(input,{})

# 方法二
def diffWaysToCompute1(input):
    ops = {'+':lambda x,y:x+y,
           '-':lambda x,y:x-y,
           '*':lambda x,y:x*y}
    def ways(s):
        ans = []
        for i in range(len(s)):
            if s[i] in '+-*':
                ans += [ops[s[i]](l,r) for l,r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
        if not ans:
            ans.append(int(s))
            return ans
    return ways(input)



