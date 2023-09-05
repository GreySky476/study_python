import math


# 定义函数
def def_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(def_abs(-100))


# 空函数 pass，当作占位符，比如还没想好怎么写代码，先放个 pass，让代码能运行起来
def nop(age):
    if age >= 18:
        # 不能缺少，否则会有语法错误
        pass
    pass


# 更详细的描述
# 上面定义的函数在针对不支持的类型时提示错误不够完整
# print(def_abs('A'))


# 定义一个新函数，做类型检查
def def_abs01(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# print(def_abs01('A'))


# 返回多个值
# import math 表示导入 math 包，并允许后续代码引用包中的方法
# 在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以算出新坐标
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 但是返回多个值其实是个假象，其实返回值是个 tuple，在语法上，返回一个 tuple 可以省略括号，而多个变量可以同时接收一个 tuple，按位置赋给对应的值。
r = move(100, 100, 60, math.pi / 6)
print(r)

'''
函数定义
1、定义函数时，需要先确定函数名和参数个数
2、如果有必要可以对数据类型做检查
3、函数内可以 return 随时返回结果
4、函数执行完毕也没有 return 语句时，自动 return None
5、函数可以返回多个值，但其实就是个 tuple
'''

'''
请定义一个函数 quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2 + bx + c = 0 的两个解。
x = -b + 根号(b^2 - 4ac) / 2a
'''


# 相关函数
def quadratic(a, b, c):
    x_1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x_2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x_1, x_2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
