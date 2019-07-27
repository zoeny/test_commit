# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/24 9:50
@month : 六月
@Author : mhm
@FileName: 2、找到出现频率最多的k个元素.py
@Software: PyCharm
'''
# 例子：Given [1,1,1,2,2,3] and k = 2, return [1,2].
# 第一种方法：用dict来统计最后用sorted方法来排序取出前k个即可
class Solution(object):
    def topKFrequent(self,nums,k):
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] += 1
        out = sorted(dict1.items(),key=lambda e:e[1],reverse=True)
        final = []
        for i in range(k):
            final.append(out[i][0])
            return final

# 第二种：用collections里面的counter，调用most_common方法
class Solution1(object):
    def topkFrequence(self,nums,k):
        import collections
        l = collections.Counter(nums)
        return [x[0] for x in l.most_common(k)]










