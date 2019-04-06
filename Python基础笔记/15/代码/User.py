class User:
    def __init__(self,record):
        """
        将住宿记录转换为对象
        :param record: 列表，一条住宿及记录
        """
        keys = ['name','ID','sex','birthday','address','zipcode','mobile','phone1','phone2','email','other']
        self.__dict__.update(dict(zip(keys,record)))      # 获取得到一个字典：{'name':"tom",'ID':"234234234243234".......}
    def __str__(self):
        return "{:8}{:20}{:4}{:10}{:30}{:8}{:14}{:10}{:10}{:20}{:2}".format(self.name,self.ID,self.sex,self.birthday,self.address,self.zipcode,self.mobile,self.phone1,self.phone2,self.email,self.other)
if __name__ == "__main__":
    user = User()






















