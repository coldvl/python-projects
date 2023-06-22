from datetime import time
from abstract_animal_home import AbstractAnimalHome



class Zoo(AbstractAnimalHome):
    def __init__(self, name, location, area, capacity, opening_time, closing_time, cost_per_day):
        super().__init__(name, location, area)
        self.capacity = capacity
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.cost_per_day = cost_per_day

    def increase_capacity(self, count):
        self.capacity += count

    def split_area(self):
        self.area /= 2

    def add_new_region(self, area):
        self.area += area

    def __str__(self):
        return super().__str__() + f", Capacity: {self.capacity}, Opening Time: {self.opening_time}, " \
                                   f"Closing Time: {self.closing_time}, Cost Per Day: {self.cost_per_day}"

    def calculate_cost_per_month(self):
        return self.cost_per_day * 30


zoo = Zoo("Limpopo", "Lviv", 100, 20, time(10, 0, 0), time(18, 0, 0), 30)
print(zoo)
print("Cost Per Month:", zoo.calculate_cost_per_month())
