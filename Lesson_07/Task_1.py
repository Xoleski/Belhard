class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy=False):
        self.color = color
        self.seats = count_passenger_seats
        self.baby = is_baby_seat
        self.busy = is_busy

    def __str__(self):
        return (f'Авто: \n'
                f'{self.color} цвет, \n'
                f'{self.seats} мест, \n'
                f'{"есть детское кресло" if self.baby else "нет детского кресла"}, \n'
                f'{"авто свободно" if not self.busy else "авто занято"}')


bmv = Car('голубой', 4, True)
print(bmv)

