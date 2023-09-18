from functools import reduce

# 高阶函数，让函数的参数能够接收别的函数
# 变量可以指向函数
print(abs(-10))
print(abs)
# 将函数调用的结果赋值给变量
x = abs(-10)
print(x)
# 将函数本身赋值给变量
f = abs
print(f(-10))

# 函数名也是变量
# 函数名解释就是指向函数的变量，对于 abs() 这个函数，可以吧函数名 abs 看成变量，它指向一个可以计算绝对值的函数
# 尝试把 abs 指向其它对象
# abs = 10
# 将 10 指向 abs 后，abs 这个变量已经不指向绝对值函数而是一个整数。一般代码不建议这样写
# 如果需要将改动生效，abs 在 builtins 模板中，要让修改 abs 变量指向在其它模块生效可以 import builtins; builtins.abs = 10
print(abs(-10))


# 传入函数
# 既然变量可以指向函数，函数的参数能够接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数


def add(x, y, f):
    return f(x) + f(y)


x = -5
y = -6
f = abs
print(add(x, y, f))

"""
map/reduce 函数，相关概念可看 Google 论文
map：接收两个参数，一个是函数，一个是 Iterable，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回
reduce: 把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元素做累积计算
"""


def f(x):
    return x * x


# r 本身是个 Iterator，Iterator 是个惰性序列，通过 list 计算出返回一个 list
r = map(f, list(range(1, 10)))
print(list(r))
# 以上的代码就是对『将传入的函数依次作用到序列的每个元素，并将结果作为新的 Iterator 返回』
# map 作为高阶函数将运算规则抽象了
# 将 list 中所有数字转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6])))


# reduce


def add(x, y):
    return x + y


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
print(reduce(add, [1, 2, 3, 4, 5, 6]))


# 把序列 [1, 3, 5, 7, 9] 变成整数 13579


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# 使用 reduce 和 map 将 str 转换成 int 函数
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


# 将以上步骤整理成 str2int
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    return reduce(fn, map(char2num, s))


print(str2int('13679'))


# 通过 lambda 表达式简化
def str2int_0(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int_0('17747'))


"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
"""


def normalize(name):
    dict_letter = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K',
                   'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U',
                   'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    name_list = list(name.lower())
    name_list[0] = dict_letter[name_list[0]]
    return reduce(lambda x, y: x + y, name_list)


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

"""
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
"""


def str2float(s):
    int_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    # 🤔：根据 . 分割，. 前面的数 * 10，后面的数 / 10
    comma_flag = False
    list_int = []
    list_decimal = []
    for ele in s:
        if ele == '.':
            comma_flag = True
            continue
        if comma_flag:
            list_decimal.append(ele)
        else:
            list_int.append(ele)

    def power(size):
        num = 1
        for i in range(1, size + 1):
            num = num * 10
        return num

    def list2int(s):
        return reduce(lambda x, y: x * 10 + y, map(lambda x: int_dict[x], s))

    int_res = list2int(list_int)
    decimal_res = list2int(list_decimal)
    return int_res + decimal_res / power(len(list_decimal))


# 参考解法
def str2float_0(s):
    char_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}
    nums = map(lambda x: char_dict[x], s)
    point = 0

    def to_float(f, n):
        # 非局部变量，作用是该变量去同步最近与它名称相同的变量
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums)


print('str2float(\'123.456\') =', str2float_0('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

"""
filter 函数
用于过滤序列，和 map 类似，也是接收一个函数和序列，filter 不同的是将函数作用于每个元素后返回 True 或 False
"""
