# range 1-100
# user to guess
## used randit to generate a number number ...
# if the user is correct show :) if not :(


import random

rand_num = random.randint(1,100)

while True:

    user_num = int(input("Enter a number between 1-100: "))

    if user_num == rand_num:
        print("you got it write :) ,, Exiting the program")
        break
    else:
        print("Try again later ")
    print("The number generated  is : {}".format(rand_num))
    play_again = input("Do you want to play again Y/N: ")
    if play_again == 'N':
        break

