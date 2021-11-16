# adapter.py
from abc import ABC, abstractmethod


class ModelAdaptee(ABC):

    @abstractmethod
    def load_headers(self):
        pass

    @abstractmethod
    def yield_row(self):
        pass


class UserModel(ModelAdaptee):

    def __init__(self):
        self.__users = []
        self.__headers = ['Name', 'Age']

    def load_headers(self):
        return self.__headers
    
    def yield_row(self):
        for user in self.users:
            yield user
    
    @property
    def users(self):
        return self.__users
    
    def add_user(self, user: list):
        self.users.append(user)

# Adapter
class ModelAdapter(ABC):

    @abstractmethod
    def write_to_csv(self):
        pass

class UserModelAdapter(ModelAdapter):
    
    def __init__(self, user_model: UserModel):
        self.__user_model = user_model
    
    def write_to_csv(self, file_name):
        with open(file_name, mode='w', encoding='utf-8', newline='\n') as fh:
            csv_header = ','.join(self.__user_model.load_headers()) # [Name, Age] => Name,Age
            fh.write(csv_header + '\n')
            for row in self.__user_model.yield_row():
                csv_row = ','.join([str(r) for r in row])# => ['Taro', 19] => ['Taro', '19'] => Taro,19
                fh.write(csv_row + '\n')




users = UserModel()
users.add_user(['Taro', 19])
users.add_user(['Jiro', 19])
users.add_user(['Saburo', 19])

# print(users.load_headers())
# for user in users.yield_row():
#     print(user)
user_model_adapter = UserModelAdapter(users)
user_model_adapter.write_to_csv('tmp.csv')