# Seq 1 to 9,000,000

import sys
def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(10000)
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
for x in values:
    print(x)
print(sys.getsizeof(values))


######

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))



# IT DOESN'T STORE ANY VALUES. IT JUST YIELDS THE NEXT VALUE. IT DOESN'T WASTE MEMORY