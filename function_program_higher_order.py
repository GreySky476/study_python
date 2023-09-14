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