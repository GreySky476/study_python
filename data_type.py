# 整数，当一个数太大时，可以在数字间使用 _ 分割，不会改变数字的大小
int_num = 10_000_000
# 浮点数，对于很大或很小的浮点数可以使用科学计数法表达
float_num = 3.14
# 等同于 3.14 * 10 的 9 次方
float_num_1 = 3.14e9
# 字符串，用单引号或双引号括起来的文本
str_1 = 'hello'
str_2 = '"'"hello"'"'
# 可以使用转义字符操作
str_3 = 'I\'m \"OK\"!'
str_4 = 'ni\nhao'
# 使用 r'' 包裹的字符串默认不转义
str_5 = r'ni\nhao'
# 当内容较多时，使用 \n 不好阅读，可以使用 '''...''' 表示多样内容
str_6 = '''Dear xiaoMing
    Long time no see, I'm want in the park today.
So, How are you today?'''
print(str_2)
print(str_3)
print(str_4)
print(str_5)
print(str_6)
# 布尔值 True False
true = True
false = False
print('3 > 2', 3 > 2)
print('2 > 3', 2 > 3)
# 可以使用 and or not 运算
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)
print(not False)
# 空值 None，特殊空值，不能理解为 0
null = None
# 变量 = 是赋值语句
# 整数
a = 1
# 字符串
b = 'str'
# 布尔值
answer = True
# 常量，大写表示，依然可以被修改，只是用法定义
PI = 3.14
# 运算符
# 默认除法结果是浮点数，即使恰好整除也是浮点数
print(10 / 3)
# 地板除（直接舍去小数部分），要想得到整数，可以使用 //，如果被除数是浮点数，那么得到的还是有 .0 结尾的浮点数
print(10 // 3)
print(3.0 // 2)
# 余数计算
print(10 % 3)
