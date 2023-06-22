import sys
sys.path.append("src/")
import logging
from datetime import time
from abstract_animal_home import AbstractAnimalHome

class Zoo(AbstractAnimalHome):
    """
    A class representing a zoo.
    """

    def __init__(self, name, location, area, capacity, opening_time, closing_time, cost_per_day):
        super().__init__(name, location, area)
        self.capacity = capacity
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.cost_per_day = cost_per_day

    
    @logged(NonIntegerCountException, mode="console")

    def add_animals(self, count):
        """
        Adds animals to the zoo.

        :param count: The number of animals to add.
        """
        if not isinstance(count, int):
            raise NonIntegerCountException("Count must be an integer")
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
    
if __name__ == "__main__":
    zoo = Zoo("Zoo", "Location", 100, 100, time(8), time(18), 10)
    print(zoo)
    zoo.add_animals(10)
    print("added animals")
    print(zoo)
    zoo.split_area()
    print("split area")
    print(zoo)
    zoo.add_new_region(100)
    print("added new region")
    print(zoo)
    zoo.add_animals(10.5)
    print("added animals with exception")
    print(zoo)