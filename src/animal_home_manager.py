from datetime import time
from models.aquarium import Aquarium
from models.farm import Farm
from models.sanctuary import Sanctuary
from models.zoo import Zoo
from abstract_animal_home import AbstractAnimalHome

class AnimalHomeManager:
    """
    A class for managing a collection of animal homes.
    """

    def __init__(self):
        """
        Initializes a new instance of the AnimalHomeManager class.
        """
        self.animal_homes = []

    def __len__(self):
        return len(self.animal_homes)

    def __getitem__(self, index):
        return self.animal_homes[index]

    def __iter__(self):
        return iter(self.animal_homes)
    
    def do_something_for_all_animal_homes(self):
        """
        Calls the __str__ method for all animal homes in the collection and returns a list of the results.

        :return: A list of the results of calling the do_something method for all animal homes.
        """
        return [f"{index}: {animal_home.__str__()}" for index, animal_home in enumerate(self.animal_homes)]

    def zip_animal_homes(self):
        """
        Calls the do_something_for_all_animal_homes method and returns a list of tuples containing the animal homes
        and the result of calling the do_something method for each animal home.

        :return: A list of tuples containing the animal homes and the result of calling the do_something method for each animal home.
        """
        animal_homes = self.animal_homes
        results = self.do_something_for_all_animal_homes()
        return list(zip(animal_homes, results))
    
    def check_conditions(self, condition):
        """
        Checks whether all objects in the animal_home_manager list satisfy a certain condition, and if at least one does.
        Returns a dictionary with the keys "all" and "any" and the corresponding boolean values.

        :param condition: The condition to check.
        :return: A dictionary with the keys "all" and "any" and the corresponding boolean values.
        """
        all_satisfy = all(condition(animal_home) for animal_home in self.animal_homes)
        any_satisfy = any(condition(animal_home) for animal_home in self.animal_homes)
        return {"all": all_satisfy, "any": any_satisfy}

    def get_attributes_by_type(self, type_name):
        attributes = []
        for animal_home in self.animal_homes:
            attributes.append(animal_home.get_attributes_by_type(type_name))
        return attributes

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


if __name__ == "__main__":
    manager = AnimalHomeManager()
    manager.add_animal_home(Farm("Wild Bluff Ranch", "USA", 200, 15, 10, "Cow"))
    manager.add_animal_home(Zoo("Limpopo", "Lviv", 100, 20, time(10, 0, 0), time(18, 0, 0), 30))
    manager.add_animal_home(Farm("Sunset Farms", "California", 300, 25, 10, "Pig"))
    manager.add_animal_home(Zoo("Lviv Zoo", "Lviv", 200, 30, time(10, 0, 0), time(18, 0, 0), 30))
    manager.add_animal_home(Farm("End of the World Fields", "California", 300, 25, 10, "Pig"))
    manager.add_animal_home(Farm("Coral Kingdom", "Australia", 500, 50, 100, "Tropical Fish"))
    manager.add_animal_home(Farm("Sky High Aviary", "USA", 150, 10, 15, "Parrots"))
    manager.add_animal_home(Zoo("Friendly Farms", "Canada", 100, 10, time(11, 0, 0), time(16, 0, 0), 20))
    manager.add_animal_home(Farm("Serengeti Plains", "Tanzania", 1000, 100, 45, "Elephants"))
    manager.add_animal_home(Farm("Dragon's Den", "USA", 200, 20, 30, "Snakes"))
    manager.add_animal_home(Aquarium("Aquarium of the Pacific", "USA", 100, 10, 10, 10))
    manager.add_animal_home(Aquarium("Shedd Aquarium", "USA", 200, 20, 20, 20))
    manager.add_animal_home(Aquarium("National Aquarium", "USA", 300, 30, 30, 30))
    manager.add_animal_home(Sanctuary("The Wild Animal Sanctuary", "USA", 100, 30, 10, 10, 50))
    manager.add_animal_home(Sanctuary("Sanctuary of the White Lion", "South Africa", 200, 60, 20, 20, 100))
    manager.add_animal_home(Sanctuary("The Elephant Sanctuary", "USA", 300, 90, 30, 30, 150))

    manager.print_all_farms()
    manager.print_all_zoos()
    manager.print_all_aquariums()
    manager.print_all_sanctuaries()

    print()
    
    

    print()

    print("The cheapest animal home is:", manager.find_cheapest_animal_home())

    print()

    print("Animal homes with the area less than 200:")
    for animal_home in manager.find_animal_homes_with_area_less_than(200):
        print(animal_home)


    print()
    
    """
    print the result of executing these methods:
    do_something_for_all_animal_homes
    zip_animal_homes
    check_conditions
    get_attributes_by_type
    """
    print(manager.do_something_for_all_animal_homes())
    print(manager.zip_animal_homes())
    print(manager.check_conditions(lambda animal_home: animal_home.area > 100))
    print(manager.get_attributes_by_type(Farm))
    
    