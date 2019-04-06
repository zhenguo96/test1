class Student:
    # 类属性
    stu_num = 0
    __num = 5
    @classmethod
    def set_num(cls,num):   #class
        print(cls)
        cls.__num = num
    @classmethod
    def get_num(cls):
        return cls.__num
    @staticmethod
    def demo():
        print("静态方法")
    def demo(self):
        print("实例方法")
    def t(self):
        print(self)
"""
类方法和实例方法的区别
1.类方法@classmethod定义，实例不需要
2.参数不同，类方法第一个参数是cls，代表当前类；实例方法第一个参数是cls，代表当前对象
3.调用方式不同，类方法可以通过类名和对象名调用，但实例方法只能通过对象调用

"""
stu = Student()
stu.set_num(30)
print(Student.get_num())
stu.t()

# 静态方法的调用方式
# Student.demo()
# 如果静态方法和实例方法同名，实例方法优先
stu.demo()











