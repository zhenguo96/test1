# 8
# 使用密码表加密
# 密码表加密是一种十分常用的密码加密方法，加密的原理是根据明文和密码表，加密形成密文，根据密文和密码表解密，读出明文。密码表可以是如下表所示：
# 自己设计密码表，任意输入一个字符串，然后显示其密文。运行输入如下所示：
s = list(input("请输入英文加数字："))
p = []
mingwen = list("abcdefghijklmnopqrstuvwxyz1234567890")
miwen = list  ("18ac4y7bxuiep23hjs5ofwv0zdl9gkm6nqrt")
for j in range(len(s)):
    for i in range(len(mingwen)):
        if s[j] == mingwen[i]:
            p.append(miwen[i])
print("".join(p))



