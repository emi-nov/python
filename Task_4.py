# Задание 1

# from sys import argv
#
# name, time, salary, bonus = argv
# try:
#     time = int(time)
#     salary = int(salary)
#     bonus = int(bonus)
#     res = time * salary + bonus
#     print(f'Зарплата сотрудника составляет {res} рублей.')
# except ValueError:
#     print('Not a number')

# Задание 2

# my_list = [153, 32, 4, 7, 32, 2, 33, 17]
# my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
# print(f'Исходный список {my_list}')
# print(f'Новый список {my_new_list}')

# Задание 3

# print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

# Задание 4

# my_list = [4, 2, 6, 4, 8, 7, 5, 9, 3, 9]
# my_new_list = [el for el in my_list if my_list.count(el) < 2]
# print(my_new_list)

# Задание 5

from functools import reduce

# def my_func(el_p, el):
#     return el_p * el

# print(f'Четные зеачения; {[el for el in range(99, 1001) if el % 2 == 0]}')
# print(f'Все элементы списка: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# Задание 6

# from itertools import count
#
# for el in count(int(input('Введите число: '))):
#     print(el)
#
# from itertools import cycle
#
# my_list = [True, 'ABC', 123, None]
# for el in cycle(my_list):
#     print(el)

# Задание 7

# from itertools import count
# from math import factorial
#
# def fibo_gen():
#     for el in count(1):
#         yield factorial(el)
#
# gen = fibo_gen()
# x = 0
# for i in gen:
#     if x < 15:
#         print(i)
#         x += 1
#     else:
#         break