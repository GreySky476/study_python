# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(len('中文'.encode('utf-8')))
# 获取字符的整数表示 ord()，把编码转换成对应字符 chr()
num = ord('中')
num = ord('文')
print(num)
print(chr(num))
# 如果知道字符的整数编码，还可以用十六进制编写
str_num = '\u4e2d\u6687'
print(str_num)
# 字符串格式化 %d 整数，%f 浮点数，%s 字符串，%x 十六进制整数
str_1 = 'Hello, %s' % 'world'
print(str_1)
str_2 = 'Hi, %s you have $%d' % ('anna', 1000)
print(str_2)
# 整数、浮点数格式化指定是否补 0 与小数位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926535)
# 想表示 % 是个普通字符可以使用 %%
print('hello %s %%' % 'world')
# 或者使用 format() 进行格式化，方法会依次替换 {0} {1} ...
print('hello{0}{1}'.format(', ', 'world'))
# f-string 以 f 为开头的字符串，字符串中如果包含 {xxx}，就会以对应的变量 xxx 替换
r = 3
# 3.14 * 2.5 的 2 次方
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r:2d} is {s:.2f}')
# 小明的成绩从去年的 72 分提升到了今年的 85 分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
r = (85 - 72) / 85 * 100
print('XiaoMing up the rate is %.2f%%' % r)
