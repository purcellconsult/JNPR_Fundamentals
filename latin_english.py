## Translate latin unmber ...
# ph2 is  to add these through a dictionary file ... 

def latin_numbers():
    latin_to_english = {'Uno':'one',
                        'Due':'two',
                        'Tries ':'three','Cuarto':'four','Cinco':'five'}
    spanish_letter = input("Enter a spanish letter: ").capitalize()
    if spanish_letter in latin_to_english.keys():
        print(latin_to_english[spanish_letter])

latin_numbers()

