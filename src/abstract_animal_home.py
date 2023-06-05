from abc import ABC, abstractmethod

class AbstractAnimalHome(ABC):
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

    def get_attributes_by_type(self, data_type):
        return {k: v for k, v in self.__dict__.items() if isinstance(v, data_type)}

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