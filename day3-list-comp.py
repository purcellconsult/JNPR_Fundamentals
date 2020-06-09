## [expression for item in list]


nums = []
for x in range(1,21):
    nums.append(x)

print(nums)
numbers = [x for x in range(1,21)]
print(numbers)


## put only even in range 1-20

i = 0
evens = []
while i <=21:
    if i%2 == 0 :
        evens.append(i)
    i+=1

print(evens)


even_two = [x for x in range(1,21) if x %2 == 0]
print(even_two)

even_three = [x for x in range(0,21,2)]
print(even_three)


x = [x for x in range(10,15) for y in range(5)]
print(x)

rand_ints = []
import random
for x in range(20):
    random_num = random.randint(1,100)
    rand_ints.append(random_num)


rand_ints_comp = [random.randint(1,10) for x in range(20)]
print(rand_ints_comp)



dict1 = {'a':5,'b':2,'c':6}
tripe = {k:v**3 for (k,v) in dict1.items()}
## tripe generate a new dictionary ... k is the same as dict1.
## values is dict1(value) ^3 .. using the for loop to iterate over the dict1 dictionary...

print(tripe) ## result {'a': 125, 'b': 8, 'c': 216}

## adding some exceptions example:

def import_test():
    try:
        import math
        import sys
        import operator
        import pyexpat
        import juniper
    except ImportError:
        print("Could not import Juniper")


import_test()

try:
    a = input("Enter an integer: ")
    if a in range(1,10):
        raise Exception("this is right")
except TypeError:
    print("This is not an integer")


    
