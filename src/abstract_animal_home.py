from abc import ABC, abstractmethod

class AbstractAnimalHome:
    """
    An abstract base class for animal homes.
    """

    def __init__(self, name, location, area):
        """
        Initializes a new instance of the AbstractAnimalHome class.

        :param name: The name of the animal home.
        :param location: The location of the animal home.
        :param area: The area of the animal home in square meters.
        """
        self.name = name
        self.location = location
        self.area = area

    @abstractmethod
    def calculate_cost_per_month(self):
        """
        Calculates the cost per month of the animal home.

        This method must be overridden by subclasses.

        :return: The cost per month of the animal home.
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the animal home.

        :return: A string representation of the animal home.
        """
        return f"Name: {self.name}, Location: {self.location}, Area: {self.area}"