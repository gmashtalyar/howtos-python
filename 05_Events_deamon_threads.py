import threading
import time

# EVENTS
# event = threading.Event()
# def myfunction():
#     print("Waiting for event to trigger...\n")
#     event.wait()
#     print("Performing action XYZ now...")
# t1 = threading.Thread(target=myfunction)
# t1.start()
# x = input("Do you want to trigger the event? (y/n)\n")
# if x == "y":
#     event.set()

# DAEMON Threads

path = "text.txt"
text= ""


def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)


def printloop():
    for x in range (10):
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)
t1.start()
t2.start()
