class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = "user"

    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._name

    def get_user_level(self):
        return self._level

    def set_user_name(self, name):
        self._name = name

    def set_user_id(self, user_id):
        self._user_id = user_id


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = "admin"

    def add_user(self, list_users, user):
        list_users.append(user)
        print("Пользователь успешно добавлен в список")
        print(list_users)

    def remove_user(self, list_users, user):
        list_users.remove(user)
        print("Пользователь успешно удален из списка")
        print(list_users)

list_users = []
admin = Admin("a1", "Gosha")
user1 = User("u1", "Alex")
user2 = User("u2", "Bob")
user3 = User("u3", "Charli")
user4 = User("u4", "David")
user5 = User("u5", "Eric")

print(user1.get_user_name())
print(user3.get_user_id())
print(user5.get_user_level())

print(admin.add_user(list_users, user1))
print(admin.add_user(list_users, user2))
print(admin.add_user(list_users, user3))
print(admin.add_user(list_users, user4))
print(admin.add_user(list_users, user5))

print(admin.remove_user(list_users, user3))

print(admin.add_user(list_users, user3))

