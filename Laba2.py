import sys
sys.path.append('C:\\Users\\iliaa\\OneDrive\\Рабочий стол\\LAB4')
from mypackage import strings
text = input("Enter a string: ")
print(strings.capitalize(text))

# #Первая задача
# name = input()
# def greet(name):
#     print('Hello, '+ name)
# greet(name)
# #Вторая задача
# number = int(input())
# def greet(number):
#     print(number**2)
# greet(number)

# #третья задача
# x = int(input())
# y = int(input())
# list = []
# def max_of_two(x, y):
#     list.append(x)
#     list.append(y)
#     if x == y:
#         print('Они равны')
#     else:
#         print(max(list))
# max_of_two(x, y)

# #Четвертая задача
# def describe_person(name, age=30):
#     print(f'Ваше имя: {name}, Ваш возраст: {age}')
#
#
# name = input('Введите ваше имя: ')
# age = int(input('Введите ваш возраст: '))
# if age == '':
#     describe_person(name)
# else:
#     describe_person(name, age)

##Пятая задача
# cnt = 0
# number = int(input("Введите число: "))
# for i in range(2,number + 1):
#     if number == 1:
#         print('Составное')
#         break
#     if number % i == 0:
#         cnt += 1
#
# if cnt >= 2:
#     print('Составное')
# if cnt < 2:
#     print('Простое')
