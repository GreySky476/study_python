"""
装饰器
"""
import functools
import time


def now():
    print('2023-09-19')


now()
# 函数对象有一个 __name__ 属性，可以获取到函数名称
print(now.__name__)


# 假设需要增强 now 函数的功能，比如在函数调用前后自动打印日志，又不希望修改 now 函数的定义，这种在代码运行期间动态增加功能的方式称之为『装饰器』
# 本质上 decorator 是一个返回函数的高阶函数，所以需要定义一个打印的 decorator 如下
# 接收一个需要增强的函数
def log(func):
    def wrapper(*args, **kw):
        # 增强功能【打印日志】
        print('call %s():' % func.__name__)
        # 返回函数
        return func(*args, **kw)
    return wrapper
# 借助 python 的 @ 语法，把 decorator 置于函数的定义处


@log
def now_power():
    print('2023-09-20')


# 将 @log 放在 now() 函数的定义处，相当于执行了 now = log(now)
now_power()
"""
由于 log() 是一个 decorator，返回一个函数，原来的 now 函数仍然存在，只是同名的 now 变量指向了新的函数，于是调用 now() 执行新函数
新函数值 log 函数中的 wrapper 函数
wrapper 函数参数定义为 (*args, **kw)【*args 加了 * 表示接收一个 tuple，** 表示接收一个 dict】，因此，wrapper 可以接受任意参数的调用。
如果 decorator 本身需要传入参数，那就需要编写一个返回 decorator 的高阶函数，会更复杂
"""


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2023-09-20')


# 相比两层嵌套的 decorator，3层嵌套的效果是 now = log('execute')(now)
# 解析：首先执行 log('execute') 返回 decorator 函数，再调用该函数，传参为 now 函数，返回值最终是 wrapper 函数

now()
# 输出为 wrapper，由于最后返回为 wrapper 函数对象，覆盖了之前的 now，所以需要把原始函数 __name__ 等属性复制到 wrapper 中，否则代码可能不符合预期
print(now.__name__)
# 不需要编写 wrapper.__name__ = func.__name__ 这样的代码，python 内置的 functools.wraps 专门干这事，导入相关模块


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2023-09-20')


now()
print(now.__name__)


# 针对带参 decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute1')
def now():
    print('2023-09-20')


now()
print(now.__name__)


"""
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
"""


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        n = fn(*args, **kw)
        print('%s executed in %.4f ms' % (fn.__name__, time.time() - start))
        return n
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

"""
请编写一个decorator，能在函数调用的前后打印出 'begin call' 和 'end call' 的日志。

再思考一下能否写出一个 @log 的decorator，使它既支持：@log、@log('execute')
"""


def log(arg):
    # 思路：如果是不传参，这里 func 默认为 None
    def decorator(func=None):
        if not func:
            print('function %s():' % arg.__name__)
            return arg()

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (arg, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def f():
    print('f测试成功')


@log('execute')
def g():
    print('g测试成功')


f()
g()
