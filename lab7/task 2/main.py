from models import Animal, Dog, Cat

dog = Dog("Rex", 3, 20)
cat = Cat("Milo", 2, 5)
animal = Animal("Tiger", 5, 100)

animals = [dog, cat, animal]

for a in animals:
    print(a)
    a.make_sound()
    print()