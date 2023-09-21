"""
偏函数
函数可以通过设定参数默认值来降低调用的难度
"""
import functools

# 将字符串转换为整数
print(int('12345'))
# 将字符串转换以八进制的方式转换成十进制并打印结果
print(int('12345', base=8))
# 将字符串转化为十六进制的方式转换成十进制并打印结果
print(int('12345', base=16))


# 以上调用有些不方便，需要手动设置 base
def int2(x, base=2):
    return int(x, base)


# 使用定义的函数输出，省去了 base 参数的设定
print(int2("10010"))
# 使用 functools.partial 创建偏函数，不需要自定义 int2，可以直接使用新函数
int2 = functools.partial(int, base=2)
print(int2('100000'))
# functools.partial 的作用就是把一个函数的某些参数固定住（设置默认值），返回一个新函数
print(int2('1000000', base=10))
"""
functools.partial 创建函数时，实际上可以接收函数对象、*args 和 **kw 3 个参数
当传入 int2 = functools.partial(int, base=2) 相当于 kw = { 'base': 2 } => int('10010', **kw)
传入 max2 = functools.partial(max, 10)，会把 10 作为 *args 的一部分自动加到左边，当调用 max2(5, 6, 7) 时，相当于 max2(10, 5, 6, 7)
使用 functools.partial 可以创建一个新函数从而固定一些参数，使得调用函数变得更简单
"""