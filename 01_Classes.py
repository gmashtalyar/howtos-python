class Person:

    amount = 0  # class variables for all objects

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1  # class variables for all objects

    def __del__(self):
        Person.amount -= 1  # class variables for all objects

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"


person = Person("Mike", 30, 175)

print(person)
print(Person.amount)
