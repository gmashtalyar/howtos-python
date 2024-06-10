import threading


def function1():
    for x in range(10000):
        print("one")


def function2():
    for x in range(10000):
        print("two")


def hello():
    for x in range(50):
        print("hello!")

# t1 = threading.Thread(target=function1)
# t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=hello)
# t1.start()
# t2.start()

t3.start()  # this way main thread continues
t3.join()  # this way main thread pauses
print("another hello")
