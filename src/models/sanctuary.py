from abstract_animal_home import AbstractAnimalHome

class Sanctuary(AbstractAnimalHome):
    """
    A class representing an animal sanctuary.
    """

    def __init__(self, name, location, area, number_of_endangered_animals, number_of_animals, cost_per_day_per_animal, cost_per_day_per_endangered_animal):
        """
        Initializes a new instance of the Sanctuary class.

        :param name: The name of the sanctuary.
        :param location: The location of the sanctuary.
        :param area: The area of the sanctuary in square meters.
        :param number_of_endangered_animals: The number of endangered animals in the sanctuary.
        :param number_of_animals: The total number of animals in the sanctuary.
        :param cost_per_day_per_animal: The cost per day of caring for a non-endangered animal in the sanctuary.
        :param cost_per_day_per_endangered_animal: The cost per day of caring for an endangered animal in the sanctuary.
        """
        super().__init__(name, location, area)
        self.number_of_endangered_animals = number_of_endangered_animals
        self.number_of_animals = number_of_animals
        self.cost_per_day_per_animal = cost_per_day_per_animal
        self.cost_per_day_per_endangered_animal = cost_per_day_per_endangered_animal

    def __str__(self):
        """
        Returns a string representation of the sanctuary.

        :return: A string representation of the sanctuary.
        """
        return super().__str__() + f", Number of Endangered Animals: {self.number_of_endangered_animals}, " \
                                   f"Number of Animals: {self.number_of_animals}, " \
                                   f"Cost Per Day per Animal: {self.cost_per_day_per_animal}, " \
                                   f"Cost Per Day per Endangered Animal: {self.cost_per_day_per_endangered_animal}"

    def calculate_cost_per_month(self):
        """
        Calculates the cost per month of the sanctuary.

        :return: The cost per month of the sanctuary.
        """
        return (self.cost_per_day_per_animal * self.number_of_animals +
                self.cost_per_day_per_endangered_animal * self.number_of_endangered_animals) * 30


sanctuary = Sanctuary("The Wild Animal Sanctuary", "USA", 100, 30, 10, 10, 50)
print(sanctuary)
print("Cost Per Month:", sanctuary.calculate_cost_per_month())