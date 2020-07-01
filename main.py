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

stats_list = ["strength:", "dexterity:", "constitution:", "intelligence:", "wisdom:", "charisma:"]

#convert lists to arrays
d_arr = np.asarray(roll_res)
s_arr = np.asarray(stats_list)

#do this as one command in the future, ierate with for loop?
print(s_arr[0], d_arr[0])
print(s_arr[1], d_arr[1])
print(s_arr[2], d_arr[2])
print(s_arr[3], d_arr[3])
print(s_arr[4], d_arr[4])
print(s_arr[5], d_arr[5])