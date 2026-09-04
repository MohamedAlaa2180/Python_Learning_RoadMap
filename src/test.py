from dataclasses import dataclass

@dataclass 
class Animal:
    name: str
    age: int
    species: str

    def make_sound(self) -> str:
        return "Animal sound"

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"

animals = [Dog("Buddy", 5, "Dog"), Cat("Whiskers", 3, "Cat")]


for animal in animals:
    print(animal.make_sound())