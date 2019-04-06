try:
    try:
        # raise后面必须是异常类的对象
        raise ZeroDivisionError("除零错误")
    except ZeroDivisionError as e:
        print(e)
        raise       # 原样抛出
    except:
        pass
except ZeroDivisionError as e:
    print("外层")
print("9"*60)










