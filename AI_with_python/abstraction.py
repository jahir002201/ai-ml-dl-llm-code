from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Dog says Woof!")


class Cat(Animal):

    def speak(self):
        print("Cat says Meow!")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()