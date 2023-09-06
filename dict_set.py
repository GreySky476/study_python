# dict 字典，其它语言称作 map(key -value)
d = {'A': 65, 'B': 66, 'C': 67}
print(d['A'])
# 直接使用 dict['key'] 方式访问 key 时，一旦 key 不存在就会报错，所以可以使用其它方式访问
# get('key', default value)，当 key 不存在时，返回 None，如果指定了返回值，则返回
print(d.get('D', 68))
# in 通过 in 判断 key 是否存在，返回 True | False
print('D' in d)
# 一个 key 只能对应一个 value，多次赋值会一次覆盖
d['A'] = 63
d['A'] = 64
print(d['A'])
# 删除 key 使用 pop()，对应的 value 也会删除
d.pop('A')
print('A' in d)
print(d)
'''
dict 特点
查找和插入速度极快，不会随着 key 的增加而变慢
需要大量内存，浪费多
list 特点，基本与 dict 相反
查找和插入随着元素增加而增加
占用空间小
即 dict 是一种空间换时间的方法
dict 的 key 必须是不可变对象！！！
原因：需要通过 key 来计算 value，为了保证 hash 正确性，key 不能变
'''
# set，与 dict 类似，不存储 value，key 不能重复
s = {1, 2, 3}
print(s)
s = {1, 1, 2, 3, 4, 2}
# 重复元素在 set 中会被过滤
print(s)
# 添加元素 add()，添加重复元素没有效果
s.add(5)
s.add(3)
s.add(2)
print(s)
# remove(key) 使用 remove 可以删除元素
s.remove(5)
print(s)
# set 可以看做无序和无重复元素的交集，因此，两个 set 可以做数学意义上的交集并集操作
s1 = {1, 2, 3}
s2 = {1, 2, 4}
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)
# 不可变对象 str 是不可变对象，list 是可变对象
# 可变对象
list_1 = [1, 3, 2, 4]
# 排序操作
list_1.sort()
# 数组顺序发生改变
print(list_1)
str_a = 'abc'
# 替换字符操作
str_b = str_a.replace('a', 'A')
# str_a 并没有发生改变，replace 生成了一个新的 str 对象
print(str_a)
print(str_b)
