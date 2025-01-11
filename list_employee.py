# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет
# сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID),
# имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).


# Класс User - базовый
class User():
    def __init__(self, id, name):
        self.__id = id                    # ID сотрудника
        self.__name = name                # сотрудника
        self.__access_level = "user"      # сотрудника

    # Получение информации о сотруднике
    def get_info(self):
        return self.__id, self.__name, self.__access_level


# Класс Admin - дочерний
class Admin(User):
    def __init__(self, id, name, admin_level):
        super().__init__(id, name)
        self.__admin_level = admin_level
        self.list_employee = {}
        self.last_id = 1

    # Добавление нового сотрудника
    def add_user(self, name):
        self.last_id += 1
        list_employee[self.last_id] = User(self.last_id, name)

    


    # Увольнение сотрудника
    def remove_user(self, name):
        pass

    # Установка уровня доступа "admin" сотруднику
    def set_access(self, level):
        self.__access_level = level

    # Получение уровня доступа сотрудника
    def get_access(self):
        return self.__access_level

list_employee = {}
last_id = 0

list_employee[last_id + 1] = Admin("Чухланцев Александр", "admin")
last_id += 1


# Запускаем цикл общения с пользователем
while True:
    print("1 - Добавить сотрудника")
    print("2 - Отметить задачу выполненной")
    print("3 - Вывести список текущих задач")
    print("4 - Завершить программу")

    num = input("Выберите действие: ")

    match num:
        case "1":
            id = input("Введите ваш ID: ")
            if id in list_employee and list_employee[int(id)].access == "admin":
                name = input("Введите ваше имя")
                access = input("Введите ваш доступ")
                last_id += 1

            while True:
                deadline = input("Введите срок выполнения в формате ДД:ММ:ГГ: ")
                obj = Check(deadline)
                print(obj.date)
                if not obj.check_date():
                    del obj
                    print("Неверный формат даты")
                else:
                    del obj
                    break
            menager.add(description, deadline)
        case "2":
            menager.print_tasks()
            index = int(input("Введите индекс выполненной задачи: "))
            menager.completed(index)
        case "3":
            menager.print_tasks()
        case "4":
            menager.exit()
            break
        case _:
            print("Такого действия нет. Повторите выбор.")


