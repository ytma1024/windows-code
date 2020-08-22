# 20200816
# 集合类型
# 1、作用
# 1.1、关系运算
# friends1 = ['Bryant', 'Jordan', 'Bruce', 'Alex']
# friends2 = ['jason', 'jack', 'Bruce', 'Bryant']
# l = []
# for x in friends1:
#     if x in friends2:
#         l.append(x)
# print(l)
# 1.2、去重

# 2、定义：在{}内用逗号分隔开多个元素，多个元素满足以下三个条件：
#         a、集合内元素必须是不可变类型
#         b、集合内元素无序
#         c、集合内元素没有重复
# s={1,2}  # s=set({1,2})
# print(s,type(s))
# s={1,[1,2]}  # 直接报错
# s={1,'a',3,'b',0,'d'}  # 集合中元素的无序性
# s={1,1,1,1,1,'a','b','b','b'}  # 集合内元素没有重复性
# print(s)

# 了解知识
# s={}  # 默认是空字典
# print(type(s))
# s=set()  # 定义空集合
# print(type(s))

# 3、类型转换
# res=set('hellollll')
# print(res)  # 运行结果：{'l', 'e', 'o', 'h'}

# 4、内置方法
# =============================关系运算=============================
# friends1 = {'Bryant', 'Jordan', 'Bruce', 'Alex'}
# friends2 = {'jason', 'jack', 'Bruce', 'Bryant'}
# 4.1、取交集：两者共同的元素
# res = friends1 & friends2
# print(res)

# res = friends1.intersection(friends2)  # 相当于上面的friends1 & friends2
# print(res)

# 4.2、取并集
# res = friends1 | friends2
# print(res)

# res = friends1.union(friends2)  # 相当于上面的friends1 | friends2
# print(res)

# 4.3、取差集
# res = friends1 - friends2  # friends1中独有的好友
# print(res)

# res = friends1.difference(friends2)  # 相当于上面的friends1 - friends2
# print(res)

# res = friends2 - friends1  # friends2中独有的好友
# print(res)

# res = friends2.difference(friends1)  # 相当于上面的friends2 - friends1
# print(res)

# 4.4、对称差集：求两个用户独有的好友们（即取掉共同的好友）
# res = (friends1 - friends2) | (friends2 - friends1)
# res = friends1 ^ friends2  # 等同于上面的(friends1 - friends2) | (friends2 - friends1)
# print(res)

# res = friends1.symmetric_difference(friends2)  # 等同于上面的friends1 ^ friends2
# print(res)

# 4.5、父子集：包含关系
# s1={1,2,3}
# s2={1,2,4}
# # 不存在包含关系，下面比较结果均为False
# print(s1>s2)
# print(s2>s1)

# s1={1,2,3}
# s2={1,2}
# # 当s1大于或者等于s2时，才能说s1是s2它爹
# print(s1>s2)

# res = s1.issuperset(s2)  # 相当于s1>s2
# print (res)
# res = s2.issubset(s1)  # 相当于s2>s1
# print(res)

# s1 = {1, 2, 3}
# s2 = {1, 2, 3}
# # s1与s2互为父子关系
# print(s1 == s2)
# =============================================================

# =============================去重=============================
# 5、集合的去重
# 5.1、只能针对不可变类型去重
# s = set([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# # print(s)

# 5.2、无法保证原来的顺序
# lst = [1, 'a', 'b', 'c', 3, 2, 1, 1]
# s = set(lst)  # 运行结果{1, 'a', 3, 2, 'c', 'b'}
# print(s)

# l = [
#     {'name': 'lili', 'age': 18, 'sex': 'male'},
#     {'name': 'jack', 'age': 73, 'sex': 'male'},
#     {'name': 'tom', 'age': 20, 'sex': 'female'},
#     {'name': 'lili', 'age': 18, 'sex': 'male'},
#     {'name': 'lili', 'age': 18, 'sex': 'male'},
# ]
#
# new_l = []
# for dic in l:
#     if dic not in new_l:
#         new_l.append(dic)
# print(new_l)

# 6、其他操作
# 6.1、长度
# 6.2、成员运算符
# 6.3、循环

# 7、其它内置方法
# 需要掌握的内置方法
# s = {1, 2, 3}
# 7.1、s.discard()  # 删除集合中的元素
# s.discard(3)  # 如果删除的元素在集合内，则直接删掉
# print(s)
# s.discard(3)  #如果删除的元素不在集合内，则不做任何事
# print(s)

# 7.2、s.remove()  # 删除集合中的元素
# s.remove(3)  # 如果删除的元素在集合内，则直接删掉
# print(s)
# s.remove(4)  # 如果删除的元素不在集合内，则报错
# print(s)

# 7.3、s.update()  # 更新集合
# res = s.update({1, 3, 5})
# print(s)

# s.difference_update({3,4,5})  # 相当于s=s.difference({3,4,5})
# print(s)

# 7.4、s.pop()  # 删除集合中的元素
# res = s.pop()
# print(s)

# 7.5、s.add()  # 向集合中添加元素
# res = s.add(4)
# print(s)

# 需要了解的内置方法

# 7.6、s.isdisjoint()  # 两个集合完全独立，没有共同部分，返回True
# res = s.isdisjoint({4, 5, 6})  # 两个集合完全独立，没有共同部分，返回True
# print(res)

# res = s.isdisjoint({3,4, 5})  # 两个集合有部分相同，返回False
# print(res)
