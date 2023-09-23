"""
编写一个 hello 模块
"""
# 该行注释可以让本文件直接在 unix/linux/mac 直接运行
# !/usr/bin/env python3
# 代表使用 utf-8 编码
# -*- coding: utf-8 -*-

import sys

'a test module'
# 使用 __author__ 变量把作者谢进入
__author__ = 'SQL'


def test():
    # argv 变量使用 list 存储命令行所有参数，argv 至少有一个参数，因为第一个参数永远是该 .py 文件名称
    args = sys.argv
    if len(args) == 1:
        # 执行 python3 hello_module.py 将打印以下结果
        print('hello world!')
    elif len(args) == 2:
        # 执行 python3 hello_module.py GREYSQL 将打印 hello, GREYSQL
        print('hello, %s' % args[1])
    else:
        # 超过 python3 hello_module.py GREYSQL 的参数将打印以下结果
        print('too many arguments!')


# 使用命令行运行 hello 模块时，python 解释器将一个特殊变量 __name__ 置为 __main__
# 如果其它地方导入本模块，if 判断将失败，因此这种 if 测试可以让一个模块通过命令行运行时执行一些额外代码
"""
作为模块导入需要手动调用 test() 函数
>> import hello_module
>>> hello_module.test()
hello world!
"""
if __name__ == '__main__':
    test()


"""
作用域
python 一般会定义很多函数和变量，但有的函数并不希望给别人使用，这时候可以使用 _ 前缀来实现
正常函数和变量名是公开的，可以被直接引用，比如 abc, syz 等
__xx__ 这种属于特殊变量，比如上方的 __author__、__name__，
类似 _xx、__xx 的函数和变量就是非公开的，不应该被直接引用，比如 _abc、_xyz
python 并没有强制限制访问 private 函数和变量，只是从编程习惯上说不应该引用
"""


def _private_1(name):
    return 'hello, %s' % name


def _private_2(name):
    return 'hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 以上函数例子就是典型例子，公开 greeting 函数，把内部逻辑通过 private 函数隐藏起来，这样调用 greeting() 就不用关心内部的函数细节
# 外部不需要引用的函数全部定义成 private，只有外部需要的函数才定义为 public
