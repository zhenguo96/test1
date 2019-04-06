try:
    # 5 / 1
    fp = open("1.txt",'r')
    fp.write("hello")
except:
    pass
# except BaseException as e:
#     print(e)
# except:
#     pass
# finally:
#     print("必须得走这个模块")
#     print("任务清理")
fp.close()
print("====="*10)





