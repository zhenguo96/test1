class Dog:
    pass
# 给对象动态添加属性
dog = Dog()
dog.name = 'asod'
dog.age = 5
print(dog.__dict__)

# 动态增加方法
def bark(self):
    print("www")
dog.bark = bark
# dog.bark(dog)
from types import MethodType
dog.bark = MethodType(bark,dog)     # 把函数绑定给对象
dog.bark()
# 动态绑定是针对特定对象，不是针对所有对象
dog1 = Dog()
# print(dog1.name)
# dog1.bark()

# 给类绑定实例方法
Dog.bark = bark
dog1.bark()









