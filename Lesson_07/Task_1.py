class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy=False):
        self.color = color
        self.seats = count_passenger_seats
        self.baby = is_baby_seat
        self.busy = is_busy

    def __str__(self):
        return f'Авто {self.color}: {self.seats} мест, {"есть детское кресло" if self.baby else "нет детского кресла"}, {"авто свободно" if not self.busy else "авто занято"}'


bmv = Car('голубая', 5, True, True)
print(bmv)

