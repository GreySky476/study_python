"""
面向对象的概念就是类（class）和实例（instance）
类是抽象的模块
实例是根据类创建一个个具体的『对象（个体）』
对象三大特性：封装、继承、多态
"""


# class  『类名』(object): 其中 object 表示继承自该类
class Student(object):
    pass


ana = Student()
# <__main__.Student object at 0x100e92370> 实例和相关内存地址
print(ana)
# <class '__main__.Student'> 命名空间
print(Student)
# 给实例 ana 绑定一个 name 属性
ana.name = 'ana'
print(ana.name)


# 因为类有模板的作用，可以在创建实例的时候把一些认为必须绑定的属性强制填写进去，通过 __init__ 方法
class StudentInit(object):
    # 和普通函数相比，在类中定义的函数只有一点不同，第一个参数永远是实例变量 self，调用时并不需要传递该参数
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'D'


ana = StudentInit('ana', 80)
print(ana.name)
print(ana.score)

"""
数据封装
面向对象有个重要特点就是数据封装，上面的 StudentInit 类中，初始化的实例拥有各自的 name 和 score，我们可以直接通过函数访问。
定义方法 print_score，打印实例的属性(name、score)
"""
# 这样依赖，从外部看的话创建实例只需要 name 和 score，而如何打印都是类里面定义的细节，这些数据和逻辑都被『封装』起来
ana.print_score()
# 类还方便添加其它方法（函数），创建实例只管使用，无需考虑其它
print(ana.get_grade())

"""
类是创建实例的模板，而实例是一个个具体的对象，各个实例拥有的数据互相独立，互不影响
方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据
通过实例调用方法，可以直接操作对象内部数据，而无需直到方法细节
python 允许对实例变量绑定任何数据，所以，对于相同的实例变量，拥有的变量名称可能不同（比较灵活，但是增加了复杂度和调用难度）
"""


