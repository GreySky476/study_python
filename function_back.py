"""
返回函数
高阶函数除了可以接受函数作为参数，还可以把函数作为结果值返回
"""


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(1, 3, 5, 7, 9))


# 也可以不立刻求和，而是根据需要再计算，返回求和的函数


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


"""
在 lazy_sum 中定义了函数 sum，并且内部函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量。
当 lazy_sum 返回 sum 时，相关参数和变量都保存在返回函数中，这种称之为『闭包』函数
"""
sum = lazy_sum(1, 3, 5, 7, 9)
print(lazy_sum(1, 3, 5, 7, 9))
print(sum())

# 每次调用 lazy_sum 返回的都是一个新函数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

"""
闭包函数
"""


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
# 期望打印是 1，4，9，实际结果为 9，9，9，在 count 函数中，返回函数引用了变量 i，它不会立即执行，而是等到 3 个函数都返回时，这时引用的变量 i 已经变成了 3
print(f1())
print(f2())
print(f3())
"""
返回闭包时必须牢记：返回函数不要引用任何循环变量，或者后续会发生变化的变量
如果一定要引用循环变量，需要在创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何修改，已绑定的函数参数值不变
"""


def count_new():
    # j 绑定 g() 函数的返回值，后续变化和当前 f 函数无关
    def f(j):
        # def g():
        #     return j * j
        # return g
        return lambda: j * j

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count_new()
print(f1())
print(f2())
print(f3())

"""
nonlocal
"""


def inc():
    x = 0

    def fn():
        # 需要增加 nonlocal 关键字，当使用闭包需要对外层变量赋值前，需要使用 nonlocal 声明该变量不是当前函数的局部变量
        nonlocal x
        # 这里想直接对外层变量赋值是不可行的，因为 python 会默认把 x 当作 fn 的局部变量使用，会报错
        x = x + 1
        return x

    return fn


f1 = inc()
print(f1())
print(f1())

"""
利用闭包返回一个计数器函数，每次调用它返回递增整数：
"""


def create_counter():
    x = 0

    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter


# 测试:
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
