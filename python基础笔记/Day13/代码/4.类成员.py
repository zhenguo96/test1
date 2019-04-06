# 类属性和类方法
class Student:
    # 类属性
    stu_num = 0
    __num = 5
    def __init__(self,name,age):
        # 对象属性，实例属性
        self.name = name
        self.age = age
        # self.__class__获取对象所属的类
        self.__class__.stu_num += 1
    def __del__(self):
        self.__class__.stu_num -= 1
    # def change_num(self,num):
    #     self.stu_num += 10      # 引用类属性可以使用self.类属性名
# obj1 = Student("tom",20)
# obj1.change_num(10)
# 也可以直接类名引用类属性
# print(Student.stu_num)
# 也可以通过对象引用类属性
# print(obj1.stu_num)
# 不能存取私有类属性
# print(Student.__num)
obj1 = Student("tom",20)
obj2 = Student("tom",20)
obj3 = Student("tom",20)
obj4 = Student("tom",20)
print(obj1.stu_num)






