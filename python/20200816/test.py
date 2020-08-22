# coding:GBK

x='上'
# print([x])  # 运行结果 ['\xc9\xcf']
#
# print('\xc9\xcf')  # 理论上： '\xc9\xcf'======>unicode======>'上'
#                    # 实际上：转换成乱码  ??
print(x)  # 运行结果：??(乱码)

y=u'上'  # 强制转换成unicode类型
# print([y])  # 运行结果：[u'\u4e0a']
print(y)  # 运行结果：上