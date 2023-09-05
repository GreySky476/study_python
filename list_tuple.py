# 学习使用 python 内置数据类型
# list
classmates = ['anna', 'emma', 'bob']
print(classmates)
# 获取 list 元素个数
print(len(classmates))
# 用索引访问没一个位置元素
print('{0} {1} {2}'.format(classmates[0], classmates[1], classmates[2]))
# 取最后一个元素可以使用 -1，倒数第二个 -2，倒数第三个 -3 等等
print(classmates[-1])
# 追加元素
classmates.append('jack')
print(classmates)
# 插入指定位置
classmates.insert(0, 'maybe')
print(classmates)
# 删除末尾元素
classmates.pop()
print(classmates)
# 删除指定位置：索引
classmates.pop(0)
print(classmates)
# 替换某个元素，可直接赋值
classmates[0] = 'annas'
print(classmates)
# list 元素的数据类型可以不同
L = ['oppo', 1, False]
print(L)
S = ['oppo', 123, [1, 2, 3]]
# 为字符串时，第二个索引是当前字符串切割成字符数组后的索引
print(S[0][1])
# 报错，整数类型不支持
# print(S[1][1])
# 取的是元素为数组中索引对应的值
print(S[2][1])
# 空数组
A = []
print(len(A))
# tuple 元组，初始化后不能修改，没有修改之类的方法，获取和 list 是一样的
tuple_1 = (1, 2, 3, 4, 5, 6, 7)
print(tuple_1[0])
