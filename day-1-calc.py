import math
# input which one  to make

math_op = input("Enter which operation to do M,S,D , SQ or ML :")


if math_op == 'M':
    ## to do addition
    x = float(input("Enter a number for addition: "))
    y = float(input("Enter the second numberfor addition: "))
    print(x, '+' ,y, '=', x+y)

elif math_op == 'S':
## to do subtraction
    x1 = float(input("Enter a number subtract: "))
    y1 = float(input("Enter the second number subtract: "))
    print(x1, '-' ,y1, '=', x1-y1)


elif math_op == 'D':
## to do division
    x2 = float(input("Enter a number division: "))
    y2 = float(input("Enter the second number division: "))
    print(x2, '/' ,y2, '=', x2/y2)


elif math_op == 'ML':
## to do multiplication
    x3 = float(input("Enter a number multiplication: "))
    y3 = float(input("Enter the second number multiplication: "))
    print(x3, 'x' ,y3, '=', x3*y3)


elif math_op == 'SQ':
## to do multiplication
    x3 = float(input("Enter a number square root: "))
    y3 = float(input("Enter the second number square root: "))
    print(x3, 'Sq root of' ,y3, '=', math.sqrt(x3)+math.sqrt(y3) )


