from abc import ABC, abstractmethod
from abstract_animal_home import AbstractAnimalHome

class Farm(AbstractAnimalHome):
    def __init__(self, name, location, area, capacity, cost_per_animal_per_day, animal_type):
        super().__init__(name, location, area)
        self.capacity = capacity
        self.cost_per_animal_per_day = cost_per_animal_per_day
        self.animal_type = animal_type

    def __str__(self):
        return super().__str__() + f", Capacity: {self.capacity}, Cost Per Animal per Day: {self.cost_per_animal_per_day}, " \
                                   f"Animal Type: {self.animal_type}"

    def calculate_cost_per_month(self):
        return self.cost_per_animal_per_day * 30 * self.capacity


farm = Farm("Wild Bluff Ranch", "USA", 200, 15, 10, "Cow")
print(farm)
print("Cost Per Month:", farm.calculate_cost_per_month())
