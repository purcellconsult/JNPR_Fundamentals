
## this is the 1st change
import math

print ("hell oworld")
a= 1.3
b = 'abc'
c = 1000
print(a)
print(b)
print(c)

x,y,z = 5,10,30


print(x,y,z)

x,y,z = z,x,y

print(x,y,z)

print(math.log(10000,2))
print(math.sqrt(4))
print(math.cos(10)+math.sin(10)+math.tan(10))

city = 'Acton'
print(city[0])
print(city[-1])
print(city[3])
print(city[1:-1])
print(city[::])


x,y,z = 5,100,30

if x < y and  y<z:
    print(y)
else:
    print(x)


from random import randint
grade = randint(1,100)
if grade < 50:
    print("failed your grade is :", grade)
else:
    print(grade, " passed")


mode = True
state = 'nice' if mode else 'not so nice'
print('state={}'.format(state))


vowels = {'a':0,"e":1,"i":2,"o":3,"u":4}
print(vowels.items())
print(vowels.values())
print(vowels.keys())

# set
set_list = {'a','b','b','e'}
print(set_list.intersection({'b','c'}))


i = 0
while i < 10:
    print('i={}'.format(i))
    i +=1

i,sum = 0,0
while i < 1000:
    i +=1
    sum +=i


print("The sum is : {}".format(sum))


for x in range (10):
    print(x)


x1 = math.erf(5)

xyz  = float(input("Enter a  number: "))
print("Here is the input:{} ".format(xyz))



x1  = float(input("Enter a  number: "))
print(type(x1))
print("Here is the input:{} ".format(x1))

print(xyz, '+', x1, '=', xyz+x1)

