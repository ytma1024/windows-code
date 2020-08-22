# 20200813
# 1、循环的语法及基本使用：
'''
while 条件:
    代码1
    代码2
    代码3
'''
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# print("循环结束！")

# 2、死循环与效率问题
# 纯计算无IO的死循环会导致致命的效率问题

# 3、循环的应用（循环的终止）
# 方法一：
# usrname='Bruce'
# usrpwd=123
#
# tag=True
# while tag:
#     inp_name=input("请输入您的账户：")
#     inp_pwd=input("请输入您的密码：")
#
#     if inp_name=='Bruce' and inp_pwd=='123':
#         print("登陆成功！")
#         tag=False
#     else:
#         print("您输入的账户或者密码错误！")
# print("=======end=======")

# 方法二：while+break
# usrname = 'Bruce'
# usrpwd = 123
#
# while True:
#     inp_name = input("请输入您的账户：")
#     inp_pwd = input("请输入您的密码：")
#
#     if inp_name == 'Bruce' and inp_pwd == '123':
#         print("登陆成功！")
#         break
#     else:
#         print("您输入的账户或者密码错误！")
# print("=======end=======")

# while + else
# count = 0
# while count < 5:
#     print(count)
#     count+=1
# else:
#     print('else包含的代码会在while循环结束后，并且while循环'
#           '是在没有被break打断的情况下正常结束的，才会运行')
# print("=====end=====")

'''
usrname = 'Bruce'
usrpwd = '123'
count =0
tag=True
while count<3:
    inp_name = input("请输入您的账户：")
    inp_pwd = input("请输入您的密码：")

    count+=1
    if inp_name == 'Bruce' and inp_pwd == '123':
        print("登陆成功！")
        while tag:
            cmd=input("请输入命令:")
            if cmd == 'q':
                break
            else:
                print("命令正在运行！")
        break
    else:
        print("您输入的账户或者密码错误！")
else:
    print("输入次数已达三次，自动退出！")
print("=======end=======")
'''