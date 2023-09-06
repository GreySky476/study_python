# 条件判断
# if 语句从上往下判断，如果有个判断是 True，该 command 执行后就忽略掉其它 condition
age = 0
if age > 0:
    print(f'you age is {age}')
elif age == 0:
    print('you are baby')
else:
    print('oh, you age is bad')
# if 简写
# 当变量为非零、非空字符串、非空 list 等就为 True，否则为 False
if age:
    print('True')
else:
    print('False')
# input 结合 if
birth = input('birth: ')
# input 输入默认是 string 类型，所以需要 int() 函数转换，当然 int() 只能转化合法数字，不合法一样报错
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')
'''
习题
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
height = 1.75
weight = 80.5
bmi = weight / height
print(f'bmi: {bmi}')
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi < 32:
    print('肥胖')
elif bmi >= 32:
    print('严重肥胖')
