try:
    print(5/0)
# 如果异常匹配到元组中任意一种，则执行对应处理
except(ZeroDivisionError,OverflowError) as e:
    print("异常处理")
except:     # 吞掉异常，不做任何处理
    pass
print("*"*89)



















