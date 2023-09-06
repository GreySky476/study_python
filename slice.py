# 切片
# 从 list 取部分元素属于常见常见操作
L = ['a', 'b', 'c', 'd']
# 比如取前三个，按照之前的操作可能需要用循环，或者 L[0]、L[1]、L[2]，但是 n 如果是个变量，那就只能考虑循环的方式，及其不方便
# 切片操作符，取前三个元素 [0,3)
print(L[0:3])
# 同上，从索引 0 开始取的话可忽略 0，从当前取到最后可忽略最后一个元素的索引
print(L[:3])
print(L[1:])
# python 支持倒数获取元素，同样支持倒数切片
print(L[-2:-1])
print(L[-2:])
# 通过切片可以非常轻松的取元素
# 生成 0-99 的数组
L_99 = list(range(100))
# 获取前 10 个
print(L_99[:10])
# 获取后 10 个
print(L_99[-10:])

# 设置步长取数
# 前 10 个数，每两个取一个
print(L_99[:10:2])
# 所有数，每五个取一个
print(L_99[::5])
# 后 10 个数，每三个取一个
print(L_99[-10::3])

# 只写 [:] 可原样复制一个 list
print(L_99[:])

# tuple 也是一种 list， 也可做切片操作，操作结果为 tuple
T = (1, 2, 3, 4, 5)
print(T[:3])

# 字符串也可看成一种 list，每个字符就是一个元素，因此也可做切片操作，结果仍然为字符串
str_ = 'ABCDEFG'
print(str_[:3])
'''
利用切片操作，实现一个 trim() 函数，去除字符串首尾的空格，注意不要调用 str 的 strip() 方法
'''


def trim(str_trim):
    # 当 str_trim 为空时，直接返回
    if not str_trim:
        return str_trim
    str_len = len(str_trim)
    start_index = -1
    end_index = -1
    str_index = str_len - 1
    for i in list(range(int(str_len / 2))):
        if start_index != -1 and end_index != -1:
            break
        if str_trim[i] != ' ' and start_index == -1:
            start_index = i
        if str_trim[str_index - i] != ' ' and end_index == - 1:
            end_index = str_index - i
    if start_index == -1 and end_index == -1:
        return ''
    return str_trim[start_index:end_index + 1]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
