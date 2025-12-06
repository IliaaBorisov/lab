class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название: {self.title} \nАвтор: {self.author} \nГод издания: {self.year}"

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self, radius):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius


try:
    Book.title = input('Название: ')
    Book.author = input('Автор: ')
    Book.year = int(input('Год издания: '))
    print(Book.get_info(Book))
except ValueError:
    print('Ошибка значений')

action = 1
while action == 1:
    action = int(input("Вы желаете продолжить работу программы? \n 1-да       0-нет\n"))
    if action == 1:
        rad = int(input("Введите радиус: "))

        circle = Circle(rad)
        print(circle.get_radius(Circle))
        want_uprad = int(input("Вы хотиту обновить радиус? \n 1-да       0-нет\n"))
        if want_uprad == 1:
            n_rad = int(input("Введите новый радиус: "))
            circle.set_radius(n_rad)
            print(circle.get_radius(Circle))
    else:
        print('Удачи')