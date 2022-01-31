# Задание 1
# from time import sleep
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'Светофор переключается \n '
#                   f'{TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(5)
#             elif i == 2:
#                 sleep(3)
#             i += 1
#
# TrafficLight = TrafficLight()
# TrafficLight.running()

# Задание 2

# class Road:
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#
#     def mass(self):
#         return self._length * self._width
#
#
# class MassCount(Road):
#     def __init__(self, _length, _width, volume):
#         super().__init__(_length, _width)
#         self.volume = volume
#
#
# r = MassCount(25, 10000, 125)
# print(r.mass())

# Задание 3

# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#         # return f'{sum(self._income.values())}'
#
#
# a = Position('Kate', 'отличный', 'преподаватель', 100000, 25000)
# print(a.get_full_name())
# print(a.position)
# print(a.get_total_income())

# Задание 4

# class Car:
#     # atributes
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     # methods
#     def go(self):
#         return f'{self.name} стартует'
#
#     def stop(self):
#         return f'{self.name} остановился'
#
#     def turn_right(self):
#         return f'{self.name} поехал направо'
#
#     def turn_left(self):
#         return f'{self.name} поехал налево'
#
#     def show_speed(self):
#         return f'Текущая скорость {self.name} - {self.speed}'
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Скорость городского авто {self.name} - {self.speed}')
#
#         if self.speed > 40:
#             return f'Скорость {self.name} выше чем допустимо для гражданского авто'
#         else:
#             return f'Скорость {self.name} нормальная для гражданского авто'
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.name} - {self.speed}')
#
#         if self.speed > 60:
#             return f'Скорость {self.name} выше допустимой'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} полицейская машина'
#         else:
#             return f'{self.name} не полицейская машина'
#
#
# audi = SportCar(100, 'Красный', 'Субару', False)
# oka = TownCar(30, 'Белый', 'Ока', False)
# lada = WorkCar(70, 'Зеленый', 'Лада', True)
# ford = PoliceCar(110, 'Синий',  'Форд', True)
# print(lada.turn_left())
# print(f'Когда {oka.turn_right()}, затем {audi.stop()}')
# print(f'{lada.go()} со скоростью {lada.show_speed()}')
# print(f'{lada.name} {lada.color}')
# print(f'{audi.name} полицейская машина? {audi.is_police}')
# print(f'{lada.name}  полицейская машина? {lada.is_police}')
# print(audi.show_speed())
# print(oka.show_speed())
# print(ford.police())
# print(ford.show_speed())

# Задание 5

# class Stationary:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
#
# class Pen(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}. Запуск отрисовки фломастером'
#
#
# class Pencil(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}. Запуск отрисовки карандашом'
#
#
# class Handle(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}. Запуск отрисовки маркером'
#
#
# pen = Pen('Фломастер')
# pencil = Pencil('Карандаш')
# handle = Handle('Маркер')
# print(pen.draw())
# print(pencil.draw())
# print(handle.draw())