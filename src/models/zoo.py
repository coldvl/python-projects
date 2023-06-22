import sys
sys.path.append("src/")
import logging
from datetime import time
from abstract_animal_home import AbstractAnimalHome

class NonIntegerCountException(Exception):
    """
    An exception raised when a non-integer count is passed to the add_animals method.
    """

def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(str(e))
                elif mode == "file":
                    logging.basicConfig(filename='exceptions.log', level=logging.ERROR)
                    logging.error(str(e))
                else:
                    raise ValueError("Invalid mode specified for logged decorator")
        return wrapper
    return decorator

class Zoo(AbstractAnimalHome):
    """
    A class representing a zoo.
    """

    def __init__(self, name, location, area, capacity, opening_time, closing_time, cost_per_day):
        """
        Initializes a new instance of the Zoo class.

        :param name: The name of the zoo.
        :param location: The location of the zoo.
        :param area: The area of the zoo in square meters.
        :param capacity: The maximum number of animals that the zoo can hold.
        :param opening_time: The time that the zoo opens.
        :param closing_time: The time that the zoo closes.
        :param cost_per_day: The cost per day of visiting the zoo.
        """
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
        """
        Splits the area of the zoo in half.
        """
        self.area /= 2

    def add_new_region(self, area):
        """
        Adds a new region to the zoo.

        :param area: The area of the new region in square meters.
        """
        self.area += area

    def __str__(self):
        """
        Returns a string representation of the zoo.

        :return: A string representation of the zoo.
        """
        return super().__str__() + f", Capacity: {self.capacity}, Opening Time: {self.opening_time}, " \
                                   f"Closing Time: {self.closing_time}, Cost Per Day: {self.cost_per_day}"

    def calculate_cost_per_month(self):
        """
        Calculates the cost per month of the zoo.

        :return: The cost per month of the zoo.
        """
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