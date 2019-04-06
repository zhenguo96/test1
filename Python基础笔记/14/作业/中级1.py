class Person():
    __males = 0
    __famales = 0
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        if self.__gender == "男":
            self.__class__.__males += 1
        elif self.__gender == "女":
            self.__class__.__famales += 1
    @classmethod
    def number_male(cls):
        return cls.__males
    @classmethod
    def number_pemales(cls):
        return cls.__famales

p1 = Person("tom",18,"男")
print(Person.number_male())
print(Person.number_pemales())













