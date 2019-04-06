class Person():
    def __init__(self,damage,xie):
        self.damage = damage
        self.xie = xie
    def da(self):
        dog1.xie -= p1.damage
        return dog1.xie
class Dog():
    def __init__(self,damage,xie):
        self.damage = damage
        self.xie = xie
    def yao(self):
        p1.xie -= dog1.damage
        return p1.xie
p1 = Person(1,10)
p2 = Person(1,10)
dog1 = Dog(2,5)
dog2 = Dog(2,5)
dog3 = Dog(2,5)
p = []
p.extend([[p1.damage, p1.xie], [p2.damage, p2.xie]])
d = []
d.extend([[dog1.damage, dog1.xie], [dog2.damage, dog2.xie], [dog3.damage, dog3.xie]])
def fight():
    while 1:
        res1 = p1.da()
        d[0][1] = res1
        print("人打狗，狗剩余血量：%d" % d[0][1])
        if d[0][1] <= 0:
            print("狗死亡")
            del d[0:1]
        elif p[0][1] <= 0:
            del p[0:1]
            print("人死亡")
        if p == [] or d == []:
            break
        res2 = dog1.yao()
        p[0][1] = res2
        print("狗咬人，人剩余血量：%d" % p[0][1])
        if d[0][1] <= 0:
            print("狗死亡")
            del d[0:1]
        elif p[0][1] <= 0:
            del p[0:1]
            print("人死亡")
        if p == [] or d == []:
            break
fight()











