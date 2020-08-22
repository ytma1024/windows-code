# 20200816
# 编码与解码
x = '上'
res = x.encode('gbk')  # unicode------->gbk
print(res, type(res))  # 运行结果：b'\xc9\xcf' <class 'bytes'>

print(res.decode('gbk'))  # 运行结果：上
