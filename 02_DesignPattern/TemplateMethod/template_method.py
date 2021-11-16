from abc import ABC, abstractmethod


# Abstract Class
class AbstractDisplay(ABC):

    def display(self):
        self._open()
        for _ in range(5):
            self._print()
        self._close()
        self._additional_method()
    
    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _print(self):
        pass

    @abstractmethod
    def _close(self):
        pass

    # 継承先で定義してもいいししなくてもいい
    def _additional_method(self):
        pass


# Concrete Class
class CharDisplay(AbstractDisplay):

    def __init__(self, character):
        self.__character = character
    
    def _open(self):
        print('<<', end='')
    
    def _print(self):
        print(self.__character, end='')
    
    def _close(self):
        print('>>')
    
    def _additional_method(self):
        print('Addtional method called')


class StringDisplay(AbstractDisplay):

    def __init__(self, msg):
        self.__msg = msg
    
    def _open(self):
        self.__print_line()
    
    def _print(self):
        print('|' + self.__msg + '|')
    
    def _close(self):
        self.__print_line()

    def __print_line(self):
        print('+' + '-' * len(self.__msg) + '+')

c_display = CharDisplay('*')
c_display.display()

s_display = StringDisplay('Hello')
s_display.display()