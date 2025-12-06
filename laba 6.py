class UserAccount:
    def __init__(self,username , email, password):
        self.username = username
        self.__password = password
        self.email = email

    def set_password(self,new_password):
        self.__password = new_password
        return f'Пароль успешно изменен'

    def check_password(self, password):
        return password == self.__password

    def user_info(self):
        return f'\nUsername: {self.username}\nEmail: {self.email}'

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f'\nМарка: {self.make}\nМодель: {self.model}'

class Car(Vehicle):
    def __init__(self,make, model, fuel_type):
        self.fuel_type = fuel_type
        self.make = make
        self.model = model
    def get_info(self):
        return f'\nМарка: {self.make}\nМодель: {self.model}\nВид топлива:{self.fuel_type}'


# username = input("Введите ваше имя: ")
# password = input("Придумайте пароль: ")
# email = input("Введите email: ")
#
# user = UserAccount(username, email ,password)
# suc_password = input("Подтвердите пароль: ")
# if user.check_password(suc_password):
#     print('Успешно')
#     print('Аккаунт создан',user.user_info())
# else:
#     print('Пароли не совпадают')
# try:
#     re_password = int(input('хотите поменять пароль?\nда-1         нет-0\n'))
#
#     if re_password == 1:
#
#         print('Изменение пароля')
#         new_password = input("Введите новый пароль: ")
#         user.set_password(new_password)
#         check_new_password = input('Подтвердите новый пароль: ')
#         if user.check_password(check_new_password):
#             print("Новый пароль подтвержден!")
#         else:
#             print("Пароль не совпадает!")
#
#     else:
#         print('как скажешь')
#
# except ValueError:
#     print('Ошибка значений')

make = input('Введите марку автомобиля: ')
model = input('Введите модель автомобиля: ')
fuel_type = input('Тип топлива: ')
car = Car(make, model, fuel_type)
print(car.get_info())
