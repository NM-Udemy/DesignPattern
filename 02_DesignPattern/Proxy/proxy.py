# proxy.py

from abc import ABC, abstractmethod
import time


class APICaller(ABC):

    @abstractmethod
    def request(self):
        pass


class RealAPICaller(APICaller):

    # 処理の重いコンストラクタとする
    def __init__(self, url):
        self.__url = url
        time.sleep(5)
    
    def request(self):
        print('APIを呼び出す')
        return


class RealAPICallerProxy(APICaller):

    def __init__(self, url):
        self.__url = url
    
    def __check_access(self):
        print('アクセスに成功しました')
        return True
    
    def __write_log(self):
        print('ログを出力します')
    
    def request(self):
        if self.__check_access():
            real_api_caller = RealAPICaller(self.__url)
            real_api_caller.request()
            self.__write_log()

# caller = RealAPICaller('http://api.com')
# caller.request()

proxy = RealAPICallerProxy('https://api.com')
proxy.request()