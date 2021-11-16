# interface_segregation.py
from abc import ABCMeta, abstractmethod

# class Athlete(metaclass=ABCMeta):

#     @abstractmethod
#     def swim(self):
#         pass

#     @abstractmethod
#     def high_jump(self):
#         pass

#     @abstractmethod
#     def long_jump(self):
#         pass

# class Athlete1(Athlete):

#     def swim(self):
#         print('I swim')
    
#     def high_jump(self):
#         pass

#     def long_jump(self):
#         pass

class Athlete(metaclass=ABCMeta):
    pass

class SwimAthlete(Athlete):
    @abstractmethod
    def swim(self):
        pass

class JumpAthlete(Athlete):
    @abstractmethod
    def high_jump(self):
        pass

    @abstractmethod
    def long_jump(self):
        pass

class Athlete1(SwimAthlete):
    def swim(self):
        print('I swim')

class Athlete2(SwimAthlete, JumpAthlete):

    def swim(self):
        print('I swim')

    def high_jump(self):
        print('I high jump')

    def long_jump(self):
        print('I long jump')

john = Athlete1()
john.swim()

yuji = Athlete2()
yuji.high_jump()