# 迭代器
"""
目前直接作用于 for 循环的数据类型有 list、tuple、dict、set、str 等
还有就是 generator 包括生成器和带 yield 的 generator function
这些可作用于 for 循环的对象统称为 Iterable【可迭代对象】
可以使用 isinstance 判断一个对象是否是 Iterable 对象
"""
from collections.abc import Iterable, Iterator
# list
print(isinstance([], Iterable))
# dict
print(isinstance({}, Iterable))
# str
print(isinstance('str', Iterable))
# generator
print(isinstance((x for x in range(10)), Iterable))
# int
print(isinstance(100, Iterable))
"""
生成器不但能作用于 for 循环，还能作用于 next() 函数
可以被 next 函数调用并不断返回下一个值的对象成为迭代器：Iterator
可以使用 isinstance 判断一个对象是否是 Iterator 对象
"""
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
"""
生成器都是 Iterator 对象，但 list、dict、str 虽然是 Iterable，但不是 Iterator，需要将 Iterable 转换成 Iterator 可以使用 iter() 函数
"""
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abc'), Iterator))
"""
思考🤔：为什么 Iterable 不是 Iterator？
Iterable 和 Iterator 的区别在于 Iterator 支持 next() 函数
generator 本身是直接支持 Iterator，而 generator 的特性是可以通过某种算法推算出来，而不比在一开始创建完整的 list。
而对比 list、dict、str，它们本身是需要初始化的，也就是有一个基本大小，generator 的大小只能通过推算
结合来看，Iterator 表示的是一个不确定、甚至无限大的数据，而其它 list 等会有一个明确的长度界限

官方点的解释：Iterator 对象表示的是一个数据流，可以被 next() 不断调用并返回数据，直到抛出 StopIteration 错误。
可以把这个数据流当作有序序列，但是不能提前知道序列的长度，只能不断的通过 next() 函数实现按需计算下一个数据，所以 Iterator 是惰性的，只有需要时返回
Iterator 甚至可以是一个无限大的数据流，比如全体自然数，而使用 list 等永远不可能存储全体自然数。

小结：
凡是可作用于 for 循环的都是 Iterable 类型
可用于 next() 是 Iterator 类型，它是一个惰性序列
集合类型不能直接使用 next()，可以通过 iter() 获得一个 Iterator 对象
for 循环本质不断的调用 next() 实现的
"""