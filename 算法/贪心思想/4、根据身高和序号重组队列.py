# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/24 14:19
@month : 六月
@Author : mhm
@FileName: 4、根据身高和序号重组队列.py
@Software: PyCharm
'''
'''
例子：
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

题目描述：一个学生用两个分量 (h, k) 描述，h 表示身高，k 表示排在前面的有 k 个学生的身高比他高或者和他一样高。
为了使插入操作不影响后续的操作，身高较高的学生应该先做插入操作，否则身高较小的学生原先正确插入的第 k 个位置可能会变成第 k+1 个位置。
身高 h 降序、个数 k 值升序，然后将某个学生插入队列的第 k 个位置中。
'''
# 方法一
def reconstructQueue(people):
    if people == []:
        return []
    people = sorted(people,key=lambda people:(-people[0],people[1]))
    res = [people[0]]
    for i in range(1,len(people)):
        res.insert(people[i][1],people[i])
    return res

'''
用插入法，因为将身高最高高的一组用户排序完成后，仅需要将身高低的用户一组一组排序插入即可（身高低的用户不会影响身高高的用户的k）。
1）先将身高最高的一组用户根据 k （在这个人前面，且身高大于等于他的人数）从小到大排序.
2）将身高第二高的一组用户根据k进行排序，然后将k作为插入时的索引，将用户插入。
3）重复2），将身高第三高组用户同样方式插入。
'''
def reconstructQueue1(people):
    a = people
    a.sort(key=lambda x:(-x[0],x[1]))
    if len(a) == 1:
        return a
    else:
        index = []
        last_i = 0
        for i in range(len(a)-1):
            if a[i][0]-a[i+1][0] != 0:
                index.append(a[last_i:i+1])
                last_i = i+1
        index.append(a[last_i:])
        for j in range(1,len(index)):
            aim = index[j]
            for ss in range(len(aim)):
                index[0].insert(aim[ss][1],aim[ss])
        return index[0]

print(reconstructQueue1([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))














