from random import randint
import numpy as np

#roll 6 numbers between 8 and 18 and add them to a list called dice_list. "return" stores the variable in the list and makes it usable.
#rewrite this as an array so I don't have to convert later

def char_roll():
  dice_list = []
  for _ in range(6):
    value = randint(8,18)
    dice_list.append(value)
  return(dice_list)

#stores character roll in variable
roll_res = char_roll()

stats_list = ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]

#convert lists to arrays. d_arr = dice array, character rolls. s_arr = stat array, names
d_arr = np.asarray(roll_res)
s_arr = np.asarray(stats_list)

#Stat variables go here
Strength = d_arr[0]
Dexterity = d_arr[1]
Constitution = d_arr[2]
Intelligence = d_arr[3]
Wisdom = d_arr[4]
Charisma = d_arr[5]

#do this as one command in the future, ierate with for loop?
print(s_arr[0], Strength)
print(s_arr[1], Dexterity)
print(s_arr[2], Constitution)
print(s_arr[3], Intelligence)
print(s_arr[4], Wisdom)
print(s_arr[5], Charisma)