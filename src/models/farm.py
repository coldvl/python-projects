from abstract_animal_home import AbstractAnimalHome

class Farm(AbstractAnimalHome):
    """
    A class representing a farm.
    """

    def __init__(self, name, location, area, capacity, cost_per_animal_per_day, animal_type):
        """
        Initializes a new instance of the Farm class.

        :param name: The name of the farm.
        :param location: The location of the farm.
        :param area: The area of the farm in square meters.
        :param capacity: The maximum number of animals that the farm can hold.
        :param cost_per_animal_per_day: The cost per day of caring for an animal in the farm.
        :param animal_type: The type of animal that the farm holds.
        """
        super().__init__(name, location, area)
        self.capacity = capacity
        self.cost_per_animal_per_day = cost_per_animal_per_day
        self.animal_type = animal_type

    def __str__(self):
        """
        Returns a string representation of the farm.

        :return: A string representation of the farm.
        """
        return super().__str__() + f", Capacity: {self.capacity}, Cost Per Animal per Day: {self.cost_per_animal_per_day}, " \
                                   f"Animal Type: {self.animal_type}"

    def calculate_cost_per_month(self):
        """
        Calculates the cost per month of the farm.

        :return: The cost per month of the farm.
        """
        return self.cost_per_animal_per_day * 30 * self.capacity


farm = Farm("Wild Bluff Ranch", "USA", 200, 15, 10, "Cow")
print(farm)
print("Cost Per Month:", farm.calculate_cost_per_month())