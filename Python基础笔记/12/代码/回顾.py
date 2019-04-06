# def magic(func):
#     def inner():
#         func()
#         print("我喜欢吃炸鸡")
#         print("我喜欢山珍海味")
#     return inner
# @magic # eat = magic(eat)
# def eat():
#     print("我喜欢吃水果")
# eat()

# class Aniaml:
#     def __init__(self,name,life,atk):
#         self.name = name
#         self.life = life
#         self.atk = atk  # 攻击力
#     def attack(self,enemy):
#         enemy.life -= self.atk
#         print("{}攻击了{},掉了{}血".format(self.name,enemy.name,self.atk))
# class Dog(Aniaml):
#     def bite(self,enemy):
#         self.attack(enemy)
# class Person(Aniaml):
#     def beat(self,enemy):
#          self.attack(enemy)
# class Game:
#     def __init__(self,personNum,dogNum):
#         self.pNum = personNum  #人的数目
#         self.dNum = dogNum   #狗的数目
#         self.persons = []  # 保存人的对象
#         self.dogs = []     # 保存狗的对象
#         self.__dog_factory()
#         self.__person_factory()
#     def main(self):
#         from random import randint as rd
#         while len(self.persons) > 0 and len(self.dogs) > 0:
#             self.persons[rd(0,len(self.persons)-1)].beat(self.dogs[rd(0,len(self.dogs)-1)])
#             self.dogs[rd(0,len(self.dogs)-1)].bite(self.persons[rd(0,len(self.persons)-1)])
#             #判定死亡
#             for i in range(len(self.persons)-1,-1,-1):
#                 if self.persons[i].life <= 0:  #如果生命值小于0，删除
#                     print("{}阵亡了".format(self.persons[i].name))
#                     self.persons.pop(i)
#             for j in range(len(self.dogs)-1,-1,-1):
#                 if self.dogs[j].life <= 0:
#                     print("{}死掉了".format(self.dogs[j].name))
#                     self.dogs.pop(j)
#     # 工具方法
#     def __person_factory(self):
#         for i in range(self.pNum):
#             self.persons.append(Person('人'+str(i+1),1500,30))
#     def __dog_factory(self):
#         for i in range(self.dNum):
#             self.dogs.append(Dog('狗'+str(i+1),100,50))
# if __name__ == "__main__":
#     game = Game(2,3)
#     game.main()


class Animal():
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    def attack(self,enemy):
        enemy.hp -= self.atk
        print("{}攻击了{}，掉了{}血".format(self.name,enemy.name,self.atk))
class Person(Animal):
    def pbite(self,enemy):
        self.attack(enemy)
class Dog(Animal):
    def dbite(self,enemy):
        self.attack(enemy)
class Fight():
    def __init__(self,num1,num2):
        self.persons = num1
        self.dogs = num2
        self.p = []
        self.d = []
        self.get_person()
        self.get_dog()
    def gan(self):
        from random import randint as r
        while len(self.p) > 0 and len(self.d) > 0:
            self.p[r(0,(len(self.p)-1))].pbite(self.d[r(0,(len(self.d)-1))])
            self.d[r(0,(len(self.d)-1))].dbite(self.p[r(0,(len(self.p)-1))])
            for i in range(len(self.p)-1,-1,-1):
                if self.p[i].hp <= 0:
                    print("{}死了".format(self.p[i].name))
                    self.p.pop(i)
            for j in range(len(self.d)-1,-1,-1):
                if self.d[j].hp <= 0:
                    print("{}死了".format(self.d[j].name))
                    self.d.pop(j)
    def get_person(self):
        for i in range(self.persons):
            self.p.append(Person('人'+str(i+1),200,70))
    def get_dog(self):
        for i in range(self.dogs):
            self.d.append(Dog('狗'+str(i+1),200,70))
if __name__ == '__main__':
    fight = Fight(2,3)
    fight.gan()





