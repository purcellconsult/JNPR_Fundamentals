from random import choice
import string
import random

first_name = ['Deen','John','Steve','Bruce','Sean']
last_name = ['Osaka','Marc','Mario','Dan','Anthony']



for x in range(2):
    random_name = '{} {}'.format(choice(first_name),choice(last_name))
    print(random_name)


## another way ....

email_service = ['gmail','hotmail','yahoo','outlook','aol']

rand_digit = random.randint(0,9)
rand_digit1 = random.randint(0,9)
rand_digit2 = random.randint(0,9)

for x in range(20):
    first,last = choice(first_name), choice(last_name)
    #random_name = f'{first} {last}'
    #print(random_name)
    random_mail_service = choice(email_service)
    random_mail_per_user = '{}.{}@{}.com'.format(first,last,random_mail_service)
    random_phone_number = '{}{}{}-{}{}{}-{}{}{}'.format(rand_digit,rand_digit1,rand_digit2,rand_digit,rand_digit1,rand_digit,rand_digit2,rand_digit,rand_digit)
    random_phone_number = '{}-{}-{}'.format(random.randint(9),random.randint(9),random.randint(9))
    print(random_mail_per_user," Phone number: ",random_phone_number)


