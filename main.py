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
str_score = d_arr[0]
dex_score = d_arr[1]
con_score = d_arr[2]
int_score = d_arr[3]
wis_score = d_arr[4]
cha_score = d_arr[5]

#Attribute Bonuses will go here. 


#do this as one command in the future, ierate with for loop?
#print(s_arr[0], str_score)
#print(s_arr[1], dex_score)
#print(s_arr[2], con_score)
#print(s_arr[3], int_score)
#print(s_arr[4], wis_score)
#print(s_arr[5], cha_score)