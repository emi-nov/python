# Задание 1

#my_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(my_l)
#print(type(my_l))

# Задание 2

#print('Введите числа от 1 до 10:')
#my_l = []
#for i in range(10):
#    my_l.append(int(input()))
#print(type(my_l))
#print(my_l)
#print('Число элементов списка:', len(my_l))
#my_l[0], my_l[len(my_l) - 1] = my_l[len(my_l) - 1], my_l[0]
#print(my_l)
#my_l[2], my_l[len(my_l) - 3] = my_l[len(my_l) - 3], my_l[2]
#print(my_l)

# Задание 3

#month = int(input('Введите месяц от 1 до 12:'))
#my_l = ['Весна', 'Лето', 'Осень', 'Зима']
#if month == 1 or month == 2 or month == 12:
#    print (my_l[3])
#elif month == 3 or month == 4 or month == 5:
#    print (my_l[0])
#elif month == 6 or month == 7 or month == 8:
#    print (my_l[1])
#elif month == 9 or month == 10 or month == 11:
#    print (my_l[2])
#else:
#    print ('Такого месяца нет')

#month = int(input('Введите месяц от 1 до 12:'))
#my_dict = {0: 'Весна', 1: 'Лето', 2: 'Осень', 3: 'Зима'}
#if month == 1 or month == 2 or month == 12:
#    print(my_dict.get(3))
#elif month == 3 or month == 4 or month == 5:
#    print(my_dict.get(0))
#elif month == 6 or month == 7 or month == 8:
#    print(my_dict.get(1))
#elif month == 9 or month == 10 or month == 11:
#    print(my_dict.get(2))
#else:
#    print ('Такого месяца нет')

# Задание 4

#my_str = input("Введите текст: ")
#my_word = []
#num = 1
#for el in range(my_str.count(' ') + 1):
#    my_word = my_str.split()
#    if len(str(my_word)) <= 10:
#        print(f" {num} {my_word [el]}")
#        num += 1
#    else:
#        print(f" {num} {my_word [el] [0:10]}")
#        num += 1

# Задание 5

#my_list = [8, 4, 1, 1, 5]
#print(f"Рейтинг чисел - {my_list}")
#digit = int(input("Введите число: (Введите 0000 для выхода) ")) #stop
#while digit != 0000:
#    for el in range(len(my_list)):
#        if my_list[el] == digit:
#            my_list.insert(el + 1, digit)
#            break
#        elif my_list[0] < digit:
#            my_list.insert(0, digit)
#        elif my_list[-1] > digit:
#            my_list.append(digit)
#        elif my_list[el] > digit and my_list[el + 1] < digit:
#            my_list.insert(el + 1, digit)
#    print(f"Новый список - {my_list}")
#    digit = int(input("Введите новое число "))