import os
# 列表表达式
# 生成 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11)))

# 生成 [1 * 1, 2 * 2, 3 * 3, 4 * 4, 5 * 5...]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# 上面的做法比较繁琐
# 以下将需要生成元素放在 for 循环前面，后面跟着 for 循环
print([x * x for x in range(1, 11)])
# 加上 if 判断，通过 x % 2 == 0 筛选
print([x * x for x in range(1, 11) if x % 2 == 0])
# 嵌套循环 ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m + n for m in 'ABC' for n in 'XYZ'])
# 导入 os 模块，listdir(): 获取指定路径下的所有文件和目录名
print([d for d in os.listdir('.')])
# 使用 items() 同时迭代 key,value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
# 也可以使用两个变量生成 list
print([k + '=' + v for k, v in d.items()])
# 把 list 中所有的字符串小写
L = ['Hello', 'World', 'IBM', 'HUAWEI']
print([s.lower() for s in L])
# 在 for 循环中使用 if...else...
# if 用法，这时候 for 之后的 if 是过滤条件，在这后面加 else 会报错
# print([x for x in range(1, 11) if x % 2 == 0 else -x])
print([x for x in range(1, 11) if x % 2 == 0])
# 而 if 在 for 之前时，提示必须加 else。可见，在一个列表生成式中， for 之前 if...else... 为表达式，for 之后是过滤条件不能带 else
print([x if x % 2 == 0 else -x for x in range(1, 11)])
'''
如果list中既包含字符串，又包含整数，由于非字符串类型没有 lower() 方法，所以列表生成式会报错
使用内建的 isinstance 函数可以判断一个变量是不是字符串
修改表达式，过滤 L1
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ele.lower() for ele in L1 if isinstance(ele, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')