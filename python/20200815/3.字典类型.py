# 20200815
# 字典类型
# 1、作用
# 2、定义:{}内用逗号分隔开多个key:value,其中value可以是任意类型，
# 但是key必须是不可变类型，且不能重复
# dic = {'k1': 111, '(1,2,3)': 222}  # dic=dict({'k1':111,'(1,2,3)':222})
# print(dic['k1'])
# print(dic['(1,2,3)'])

# d={}  # 默认定义出来的是空字典
# print(d,type(d))

# d=dict(x=1,y=2,z=3)  # 造字典类型
# print(d,type(d))

# 3、数据类型转换
# info = [
#     ['name', 'Bruce'],
#     ('age', 20),
#     ['gender', 'male']
# ]
# d = {}
# for item in info:
#     d[item[0]] = item[1]
# print(d)

# dic=dict(info)  # 一行代码搞定上述for循环的功能
# print(dic)

# 造字典的方式：快速初始化一个字典
# key = {'name', 'age', 'gender'}
# d = {}
# for x in key:
#     d[x] = None
# print(d)

# dic={}.fromkeys(key,None)  # 一行代码实现上述for循环的功能
# print(dic)

# 4、内置方法
# 优先掌握的操作
# 4.1、按key存取值，可存可取
# d = {'k1':111}
# 针对赋值操作：k存在，则修改
# d['k1']=222
# print(d)
# 针对赋值操作：k不存在，则创建新值
# d['k2']=333
# print(d)

# 4.2、长度len:统计key的个数
# d = {'k1':111,'k2':222,'k1':333,'k1':444}
# print(len(d))

# 4.3、成员运算in和not in:依据的是key
# d = {'k1':111,'k2':222}
# print('k1' in d)
# print(111 in d)

# 4.4、删除
# d = {'k1':111,'k2':222}
# 4.4.1 通用删除方法：
# del d['k1']
# print(d)

# 4.4.2、pop删除：根据key值删除，会返回删除的key对应的value值
# res = d.pop('k2')
# print(d)
# print(res)

# 4.4.3、popitem删除：随机删除,会返回一个元组，（刚刚删除的那个key和它对应的value组成的元组）
# res = d.popitem()
# print(d)
# print(res)

# 4.5、键keys(),值values(),键值对items()  (在python2中演示)
# d = {'k1':111,'k2':222}

# 4.6、for循环
# d = {'k1': 111, 'k2': 222}
# for k in d:
#     print(k)
#
# for v in d.values():
#     print(v)
#
# for k, v in d.items():
#     print(k, v)

# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# 5、其他内置方法
# 需要掌握的
# d = {'k1':111,'k2':222}
# 1、d.clear()
# print(d.clear())  # 清空字典

# 2、d.update()  # 更新字典，老字典中没有的，追加到老字典中
# d = {'k1':111,'k2':222}
# dic = {'k3':333,'k4':444}
# res = d.update(dic)
# print(d)

# 3、d.get()
# d = {'k1':111,'k2':222}
# print(d['k1'])  # 111
# print(d['k3'])  # key不存在则报错
# print(d.get('k1'))  # 111
# print(d.get('k3'))  # key不存在不报错，返回值为None

# 4、d.setdefault()
# 4.1、如果key由则不添加，返回字典中key对应的值
# info = {'name':'Bruce','age':20}
# res = info.setdefault('name','Bruce')
# print(info)
# print(res)

# 4.2、如果key没有则添加，返回字典中key对应的值
# info = {}
# res = info.setdefault('name','Bruce')
# print(info)
# print(res) 