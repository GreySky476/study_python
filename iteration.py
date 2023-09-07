# 导入相关包
from collections.abc import Iterable
# 迭代
# 给定一个 list or tuple，通过 for 循环遍历，这种方式称为迭代
# 迭代 map
d = {'a': 1, 'b': 2, 'c': 3}
# 默认迭代 key
for key in d:
    print(key)
# 迭代 value
for value in d.values():
    print(value)
# 迭代 key, value
for key, value in d.items():
    print('key:', key, " value:", value)
# 字符串也能作为迭代对象
for c in 'ABC':
    print(c)

# 判断一个对象时候为可迭代对象
# 判断字符串时候可以迭代
print(isinstance('abc', Iterable))
# 判断 list 是否可以迭代
print(isinstance([1, 2, 3], Iterable))
# 判断整数是否可以迭代
print(isinstance(123, Iterable))

# 下标循环，python 中内置 enumerate 函数，可以把一个 list 变成索引-元素对，这样就可以同时迭代索引和元素本身
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)
'''
请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''


def find_min_and_max(L):

    if not isinstance(L, Iterable):
        return (None, None)
    if not L:
        return (None, None)
    min = L[0]
    max = L[0]
    for ele in L:
        if ele > max:
            max = ele
        if ele < min:
            min = ele

    return (min, max)


# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

