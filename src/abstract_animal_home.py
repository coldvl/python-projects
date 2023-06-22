from abc import ABC, abstractmethod

class AbstractAnimalHome(ABC):
    """
    An abstract base class for animal homes.
    """

    def __init__(self, name, location, area):
        self.name = name
        self.location = location
        self.area = area

    def get_attributes_by_type(self, data_type):
        return {k: v for k, v in self.__dict__.items() if isinstance(v, data_type)}

    @abstractmethod
    def calculate_cost_per_month(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}, Area: {self.area}"

