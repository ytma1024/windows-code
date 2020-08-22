# 20200814
# 1、for循环的语法
'''
for 变量名 in 可迭代对象: # 可迭代对象可以是：列表，字典，字符串，元组，集合
    代码1
    代码2
    代码3
'''
# 案例1：列表循环取值
# lst = ['Bruce', 'Alex', 'L1n']
# for x in lst:
#     print(x)

# 案例2：字典循环取值
# dic = {'k1': 111, 'k2': 222, 'k3': 333}
# for k in dic:
#     print(k, dic[k])

# 案例3：字符串循环取值
# msg = 'you can you up,no can no bb.'
# for x in msg:
#     print(x)

# 2、for循环控制循环次数
# range功能介绍：

# for x in range(30):
#     print("===>")

# for+break:同while循环一样
# for+else:同while循环一样
# for+continue:同while循环一样

# username = 'Bruce'
# password = '123'
# for x in range(3):
#     inp_usrname = input("请输入您的账户：")
#     inp_usrpwd = input("请输入您的密码：")
#     if inp_usrname == username and inp_usrpwd == password:
#         print("登陆成功！")
#         break
# else:
#     print("输入次数过多，登陆失败！")

# 3、print补充
# print('hello','world')

# print('hello')
# print('world')

# print('hello',end=' ')  # 单引号中间填的任何符号，显示在hello和world中间
# print('world')