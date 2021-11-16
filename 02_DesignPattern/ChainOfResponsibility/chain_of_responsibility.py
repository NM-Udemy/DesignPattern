# chain_of_responsibility.py
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    gender: str


class Handler(ABC):

    _next = None

    def set_next(self, handler):
        self._next = handler
        return handler
    
    def handle(self, user:User):
        # filterがTrueだった場合
        if self.filter(user):
            return self.done(user)
        # nextが存在する場合はnextのhandleを実行
        if self._next:
            return self._next.handle(user)
        return self.end(user)

    @abstractmethod
    def filter(self, user:User):
        pass

    def done(self, user: User):
        print(f'{user}は{self.__class__.__name__}でフィルタリングされました')
        return False

    def end(self, user: User):
        print(f'{user}の確認は完了しました')
        return True

class NameCheckHandler(Handler):
     
    def filter(self, user:User):
        if user.name in ['', None, 'Nanashi']:
            return True
        return False

class AgeCheckHandler(Handler):

    def filter(self, user: User):
        if (user.age < 0) or (user.age > 100):
            return True
        return False

    def done(self, user: User):
        print(f'年齢が0より小さいか、100より大きいです')
        return False

class GenderCheckHandler(Handler):

    def filter(self, user: User):
        if user.gender not in ['Man', 'Woman']:
            return True
        return False

user1 = User('Name', 20, 'M')
user2 = User('Name', 20, 'Man')
user3 = User('', 20, 'Man')
user4 = User('Name', 120, 'Man')
user5 = User('Hanako', 20, 'Woman')

name_handler = NameCheckHandler()
age_handler = AgeCheckHandler()
gender_handler = GenderCheckHandler()

name_handler.set_next(age_handler).set_next(gender_handler)

name_handler.handle(user1)
# Nameのチェック、ageのチェック、genderのチェックを順番に実行してくれる
valid_users = []
for user in [user1, user2, user3, user4, user5]:
    if name_handler.handle(user):
        valid_users.append(user)
print(valid_users)