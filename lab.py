
x = 2
y = 4
x,y = y,x
print(x,y)

if x > y :
    print("Largest number is: ", x)
else:
    print("Largest number is: ", y)

def longest_str(str_1,str_2):
    if len(str_1) > len(str_2): print(str_1)
    else:print(str_2)


longest_str('hello','hi')

for i in range(1,101):
    if i %2 == 0  : print(i)

i = 0
while i < 101:
    if i % 2 == 0: print(i)
    i +=1

i = 0
while i < 3:
    print('***')
    i+=1

i=0
y = '*'
while i < 4:
    print(y * i) ## we will print * multiple times ....
    i+=1

import random
i = 0
i_list = []
while i < 11:
    i_list.append(random.randint(1,10))
    i+=1
print(i_list)

