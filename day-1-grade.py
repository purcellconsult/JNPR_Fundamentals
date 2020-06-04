
grade = int(input("Enter your grade: "))


if grade >= 90:
    print("A")

elif grade < 90 and grade>=80:
    print("B")


elif grade < 80 and grade>=70:
    print("C")


elif grade < 70 and grade>60:
    print("C")


else :
    print("reconsder  the colleage .... ")



# if nesting
x,y,z = 10,20,30

if x == 10:
    print(x)
    if y == 20:
        print("Here is y {}".format(y))
        if z == 30:
            print("X+Y = {}".format(x+y))



xx = 20
for x in range(10):
    print(x)

sum = 0
for x in range (1,5):
    if sum > 2016:
        pass
        print("hit the pass")
    sum +=x
    print(sum)




for x in range(3):
    for y in range(4):
        print(x,y, end =' ')
    print()


i = 0
while i < 10:
    print("The value of i is :",i)
    i+=1