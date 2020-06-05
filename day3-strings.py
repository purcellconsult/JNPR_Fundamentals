x = 'hello world'
print(x[0])
print(x[-1])


print(x[1:3])## slice a string


print(len(x[::]))## print the list of string


print(x[::-1]) ## to reverse a string

print(x[::2]) ## this just by 2 items in the string

i_list = [i for i in x]
print(i_list)

## when to use while or a for ...
### if we know the list letngth we shall use for.
##### if we know the length, and need to keep track of the item index we can use while loop.


for index,char in enumerate("Boston"): print(index,char,end=" ** \n")

# the end use to add something to each  iteration, am adding ** :)



poem = """ this si a simple poem which has nothing and means nothing """
check_poem = print(poem.isnumeric())


char ='a'
char +='b'
char +='b'
char+='c'
print(char)


import string
print(string.ascii_letters)

## to compare two strings.....

user_input = "Z"
list_cjeck = ["Yes" for user_input in string.ascii_letters]
print(list_cjeck)
if "Z" in string.ascii_letters:
    print("YEs" )