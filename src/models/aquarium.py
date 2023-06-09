from abc import ABC, abstractmethod
from abstract_animal_home import AbstractAnimalHome

class Aquarium(AbstractAnimalHome):
    def __init__(self, name, location, area, cost_per_day_per_fish, number_of_fish_in_one_aquarium, number_of_aquariums):
        super().__init__(name, location, area)
        self.cost_per_day_per_fish = cost_per_day_per_fish
        self.number_of_fish_in_one_aquarium = number_of_fish_in_one_aquarium
        self.number_of_aquariums = number_of_aquariums

    def __str__(self):
        return super().__str__() + f", Cost Per Day per Fish: {self.cost_per_day_per_fish}, " \
                                   f"Number of Fish in One Aquarium: {self.number_of_fish_in_one_aquarium}, " \
                                   f"Number of Aquariums: {self.number_of_aquariums}"

    def calculate_cost_per_month(self):
        return self.cost_per_day_per_fish * 30 * self.number_of_fish_in_one_aquarium * self.number_of_aquariums


aquarium = Aquarium("Aquarium of the Pacific", "USA", 100, 10, 10, 10)
print(aquarium)
print("Cost Per Month:", aquarium.calculate_cost_per_month())
