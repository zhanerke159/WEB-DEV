class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food):
        print(f"{self.name} eats {food}")

    def make_sound(self):
        print("Animal makes a sound.")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"


class Dog(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def make_sound(self):
        print("Woof")

    def run(self):
        print(f"{self.name} runs.")


class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def make_sound(self):
        print("Meow")

    def sleep(self):
        print(f"{self.name} is sleeping.")