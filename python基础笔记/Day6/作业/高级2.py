# 2凯撒密码：
str1 = "vRqfh pruh lqwr wkh euhdfk,ghdu iulhqgv,rqfh pruh; Ru forvh wkh zdoo xs zlwk rxu Hqjolvk ghdg.Lq shdfh wkhuh'v qrwklqj vr ehfrphv d pdq Dv prghvw uwlooqhvv dqg kxplolwb:Exw zkhq wkh eodvw ri zdu eorzv lq rxu hduv, Wkhq lplwdwh wkh dfwlrq ri wkh wljhu; Vwliihq wkh vlqhzv,vxpprq xs wkh eorrg."
l = "abcdefghijklmnopqrstuvwxyz"
str3 = str1.lower()
list1 = list(str3)
list2 = list(l)
str2 = ""
for i in range(len(list1)):
    if list1[i].isalpha():
        str2 +=list2[list2.index(list1[i]) - 3]
    else:
        str2 += list1[i]
print(str2)


