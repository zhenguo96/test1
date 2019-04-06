class Student:
    # 类属性
    stu_num = 0
    __num = 5   #私有类属性，不能通过类名和对象直接存取
    @classmethod
    def set_num(cls,num):  #class
        # print(cls)
        cls.__num = num
    @classmethod
    def get_num(cls):
        return  cls.__num
Student.set_num(30)
print(Student.get_num())