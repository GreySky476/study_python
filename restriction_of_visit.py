"""
访问限制
在 class 内部有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，隐藏了复杂逻辑
单数之前的例子外部代码还是可以自由修改一个实例的属性
"""
# 在 python 中，不想让内部属性被外部访问，可以在属性名称前面加 __ 双下划线，这样就成了私有变量，只有内部能访问


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        # 参数校验
        if score < 0:
            raise ValueError('Bad score')
        self.__score = score


bob = Student('bob', 59)
# 'Student' object has no attribute '__name'
# print(bob.__name)
# 这种方式确保了代码的健壮性，如果外部代码要获取相关属性，可以提供 get_xx 方法
print(bob.get_score())
print(bob.get_name())
# 修改可以提供 set_xx 方法
bob.set_name('ana')
bob.set_score(70)
print(bob.get_name())
print(bob.get_score())
# 大费周折定义方法获取相关属性是为了方便做参数处理，可以对参数做检查
# Bad score
# bob.set_score(-1)
"""
在 python 中，__xxx__ 以双下划线开头并结尾的属于特殊变量，是可以直接访问的
有时候会看到 _ 单下划线开头的变量，约定俗成把它视为私有变量，不要随意访问
双下划线开头的实例变量是可以被访问到的，只是 python 解释器将它改成了其它名字
"""
# 改名规则 _类名__xx（属性）,但强烈不推荐这样访问，因为不同的解释器改名规则也不同
# python 解释器不对使用者做出强制要求，一切靠自觉
print(bob._Student__name)
# 以下使用实例的错误写法
grey = Student('grey', 80)
print(grey.get_name())
# 这里的赋值并没有修改到 grey 实例里面的 __name 属性，因为解释器已经把它改名了，所以这里属于是新增了一个 __name 变量
grey.__name = 'zoo'
# 所以这里的结果并不相同
print(grey.__name)
print(grey.get_name())
"""
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
"""


class Student_exercise(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender != 'male' and gender != 'female':
            raise ValueError('Bad gender')

        self.__gender = gender


# 测试:
bart = Student_exercise('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
