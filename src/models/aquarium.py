from abstract_animal_home import AbstractAnimalHome

class Aquarium(AbstractAnimalHome):
    """
    A class representing an aquarium.
    """

    def __init__(self, name, location, area, cost_per_day_per_fish, number_of_fish_in_one_aquarium, number_of_aquariums):
        """
        Initializes a new instance of the Aquarium class.

        :param name: The name of the aquarium.
        :param location: The location of the aquarium.
        :param area: The area of the aquarium in square meters.
        :param cost_per_day_per_fish: The cost per day of caring for a fish in the aquarium.
        :param number_of_fish_in_one_aquarium: The number of fish in each aquarium.
        :param number_of_aquariums: The total number of aquariums in the aquarium.
        """
        super().__init__(name, location, area)
        self.cost_per_day_per_fish = cost_per_day_per_fish
        self.number_of_fish_in_one_aquarium = number_of_fish_in_one_aquarium
        self.number_of_aquariums = number_of_aquariums

    def __str__(self):
        """
        Returns a string representation of the aquarium.

        :return: A string representation of the aquarium.
        """
        return super().__str__() + f", Cost Per Day per Fish: {self.cost_per_day_per_fish}, " \
                                   f"Number of Fish in One Aquarium: {self.number_of_fish_in_one_aquarium}, " \
                                   f"Number of Aquariums: {self.number_of_aquariums}"

    def calculate_cost_per_month(self):
        """
        Calculates the cost per month of the aquarium.

        :return: The cost per month of the aquarium.
        """
        return self.cost_per_day_per_fish * 30 * self.number_of_fish_in_one_aquarium * self.number_of_aquariums


aquarium = Aquarium("Aquarium of the Pacific", "USA", 100, 10, 10, 10)
print(aquarium)
print("Cost Per Month:", aquarium.calculate_cost_per_month())