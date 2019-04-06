class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("吃")
class Cow(Animal):
    def eat(self):
        print("吃的是草，挤得是奶")
# 类信息
# print(Cow.__name__)     # 获取类名字符串
# print(Cow.__dict__)     #
# print(Cow.__bases__)    # 获取父类
# print(Cow.__mro__)      # 继承顺序
#
cow = Cow("huahua")
# print(cow.__dict__)     # 获取对象自己的属性和值的字典
cow.age = 5
# print(cow.__dict__)
cow.__dict__.update({'sex':'mmmm','colour':'black'})
# print(cow.__dict__)
# print(dir(cow))

# isinstance
print(type(cow) == Animal)      # 不能判定子类对象属于父类
print(isinstance(cow,Animal))   # 可以判断子类对象属性属于父类

# subclass
print(isinstance(Cow,Animal))   # T
print(isinstance(int,Animal))   # F





