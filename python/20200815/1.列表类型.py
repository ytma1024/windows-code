# 20200815

# 列表类型
# 1、作用：按位置存放多个值

# 2、定义：
# lst = [1, 2, 'a']  # lst=list()
# print(type(lst))

# 3、类型转换：但凡能够被for循环遍历的类型都能够当做参数传给list()转成列表
# res=list('hello')
# print(res,type(res))
# res = list({'k1': 111, 'k2': 222, 'k3': 333})
# print(res,type(res))

# 4、内置方法
# 优先掌握的操作
# lst=[111,'Bruce','Alex']
# 4.1、按照索引存取值（正向存取+反向存取）：即可以取也可以改
# lst=[111,'Bruce','Alex']
# 正向取
# print(lst[0])
# 反向取
# print(lst[-1])
# 可以取也可以改:索引存在修改对应值
# lst[0]=333
# print(lst)

# 无论是取值操作还是赋值操作：索引不存在则报错
# lst[3]=111
# print(lst)

# 4.2、切片（顾头不顾尾，步长）
# lst=[111,'Bruce','Alex','a','b','c','d']
# print(lst[:])
# print(lst[0:5:2])
# print(lst[5:0:-1])
# new_lst=lst[:]  # 切片等同于拷贝行为，相当于浅copy
# print(lst[::-1])  # 将列表倒置

# 4.3、长度：统计列表中元素的个数,len()
# lst=[111,'Bruce','Alex','a','b','c','d']
# # print(len(lst))

# 4.4、成员运算in和not in
# lst=[111,'Bruce','Alex','a','b','c','d']
# print(111 in lst)
# print(222 not in lst)

# 5、列表中添加值
# 5.1、追加:往列表中追加值
# lst.append(333)
# print(lst)

# 5.2、插入值：往列表的任意位置插入值
# lst.insert(1,'Hello')
# print(lst)

# 5.3、lst.extend()
# lst=[111,'Bruce','Alex']
# new_lst=[1,2,3]
# 需求：将new_lst中的元素取出来加到lst后面
# for item in new_lst:
#     lst.append(item)
# print(lst)

# extend实现了上述代码的功能
# lst.extend(new_lst)
# lst.extend('abc')
# print(lst)

# 6、删除
# del是通用的删除方法，只是单纯的删除方法，没有返回值
# 方法一：
# lst=[111,'Bruce','Alex']
# del(lst[1])
# x=del(lst[1])  # 抛出异常，不支持赋值语法
# print(lst)

# 方法二：lst.pop()根据索引删除，有返回值，返回删掉的那个值
# lst=[111,'Bruce','Alex']
# lst.pop()  # 不指定索引，默认删除最后一个
# print(lst)

# res = lst.pop(1)  # 有返回值，返回删掉的那个值
# print(res)

# 方法三：l.remove(),返回值为None
# lst=[111,'Bruce','Alex']
# res = lst.remove('Bruce')
# print(lst)
# print(res)  # 返回值为None

# 7、循环
# lst=[111,'Bruce','Alex','a','b','c','d']
# for x in lst:
#     print(x)

# 需要掌握的操作
# 1、lst.count():统计字符串在列表中出现的次数
# lst=[111,'Bruce','Alex','Bruce','Bruce']
# res = lst.count('Bruce')
# print(res)

# 2、lst.index()：统计字符串在列表中首次出现的索引数
# lst = [111, 'Bruce', 'Alex', 'Bruce', 'Bruce']
# res = lst.index('Bruce')
# print(res)
# print(lst.index(('aaa'))  # 找不到时报错

# 3、lst.clear():清空列表
# lst=[111,'Bruce','Alex','Bruce','Bruce']
# res=lst.clear()
# print(res)

# 4、lst.reverse():不是排序，就是将列表倒置
# lst = [111, 'Bruce', 'Alex']
# res = lst.reverse()
# print(lst)

# 5、lst.sort():排序，列表内元素必须是同种类型才可以排序
# lst = [11, -3, 2, 0, 9]
# lst.sort()  # 从小到大排序，默认为升序
# print(lst)

# lst.sort(reverse=True)  # 从大到小排序，设置为降序
# print(lst)

# 补充知识：队列与堆栈
# 1、队列：FIFO，先进先出
# lst=[]
# # 入队操作
# lst.append('first')
# lst.append('second')
# lst.append('third')
# print(lst)
# # 出队操作
# print(lst.pop(0))
# print(lst.pop(0))
# print(lst.pop(0))

# 2、堆栈：LIFO，后进先出
# lst = []
# # 入栈操作
# lst.append('first')
# lst.append('second')
# lst.append('third')
# print(lst)
# # 出栈操作
# print(lst.pop())
# print(lst.pop())
# print(lst.pop())
