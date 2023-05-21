from abc import ABC, abstractmethod

class AbstractAnimalHome:
    def __init__(self, name, location, area):
        self.name = name
        self.location = location
        self.area = area

    @abstractmethod
    def calculate_cost_per_month(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}, Area: {self.area}"

