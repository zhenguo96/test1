# 3.自定义一个字典类，完成：
# - add(self,key,value) 添加键值对到字典
# - get(self,key)获取键对应的值
# - update(self,dict1)合并另外一个字典到当前字典中
class Dict1():
    def __init__(self):
        self.dic = {}
    def add(self,key,vale):
        self.dic[key] = vale
        return self.dic
    def get(self,key):
        return self.dic.get(key)
    def update(self,dict1):
        self.dic.update(dict1)
        return self.dic
d = Dict1()
print(d.add("name",'tom'))
print(d.get("name"))
print(d.update({"age":18}))












