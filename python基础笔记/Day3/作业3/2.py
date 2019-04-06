# 2.假设用户名为admin，密码为123abc,从控制台分别输入用户名和密码，如果和已知用户名和密码都匹配上的话，则验证成功，否则验证失败
user = "admin"
passwd = "123abc"
inputuser = input("用户名：")
if inputuser == "":
    print("账号不能为空")
    exit()
inputpasswd = input("密码：")
if inputuser == user and inputpasswd == passwd:
    print("登陆成功！")
else:
    print("账号或密码错误")













