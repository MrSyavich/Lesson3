# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def function(name, age, city):
    print('{}, {} год(а), проживает в городе {}'.format(name, age, city))


x = input('Введите имя ')
y = input('Введите год рождения ')
z = input('Город ')

function(x, y, z)
print()


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

import random

a = random.randint(-100, 100)
b = random.randint(-100, 100)
c = random.randint(-100, 100)

print(a, b, c)


def maxfunk(x, y, z):
    m = (max(x, y, z))
    return m


print('Наибольшее число:', maxfunk(a, b, c))
print()


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def strlong(args):
    x = 0
    for arg in args:
        if len(arg) > x:
            x = len(arg)
            maxlen = arg
        else:
            pass
    return maxlen


name = ['Глеб Жиглов', 'Петров Сухоруков', 'Владимир Владимирович', 'Вячеслав Кодд']

print(strlong(name))
