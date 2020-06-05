

## using set to remove duplicate entries on  list
from typing import Dict

dup_list = [1,1,1,2,3,4,4,6,7]
dup_list_new = list(set(dup_list)) # change the list to set --> to remove duplicates...
print(dup_list_new) ## this will print the new list without duplicates ....


## dictionary ....

letters= {'a':'apple','b':'boy','c':'cat'}
for x in letters: print("dic keys is:",x,", value is:",letters[x])

# to remove an item from a dictionary
letters.pop('c')
print(letters)

# to add an item to a dictionary

letters["d"] = "diamond"
print(letters)
letters.update({"c":"car"})
print(letters)






music = {'jazz':['song1','song2','song3'], 'rock':['song1','song2',['track1','track2','track3']]}
music2 = {'electronic':['song1','song2','song3'], 'house':['song1','song2',['track1','track2']]}

print(music)
print(music['jazz'][1], music['rock'][2][2])

## to merge a dictionary :

music_merge = music.update(music2)
print(music)

## or
music_merge2 = {** music,** music2}
print(music_merge2)