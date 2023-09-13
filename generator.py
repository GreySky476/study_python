# 生成器

"""
通过列表生成式（range）可以很轻松的创建一个列表，但是列表大小会受到内存限制。
而且创建一个大的列表而访问的仅仅是前几个元素，会浪费很多空间
所以有了一种猜想，如果列表元素可以按照某种算法推算出来，是否可以在循环的过程中不断推算出后续元素呢？
这样的好处就是不必创建完整的 list，节省大量空间。
在 python 中，一边循环一边计算的机制称为生成器：generator
"""
# 创建 generator，最简单的方式就是把列表生成式的 [] 改成 ()
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
# 生成器可以通过 next(g) 获取下一个元素，直到返回 StopIteration 错误
print(next(g))
print(next(g))
print(next(g))
# 也可以使用 for 循环
for ele in g:
    # 有意思的是，上面通过 next(g) 向后推算了后续元素，这里的 for 循环将继续推算，而不是重新打印！！！
    print(ele)
# 著名的斐波拉契数列，除了第一、第二个数外，任意一个数都可由前两个数相加得到：
# 1,1,2,3,5,8,13,21,34
# 使用函数定义


def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        print(b)
        # 该赋值语句等于 t = (b, a + b) a = t[0] b = t[1]
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(6))
# fib 函数定义了斐波那契数列的推算规则，可以从第一个元素开始，推算出后续任意元素，这种逻辑类似与 generator
# 要将 fib 函数变成 generator 函数，只需要把 print(b) 改成 yield b


def fib_gener(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib_gener(6))
"""
generator 函数和普通函数执行流程不同
1、普通函数顺序执行，遇到 return 语句或最后一行函数就返回
2、generator 函数在每次调用 next() 时执行，遇到 yield 语句返回，再次执行时从上次 yield 语句处继续向下执行
"""
