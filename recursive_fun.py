# 递归函数
# 计算阶乘 n! = 1 * 2 * 3 * ... * n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 使用递归要注意栈溢出问题。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧。
# 每当函数返回时，又会减少一层，而栈的大小是有限的，所以递归调用次数过多就会导致栈溢出
print(fact(10))
# 栈溢出
# print(fact(1000))

'''
在一些特殊场景中，可能对递归有一定的需求，而又因为栈的限制，所以出现了一种叫做『尾递归』优化。
尾递归和循环效果是一样的，可以把循环看做是一种特殊的尾递归函数
尾递归指在函数返回的时候调用自身本身且 return 语句不能包含表达式，这样编译器就可以把尾递归做优化，使得递归本地只会占用一个栈帧，不会出现栈溢出问题
上方的方法因为使用了 n * fact(n - 1)，引入乘法表达式，导致不是尾递归，下面将每一步的乘积传递到递归函数中。保证 return 不包含表达式
'''


def fact_0(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_0(10))
# 淦，python 解释器没对尾递归做优化
# print(fact_0(1000))

'''
汉诺塔的移动可以用递归函数非常简单地实现。
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
'''


# a 原始柱，b 中转柱，c 目标柱
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        # step1. 把除了最大盘的所有盘子从 A 移动到 B
        move(n - 1, a, c, b)
        # step2. 这时候只剩最大盘了，移动 A --> C
        move(1, a, b, c)
        # step3. 最大盘已经位于 C，现在需要将除了最大盘之外的所有盘从 B 移动到 C
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
