"""
偏函数，函数通过设定参数的默认值可以降低函数调用的难度，偏函数同样能做到这一点
"""

# base 的设定表示将当前数当成什么进制进行转换成十进制
print(int('12345'))
# 八进制
print(int('12345', base=8))
# 十六进制
print(int('12345', base=16))
# 二进制
print(int('100000', base=2))


# 假如要大量的转换某一进制（比如二进制）非常麻烦，于是定义个函数 int2
def int2(x, base=2):
    return int(x, base)


print(int2('100000'))
print(int2('100010'))
