"""
This program is used as temp. change ....
Below are the equations to be used ... 
 F -> C = (F - 32) x 5/9
 F -> K = (F - 32)/1.8 + 273.15
 C -> F = (C x 9/5) + 32
 C -> K = C + 273.15
 K -> F = (K - 273.15) x 9/5 + 32
 K -> C = K - 273.15
"""

def kelvin_cele(temp_in):
    temp_is = temp_in - 273.15
    print(temp_is, 'C')

def kelvin_fehr(temp_in):
    temp_is = (temp_in - 273.15)* 9/5 + 32
    print(temp_is, 'F')

def cele_fehr(temp_in):
    temp_is = (temp_in *9/5) + 32
    print(temp_is, 'F')


def cele_kelvin(temp_in):
    temp_is = temp_in + 273.15
    print(temp_is, 'K')


def fehr_cele(temp_in):
    temp_is = (temp_in - 32) * 5/9
    print(temp_is, 'C')

def fehr_kelvin(temp_in):
    temp_is = (temp_in - 32)/1.8 + 273.15
    print(temp_is, 'K')


def main_temp():
    temp_is = 0
    temp_in = 0
    check_in = input("Enter the type of temp you need to change from-To-temp: ")
    input_temp = check_in.split('-')
    if input_temp[0] == 'F':
        if input_temp[1] == 'C':
            temp_in = int(input_temp[2])
            fehr_cele(temp_in)
        elif input_temp[1] == 'K':
            temp_in = int(input_temp[2])
            fehr_kelvin(temp_in)
    elif input_temp[0] == 'K' and input_temp[1] == 'F':
        temp_in = int(input_temp[2])
        kelvin_fehr(temp_in)
    elif input_temp[0] == 'K' and input_temp[1] == 'C':
        temp_in = int(input_temp[2])
        kelvin_cele(temp_in)


    elif input_temp[0] == 'C' and input_temp[1] == 'F':
        temp_in = int(input_temp[2])
        cele_fehr(temp_in)
    elif input_temp[0] == 'C' and input_temp[1] == 'K':
        temp_in = int(input_temp[2])
        cele_kelvin(temp_in)





main_temp()
