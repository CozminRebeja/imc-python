
#garbage collection
# import gc
# gc.collect()
    ##explicitly triggeting garbage collector

print ("hello", "how are you", end ="?\n")

print ("hello", "how are you", end ="?\n", sep = " * ")

print ("hi", "i am", 4*3, "years old", sep ="-")

# single line comments

"""
multiline
comments
"""

#variables , expressions, statements, types

#operator assignments
numberItems = 5
pricePeritem = 17.29
currency = "Euro"
sum = numberItems * pricePeritem

#variable assignments
x = 12
y = 23

x += y
x -= y
x *= y
x /= y

'''
Data types in python:

- Numbers: Integers (int) and floating point (float) (64-bit)
- Complex numbers: x = 3+1j or x = complex(3,1)
- Strings, using double or single quotes: "cat" 'dog'
- Boolean: True and False
- Collections of variables
- Lists, dictionaries, and tuples
- Special types: files, network connections, objects

'''

# type conversion

intVal = int('123') #123
intVal = int(3.5) #3

strVal = str(3) # "3"
floatVal = float(3) # 3.0

"""
these will not work:
    floatVar = float('abc')
    intVal = int('abc')
"""

#number formats
# int()
# bin()
# oct()
# hex()

#when computing with floats, / will indicate regular division with fractional results.
14.0 % 5.0 # = 4.0
14 % 4 # = 4
14.0 / 5.0 # = 2.8
14 / 5 # = 2.8 (since Python 3)
14.0 // 5.0 # = 2

#reading inputs from keyboard
name = input("Insert your name: ")
print(name)

#reading numbers from inputs:
priceString = input("Enter Price: ")
price = float(priceString)

#formated output f-String

print(f"Hello, {name}")

#multiline f-String

print(f"hi, {name}\n" \
    f"How are you today?\n" \
    f"Fuck you.\n")