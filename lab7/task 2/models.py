class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def eat(food):
        print(f"Animal eats {food}")

    def make_sound():
        print("Animal make sound.")

    def __str__(self):
        return "Name: "+self.name +"," + "Age: "+self.age + ","+"Weight: "+self.weight
    
class Dog(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def make_sound(self):
        print("Woof")

    def run(self):
        print(self.name, "runs.")


class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def make_sound(self):
        print("Meow")

    def sleep(self):
        print(self.name, "is sleeping.")