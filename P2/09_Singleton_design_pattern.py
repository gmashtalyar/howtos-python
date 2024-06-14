from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data():
        """implement in child class"""


class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}. Age: {PersonSingleton.__instance.age}")


p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

# p2 = PersonSingleton("Bob", 25)
# print(p2)
# p2.print_data()

p3 = PersonSingleton.get_instance()
print(p3)
p3.print_data()
