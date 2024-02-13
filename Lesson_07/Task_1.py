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


# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError


class Category:
    categories = []

    @classmethod
    def add(cls, name: str):
        if name in cls.categories:
            raise ValueError
        else:
            cls.categories.append(name)
            return cls.categories.index(name)

    @classmethod
    def get(cls, index: int):
        return cls.categories[index]

    @classmethod
    def delete(cls, index: int):
        try:
            del (cls.categories[index])
        except IndexError:
            pass

    # def __int__(self, categories):
    #     self.cat = categories


mn = ['low', 'high', 'medium']
kitkat = Category().add("low")
print(kitkat)
kitkat = Category().add("high")
print(kitkat)
Category().delete(2)
print(i := Category().get(1))

# Category().add('high')
# print(kitkat)






























# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError




