class User:

    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level
    
    def set_name(self, new_name):
        self.__name = new_name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__admin_access_level = 'admin'

    def get_access_level(self):
        # Возвращаем admin для админа
        return self.__admin_access_level

    def add_user(self, users_list, user):
        if isinstance(user, User) and user not in users_list:
            users_list.append(user)
            print(f"Добавлен пользователь {user.get_name()}")
        else:
            print("Ошибка: объект не User или уже в списке.")

    def remove_user(self, users_list, user_id):
        for user in users_list:
            if user.get_id() == user_id:
                users_list.remove(user)
                print(f"Пользователь {user.get_name()} удалён.")
                return
        print("Пользователь с таким ID не найден.")

# Пример работы
user1 = User(123, "Nick")
user2 = User(456, "Olga")
user3 = User(789, "John")
users_list = [user1, user2, user3]
admin1 = Admin(1001, "Anna")

print("Список пользователей:")
for user in users_list:
    print(user.get_id(), user.get_name(), user.get_access_level())

print("\nАдмин добавляет нового пользователя:")
new_user = User(321, "Max")
admin1.add_user(users_list, new_user)

print("\nСписок пользователей после добавления:")
for user in users_list:
    print(user.get_id(), user.get_name(), user.get_access_level())

print("\nАдмин удаляет пользователя с ID 456:")
admin1.remove_user(users_list, 456)

print("\nСписок пользователей после удаления:")
for user in users_list:
    print(user.get_id(), user.get_name(), user.get_access_level())
    

