class Lycparse:
    def __init__(self,name):
        self.name = name

class Views:
    def jiexi(self):
        fp = open(ly.name,encoding="utf-8")
        d = fp.readlines()
        data = [line.strip() for line in d]
        # print(data)
        datalist = []
        for i in range(len(data)):
            a = data[i].split("]")
            # print(a)
            for j in range(len(a)-1):
                datatimestr = a[j][1:]
                # print(datatimestr)
                datatimelist = datatimestr.split(":")
                datatime = float(datatimelist[0]) * 60 + float(datatimelist[1])
                datalist.extend([[datatime,a[-1]]])
                print(datatime)
        sortdatalist = sorted(datalist,key=(lambda x:x[0]))
        print(sortdatalist)
        inp = float(input("输入时间："))
        for v in range(len(sortdatalist)-1):
            if sortdatalist[v][0] <= inp < sortdatalist[v+1][0]:
                print(sortdatalist[v][1])
                break
        fp.close()

class ChuanQi(Lycparse):
    def __init__(self,name='chuanqi.txt'):
        super().__init__(name)

class MiMi(Lycparse):
    def __init__(self,name='qfile.txt'):
        super().__init__(name)

cq = ChuanQi()
mm = MiMi()
ly = Lycparse(mm.name)
views = Views()
views.jiexi()


