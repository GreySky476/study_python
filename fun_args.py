# 函数参数的定义
def power(x):
    return x * x


# power 函数计算传入值的平方
# 但是该函数不够灵活，当计算其它次方就无法使用，所以扩展下
def power_1(x, n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(power_1(2, 2))


# 但是有时候只想计算平方，所以
def power_2(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


# 给予默认值
print(power_2(2))
print(power_2(2, 3))

'''
默认参数：可以简化函数调用
1、必选参数在前，默认参数在后，否则会报错，为什么？
思考原因：有歧义，必选参数在前时，可以确认在必选参数位数不够可以返回少了位置参数，
    而默认参数在前，必选在后，这时候无法给予用户正确的反馈，不确定是少填了位置参数，还是使用默认参数
2、如何设置默认参数
2.1、函数有多个参数时，变化大的参数放前面，变化小的放后面，变化小的就可以作为默认参数
3、默认参数注意事项：
3.1、函数在定义时，默认参数已经被计算出来了，即默认参数只想一个对象
3.2、定义默认函数必须指向不变对象！！！
'''


# 这里的定义 pycharm 已经提示了相关的语法错误
def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())

# 上面函数运行后会出现追加的情况，在函数定义时，默认参数 L 指向了一个对象 []，每次调用函数时，当使用默认参数，就会使用默认指向的对象去操作


# 该函数运行正常
def add_end_0(M=None):
    if M is None:
        M = []
    M.append('END')
    return M


print(add_end_0())
print(add_end_0())
print(add_end_0())

'''
为什么需要不变参数？
1、不变对象一旦创建，对象内部的数据就不能修改，减少了由于修改数据导致的错误
2、在多线程环境下，对象不变就没必要加锁，同时读不会产生问题，在编码中能设置不变对象就尽量设置不变对象
'''


# 可变参数的使用
def calc(numbers):
    sum_number = 0
    for n in numbers:
        sum_number = sum_number + n * n
    return sum_number


print(calc([1, 2, 3]))
# 以上调用比较麻烦，必须定义一个数组或 tuple


# 在参数前面增加一个 *，在函数内部，参数 numbers 接收到的是一个 tuple，因此，函数代码完全不变，但调用时可以传入任意参数，包括 0
def calc_0(*numbers):
    print(numbers)
    sum_number = 0
    for n in numbers:
        sum_number = sum_number + n * n
    return sum_number


print(calc_0(1, 2, 3))
print(calc_0())

# 当 list、tuple 需要调用传入可变参数时，可以在 list 或者 tuple 前加 * 表示把 list 或 tuple 作为可变参数传进去
nums = [1, 2, 3]
print(calc_0(*nums))


# 关键字参数，关键字参数允许传入 0 或任意个含参数名的参数，这些关键字函数在函数内部自动组装成一个 dict
def person(name, age, **kv):
    print('name:', name)
    print('age:', age)
    print('other:', kv)


person('Anna', 30)
person('Anna', 30, kv='zhouji')
person('Anna', 30, city='zhouji')
extra = {'city': 'Beijing', 'job': 'work'}
# **extra 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到 **kv 参数，kv 将获得一个 dict 的拷贝，并不会影响函数外的 extra
person('jon', 25, **extra)


# 检查关键字函数
def person_0(name, age, **kv):
    if 'city' in kv:
        pass
    if 'job' in kv:
        pass
    print('name:', name)
    print('age:', age)
    print('other:', kv)


# 命名关键字参数，限制关键字参数的名称，只接收固定的参数名。使用 * 分割，* 后面的都视为命名关键字参数
def person_1(name, age, *, city='BeiJing', job):
    print(name, age, city, job)


person_1('jack', 23, city='hz', job='program')
# 命名关键字参数必须传入参数名，没有传入则报错，但是可以为命名关键字参数设置默认值
# person_1('jack', 23, city='hz', 'program')

'''
参数组合，在定义函数时，可以用多个参数组合使用，但是顺序必须为
必选、默认、(可变||命名关键字)、关键字参数这样的顺序排列
'''


def f1(a, b, c=0, *, d, **kw):
    print(a, b, c, d, kw)


def f2(a, b, c=1, *d, **kw):
    print(a, b, c, d, kw)


f1(1, 2, d=3, kw='city')
f2(1, 2, 3, 4, 5, 6, kw='city')
# 除了依次填入，也可以使用 tuple 和 dict
args = (1, 2, 3)
kv = {'d': 99, 'e': 100}
# 关键字参数的值由 kv 中的 d: '99' 赋值
f1(*args, **kv)

args = (1, 2, 3, 4, 5, 6)
kv = {'d': 99, 'e': 100}
f2(*args, **kv)

# 对于任意函数，都可以使用 func(*args, **kw) 进行调用，无论它的参数是如何定义的

'''
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
'''


def mul(*numbers):
    if not numbers:
        raise TypeError
    res = 1
    for i in numbers:
        res = res * i
    return res


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
