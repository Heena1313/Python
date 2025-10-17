class Car:
    def __init__(self):
        self.make = 'BMW'
        self.model = '24AC18'
        self.year = 2025

    def talk(self):
        print("The car brand is:", self.make)
        print("The cost of car is:", self.model)
        print("The year:", self.year)

my_car = Car()
my_car.talk()