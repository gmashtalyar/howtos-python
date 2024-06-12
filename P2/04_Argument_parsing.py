
# Not actual argument parsing. Just kwargs and args
# def myfunction(*args, **kwargs):
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])
#     print(kwargs['KEYONE'])
#     print(kwargs['KEYTWO'])
# myfunction('hey', True, 19, 'wow', KEYONE="TEST", KEYTWO=7)


# ACTUAL ARGUMENT PARSING
import sys

# print(sys.argv[0])
# print(sys.argv[1])

# Usage: main.py FILENAME
# filename = sys.argv[1]
# message = sys.argv[2]
# with open(filename, 'w+') as f:
#     f.write(message)


import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])  # change to f:m:t if nothing after

print(opts)
print(args)

filename = "test.txt"  # default values
message = "Hello"  # default values

for opt, args in opts:
    if opt == "-f":
        filename = args
    if opt == "-m":
        message = args

with open(filename, "w+") as f:
    f.write(message)

# python3 03_Argument_parsing.py -f file.txt -m test
# python3 03_Argument_parsing.py file.txt test
