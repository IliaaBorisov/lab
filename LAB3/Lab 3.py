# #Lab 3.1
# text = 'example.txt'
# def read_all(text):
#     with open(text, 'r', encoding='utf-8') as file:  # Чтение всего файла
#         content = file.read()
#         return content
# def read_line(text):
#     with open(text, 'r', encoding='utf-8') as file:
#         for line in file:
#             return(line)
# a = int(input('Каким медотом чтения файла вы хотите воспользоваться?\n 1-чтение всего файла    2-построчное чтение файла\n Введите ответ:' ))
# try:
#     if a == 1:
#         print(read_all(text))
#     elif a == 2:
#         print(read_line(text))
# except FileNotFoundError:
#     print('Файл не найден')
# # Lab 3.2
# user_input = input()

# #Построчное чтение
# with open('user_input.txt', 'a',encoding="utf-8") as file:
#     file.write(user_input+'\n')

# #Lab 3.3
# def read_all():
#     with open(text, 'r',encoding="utf-8") as file:
#         content = file.read()
#         return content
# def read_line():
#     with open(text, 'r',encoding="utf-8") as file:
#         for line in file:
#             return line
# a = int(input('Каким медотом чтения файла вы хотите воспользоваться?\n 1-чтение всего файла    2-построчное чтение файла\n Введите ответ:' ))
#
# try:
#     if a == 1:
#         print(read_all())
#     elif a == 2:
#         print(read_line())
# except FileNotFoundError:
#     print('Файл не найден')
