from datetime import time
from models.aquarium import Aquarium
from models.farm import Farm
from models.sanctuary import Sanctuary
from models.zoo import Zoo

class AnimalHomeManager:
    """
    A class for managing a collection of animal homes.
    """

    def __init__(self):
        """
        Initializes a new instance of the AnimalHomeManager class.
        """
        self.animal_homes = []

    def add_animal_home(self, animal_home):
        """
        Adds an animal home to the collection.

        :param animal_home: The animal home to add.
        """
        self.animal_homes.append(animal_home)

    def find_cheapest_animal_home(self):
        """
        Finds the animal home with the lowest cost per month.

        :return: The animal home with the lowest cost per month.
        """
        return min(self.animal_homes, key=lambda animal_home: animal_home.calculate_cost_per_month())

    def find_animal_homes_with_area_less_than(self, area):
        """
        Finds all animal homes with an area less than the specified value.

        :param area: The maximum area of the animal homes to find.
        :return: A list of animal homes with an area less than the specified value.
        """
        return [animal_home for animal_home in self.animal_homes if animal_home.area < area]

    def print_all_farms(self):
        """
        Prints all farms in the collection.
        """
        print("Farms:")
        for animal_home in self.animal_homes:
            if isinstance(animal_home, Farm):
                print(animal_home)

    def print_all_zoos(self):
        """
        Prints all zoos in the collection.
        """
        print("Zoos:")
        for animal_home in self.animal_homes:
            if isinstance(animal_home, Zoo):
                print(animal_home)
    
    def print_all_aquariums(self):
        print("Aquariums:")
        for animal_home in self.animal_homes:
            if isinstance(animal_home, Aquarium):
                print(animal_home)

    def print_all_sanctuaries(self):
        print("Sanctuaries:")
        for animal_home in self.animal_homes:
            if isinstance(animal_home, Sanctuary):
                print(animal_home)