"""
匿名函数
在传入函数时，有时候不需要显式定义函数，直接传入匿名函数会更方便
"""
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8])))


# 以上🌰的匿名函数就是
def f(x):
    return x * x


"""
关键字 lambda 表示匿名函数，冒号前的 x 表示函数参数
匿名函数只能有一个表达式，不用写 return，返回值就是该表达式的结果
匿名函数没有名字，不用担心函数名冲突，匿名函数也是个函数对象，可以将匿名函数赋予一个变量，再利用变量调用函数
"""

l_f = lambda x: x * x

print(l_f)
print(list(map(l_f, [1, 2, 3, 4, 5])))


# 也可以将匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


l_f_1 = build(1, 2)
print(l_f_1)
print(l_f_1())

"""
练习
请用匿名函数改造下面的代码：
"""


# 改造前
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
# 改造后

M = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L)
print(M)
