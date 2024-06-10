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


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary {}".format(self.salary)
        return text

    def cal_yearly_salary(self):
        return self.salary * 12


worker1 = Worker("Henry", 40, 176, 3000)
print(worker1)
print(worker1.cal_yearly_salary())


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)


v1 = Vector(2, 5)
v2 = Vector(6, 3)
print(v1)
print(v2)
v3 = v1 - v2

print(v3)

