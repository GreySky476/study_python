# 循环，for..in
names = ['A', 'B', 'C']
for name in names:
    print(name)
sum_num = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum_num = sum_num + x
print(sum_num)
# 计算 1-100 整数和，range() 函数生成一个整数序列，该序列小于当前指定值，再通过 list() 可转化成 list
print(range(5))
print(list(range(5)))
# 计算 1-100 和
sum_num = 0
for x in list(range(101)):
    sum_num = sum_num + x
print(f'1-100 sum: {sum_num}')
# while 循环
condition_num = 99
sum_num = 0
while condition_num > 0:
    sum_num = sum_num + condition_num
    condition_num = condition_num - 2
print(sum_num)
'''
练习
    请利用循环依次对list中的每个名字打印出Hello, xxx!：
'''
L = ['Bart', 'Lisa', 'Adam']
for e in L:
    print(f'Hello, {e}')
# break
n = 1
while n <= 100:
    if n > 10:
        break
    n = n + 1
print(n)
# continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
