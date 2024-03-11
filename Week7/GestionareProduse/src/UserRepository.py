from AbstractClass import IRepository
from User import User

class UserRepository(IRepository):

    def __init__(self):
        self.users = []

    def create(self, data: dict):
        user_id = len(self.users) + 1
        user = User(user_id, **data)
        self.users.append(user)

    def read(self, entry_id):
        for user in self.users:
            if user.user_id == entry_id:
                print(f'ID: {user.user_id}, Name: {user.name}, Email: {user.email}')
                return
        print(f"The user with id {entry_id} is not available.")

    def update(self, entry_id, new_data: dict):
        for user in self.users:
            if user.user_id == entry_id:
                user.name = new_data.get('name', user.name)
                user.email = new_data.get('email', user.email)
                print(f'The user with id {entry_id} has been updated')
                return
        print(f'The user with id {entry_id} is not available.')

    def delete(self, entry_id):
        for user in self.users:
            if user.user_id == entry_id:
                self.users.remove(user)
                print(f'The user with the id {entry_id} was deleted')
        print(f'The user with id {entry_id} is not available.')