class AbstractAnimalHome:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.area = 0.0

    def calculate_cost_per_month(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}, Area: {self.area}"


class AnimalHome(AbstractAnimalHome):
    def __init__(self, name, location, area):
        super().__init__(name, location)
        self.area = area

    def calculate_cost_per_month(self):
        # Implement the cost calculation logic here
        pass
