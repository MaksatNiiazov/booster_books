
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    def drive(self):
        return f"{self.make} {self.model} {self.year} is driving"

