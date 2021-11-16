# flyweight_1.py
class User:

    def __init__(self, name='', age=''):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
    
    def __str__(self):
        return f'name: {self.name}, age: {self.age}'


# FlyWeightFactory
class UserFactory:

    __instances = {}

    @classmethod
    def get_instance(cls, id):
        if id not in cls.__instances:
            user = User()
            cls.__instances[id] = user
            return user
        return cls.__instances.get(id)

user1 = UserFactory.get_instance(1)
user1.name = 'Taro'
user1.age = 20

user2 = UserFactory.get_instance(2)

user3 = UserFactory.get_instance(1)

print(id(user1))
print(id(user2))
print(id(user3))
print(user3)
user3.name = 'Hanako'
print(user1)