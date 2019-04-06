class Singleton:
    __instance = None   # 保存已经实例的对象引用

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:      # 未实例化对象
            cls.__instance = object.__new__(cls,*args,**kwargs)
        return cls.__instance














