

def mydecorator(function):
    def wrapper(*args, **kwargs):  # add *args, **kwargs to be safe
        print("I am decorating your function!")
        function(*args, **kwargs)
        function(*args, **kwargs)
        print("I am decorating your function!")
        return_value = function(*args, **kwargs)  # structure to return after printing
        print("I am decorating your function!")
        return return_value
    return wrapper


@mydecorator
def hello_world(person):
    print(f"Hello {person} World!")
    return f"Hello {person}!"


print(hello_world("Mike"))


# PRACTICAL Example #1 - Logging
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} retunred value {value}")
            f.write(f"{fname} retunred value {value}\n")
        return value
    return wrapper


@logged
def add(x, y):
    return x + y


print(add(10, 20))


# PRACTICAL Example #2 - Timing
import time
def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result

myfunction(100000)

