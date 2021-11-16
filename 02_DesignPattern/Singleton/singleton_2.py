class DataBase:

    __instance = None

    def __init__(self):
        raise RuntimeError('このクラスのコンストラクタは呼び出せません')
    
    @classmethod
    def get_instance(cls, database_url=None):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
        if database_url:
            cls.__instance.__database_url = database_url
        return cls.__instance
    
    @property
    def database_url(self):
        return self.__database_url
    
    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url
    
    def connect(self): # Databaseに接続
        pass

a = DataBase.get_instance('128.1.1.1:1111')
b = DataBase.get_instance()
print(a==b)
print(id(a), id(b))
print(a.database_url, b.database_url)
a.database_url = '128.1.1.1:5678'
print(a.database_url, b.database_url)
