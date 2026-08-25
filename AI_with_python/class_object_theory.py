class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


car = Car("Toyota", "Corolla")

car.display()