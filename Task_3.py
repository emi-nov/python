# ЗАДАНИЕ 1

#def div(*division):
#    try:
#        ch1 = int(input("Введите первое число: "))
#        ch12 = int(input("Введите второе число: "))
#        result = ch1 / ch12
#    except ValueError:
#        return 'Это не число!'
#    except ZeroDivisionError:
#        return "Вы не можете использовать ноль!"
#    return result
#print(f'Результат  {div()}')

# ЗАДАНИЕ 2

#name = input('Введите имя: ')
#surname = input('Введите фамилию: ')
#age = input('Введите возраст: ')
#city = input('Введите город: ')
#email = input('Введите email: ')
#phone = input('Введите номер телефона: ')
#def my_func (name, surname, age, city, email, phone):
#     return ' '.join([name, surname, age, city, email, phone])
#print(my_func(name = name, surname = surname, age = age, city = city, email = email, phone = phone))

# ЗАДАНИЕ 3

#def my_func(argum1 , argum2, argum3):
#    if argum1 >= argum3 and argum2 >= argum3:
#        return argum1 + argum2
#    elif argum1 > argum2 and argum1 < argum3:
#        return argum1 + argum3
#    else:
#        return argum2 + argum3
#print(f'Результат: {my_func(int(input("Введите первый аргумент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргумент: ")))}')

# ЗАДАНИЕ 4

#def my_func(x,y):
#    value1 = x ** y
#    value2 = 1
#    i = 1
#    while i <= abs(y):
#        value2 *= x
#        i += 1
#    return value1, 1 / value2
#print(my_func(int(input("Введите первое число: ")),int(input("Введите второе число: "))))

# ЗАДАНИЕ 5

#def my_sum ():
#    sum_res = 0
#    ex = False
#    while ex == False:
#        number = input('Введите числа через пробел. Для выхода введите "X": ').split()
#        res = 0
#        for el in range(len(number)):
#            if number[el] == 'x' or number[el] == 'X':
#                ex = True
#                break
#            else:
#                res = res + int(number[el])
#        sum_res = sum_res + res
#        print(f'Текущая сумма:  {sum_res}')
#        print(f'Финальная сумма:  {sum_res}')
#my_sum()

# ЗАДАНИЕ 6

#def int_func (*words):
#    word = input("Вводите слова через пробел: ")
#    print(word.title())
#    return
#int_func()