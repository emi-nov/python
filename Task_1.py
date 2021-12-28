# Задание 1

#name = input("Введите имя: ")
#surname = input("Введите фамилию: ")
#age = int(input("Введите свой возраст: "))
#print(name, surname, age, 'лет')

# Задание 2

#a = int(input("Введите число: "))
#h = str(a//3600)
#m = (a//60) % 60
#s = a % 60
#if m < 10:
#    m = '0' + str(m)
#else:
#    m = str(m)
#if s < 10:
#    s = '0' + str(s)
#else:
#    s = str(s)
#print(h+':'+m+':'+s)

# Задание 3

#num = int(input("Введите число: "))
#sum = 0
#while (num != 0):
#    sum = sum + num % 10
#    num = num // 10
#print("Сумма равна: ", sum)

# Задание 4

#num = int(input('Введите число: '))
#r = -1
#while num > 10:
#    d = num % 10
#    num //= 10
#    if d > r:
#        r = d
#print(r)

# Задание 5

#proceeds = int(input('Введите выручку: '))
#costs = int(input('Введите издержки: '))
#print('Остаток составляет: ', proceeds - costs)
#rent = (proceeds - costs)
#if costs > proceeds:
#    print('Расход превышает доход.')
#else:
#    print('Расход не превышает доход')
#print('Рентабельность составляет', proceeds // costs * 0.100, '%')
#emp = int(input('Ведите число сотрудников: '))
#print('Прибыль фирмы в расчете на одного сотрудника:', rent // emp)