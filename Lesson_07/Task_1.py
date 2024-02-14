# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле


class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy=False):
        self.color = color
        self.seats = count_passenger_seats
        self.baby = is_baby_seat
        self.busy = is_busy

    def get_instance_names(self):
        names = [i for i, j in globals().items() if isinstance(j, type(self))]
        if names:
            return names

    def get_var_name(self):
        for k, v in globals().items():
            if v is self:
                return k

    def __str__(self):
        return (f'Авто: '
                f'{self.color} цвет, '
                f'{self.seats} мест, '
                f'{"есть детское кресло" if self.baby else "нет детского кресла"}, '
                f'{"авто свободно" if not self.busy else "авто занято"}')


bmv = Car("голубой", 4, True)
mazda = Car("чёрный", 4, False)
opel = Car("красный", 4, True)
bugatti = Car("изумрудный", 2, False)
# print(bmv)
# print(mazda)
# print(opel)
# print(bugatti)


# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать Non

class Taxi:
    def __init__(self, cars: list[Car]):
        self.car = cars

    def find_car(self, count_passengers, is_baby):
        a = None
        for i in range(len(self.car)):
            if count_passengers > self.car[i].seats:
                pass
            elif is_baby and not self.car[i].baby:
                pass
            elif not self.car[i].busy:
                b = self.car[i].get_var_name()
                a = f'{b.upper()} {self.car[i]}'
                self.car[i].busy = True
                break
        return a


d = Taxi([bmv, mazda, opel, bugatti])

s = d.find_car(3, True)
print("s: ", s)
p = d.find_car(2, False)
print("p: ", p)
l = d.find_car(2, False)
print("l: ", l)
x = d.find_car(5, False)
print("x: ", x)
kj = d.find_car(2, False)
print("kj: ", kj)

