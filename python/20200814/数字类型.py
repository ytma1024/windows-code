# 20200814
# 1、int类型
# 1.1、定义：
# age=10  # 相当于 age=int(10)

# 1.2、类型转换
# 纯数字的字符串转换成int
# res=int('11011')
# print(res,type(res))

# 10进制 -> 二进制
# print(bin(11))  # 0b1011 0b开头代表二进制

# 10进制 -> 八进制
# print(oct(11))   # 0o13 0o开头代表八进制

# 10进制 -> 十六进制
# print(hex(11))  # 0xb 0x开头代表十六进制

# 二进制 -> 十进制
# print(int ('0b1011',2))

# 八进制 -> 十进制
# print(int ('0o13',8))

# 十六进制 -> 十进制
# print(int ('0xb',16))

# 2、float类型
# 2.1、定义
# salary=3.1  # salary=float(3.1)

# 2.2、类型转换
# 将字符串转换成float类型
# res=float('3.1')
# print(res,type(res))