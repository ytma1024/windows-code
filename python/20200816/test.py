# coding:GBK

x='��'
# print([x])  # ���н�� ['\xc9\xcf']
#
# print('\xc9\xcf')  # �����ϣ� '\xc9\xcf'======>unicode======>'��'
#                    # ʵ���ϣ�ת��������  ??
print(x)  # ���н����??(����)

y=u'��'  # ǿ��ת����unicode����
# print([y])  # ���н����[u'\u4e0a']
print(y)  # ���н������