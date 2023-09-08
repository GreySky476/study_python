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
