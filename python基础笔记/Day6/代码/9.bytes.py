# 字节流字符串
import hashlib
# python 字符串
password = input("请输入你的密码：")
# python 转字节流字符串
res = password.encode("utf-8")
print(res,type(res))
print(password)
password = hashlib.md5(password.encode("utf-8")).hexdigest()
# print(password,type(password))
b1 = b'123'
# 字节流字符串转python字符串
res = b1.decode('utf-8')
print(res,type(res))



