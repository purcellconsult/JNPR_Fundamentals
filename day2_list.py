
## get the input from user.

#for i in range 5:


init_list = [0,10,30,40,50,60]
list_count = len(init_list)
count = 0
print(list_count)
for i in init_list:
    if count % 2 != 0 :
        pass
        print("This is the : ", count, "in this list with value in list is :", i)
    count +=1


x = [1, 2, 2, 4, 5,6,7,8]
print('Even: ', x[1::2])
print('Odd: ', x[::2])


odds = [1,3,5,7,9]
odds.append(11)
print(odds) ## [1, 3, 5, 7, 9, 11]
odds.insert(0,13) ## 0 is  the  location in the list
print(odds) ## [13, 1, 3, 5, 7, 9, 11]


list_new = [10,'adsd','sssas']

for index,item in enumerate(list_new):
    print("For index :",index, "The item is: ", item)


nested_list = [[10,'adsd','sssas'], 10,20,[1, 2, 2, 4, 5,6,7,8]]

for index,item in enumerate(nested_list):
    print("For index :",index, "The item is: ", item)

## to access a nested list item

nested_item_in = nested_list[3][3]
print(nested_item_in)


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)

print(matrix[0][2] * matrix[1][1]) ## this should be 3 * 5

## to go through all matrix values

for row in matrix:
    for col in row:
        print(col)



win,loss = 0,0
import random

for i in range(5):
    coin_face = random.choice(['pic','letter'])
    terminate = 'done'

    #print(coin_face)
    user_input = input("Enter which  side of the coin  pic or letter : ")
    if user_input == terminate:
        break
    if user_input == coin_face:
        print("You got it write")
        win +=1
    else:
        print("this was wrong")
        loss +=1

print("Won time : ", win,"Loss time: ", loss)
