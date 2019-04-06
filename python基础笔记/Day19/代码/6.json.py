import json
# python 转json字符串
d1 = [1,2,3,4]
res = json.dumps(d1)
print(res,type(res))

# 从json文件中加载
with open("json/city.json",encoding="utf-8") as fp:
    city = json.load(fp)

# 将json对象写入文件
d1 = {"name":"asdjf", "age":32}
# with open('1.txt','w') as p:

















