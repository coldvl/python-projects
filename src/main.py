from animal_home_manager import AnimalHomeManager
from datetime import time
from models.aquarium import Aquarium
from models.farm import Farm
from models.sanctuary import Sanctuary
from models.zoo import Zoo

def main():
    """
    The main function of the program.

    This function creates an instance of the AnimalHomeManager class and adds several animal homes to it. It then calls
    several methods of the AnimalHomeManager class to print information about the animal homes.
    """
    manager = AnimalHomeManager()

    # Add several animal homes to the manager
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

    # Print information about the animal homes
    manager.print_all_farms()
    manager.print_all_zoos()
    manager.print_all_aquariums()
    manager.print_all_sanctuaries()