from datetime import time
from abstract_animal_home import AbstractAnimalHome

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

    def add_animals(self, count):
        """
        Adds animals to the zoo.

        :param count: The number of animals to add.
        """
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