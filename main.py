from random import randint
import numpy as np

#roll 6 numbers between 8 and 18 and add them to a list called dice_list. "return" stores the variable in the list and makes it usable. 8-18 provides a medium-to-high character power level.
#rewrite this as an array so I don't have to convert later?

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

#character attribute names as constants
strength = s_arr[0]
dexterity = s_arr[1]
constitution = s_arr[2]
intelligence = s_arr[3]
wisdom = s_arr[4]
charisma = s_arr[5]

#Stat variables go here
str_score = d_arr[0]
dex_score = d_arr[1]
con_score = d_arr[2]
int_score = d_arr[3]
wis_score = d_arr[4]
cha_score = d_arr[5]

print("unmodified str score: " +str(str_score))   #prints str_score for tests

#do this as one command in the future, iterate with for loop?
#print(s_arr[0], str_score)
#print(s_arr[1], dex_score)
#print(s_arr[2], con_score)
#print(s_arr[3], int_score)
#print(s_arr[4], wis_score)
#print(s_arr[5], cha_score)

#Attribute Bonuses go here. Formula calculates correct bonuses, assuming Attribute of 10-11 = +0
str_mod = ((str_score//2)-5)
dex_mod = ((dex_score//2)-5)
con_mod = ((con_score//2)-5)
int_mod = ((int_score//2)-5)
wis_mod = ((wis_score//2)-5)
cha_mod = ((cha_score//2)-5)

#Races will go here. Class has kw arg so that these items cna be referenced in other functions. These items are the defaults, applied to all races - exceptions are written into the races (most races are medium, so medium is the default. halflings are small, so will have a 'size' of 'small'.)
#Dragonborn, Dwarf, Elf, Gnome, Half-elf, Halfling, Half-Orc, Human, Tiefling
class Race:
  def __init__(self, race, **kw):
    self.race = race
    self.size = kw.get('size', 'medium')
    self.speed = kw.get('speed', 30)
    self.stat_mods = kw.get('stat_mods')
  #most races share the above traits, so those traits are listed above.

#individual races are listed below - subraces are, for now, listed as their own races. These races will assume the information from the above class, unless they replace that information with their own.
Races = {
#need to write draconic ancestry

  'dragonborn': Race('dragonborn', stat_mods={
      'stre': 2,
      'cha': 1, 
      'abilities': 'draconic_ancestry'
  }),

#Need to fill out the dwarven abilities and decide how best to append these
  'hill_dwarf': Race('hill_dwarf', stat_mods={
      'con': 2,
      'wis': 1,
      'speed': 25,
      'size': 'small',
      'abilities': ['darkvision', 'dwarven_resilience', 'dwarven_combat', 'dwarf_tool_prof', 'stonecunning', 'dwarven_toughness'],
      'languages': 'dwarf'
  }),

  'mountain_dwarf': Race('mountain_dwarf', stat_mods={
      'con': 2,
      'stre': 2,
      'speed': 25,
      'size': 'small',
      'abilities': ['darkvision', 'dwarven_resilience', 'dwarven_combat', 'dwarf_tool_prof', 'stonecunning', 'dwarven_armor_training'],
      'languages': 'dwarf'
  })
}

#adds racial attribute bonus to str_score and redefines str_score as the new number. Will edit this later to be either universal, or add more equations per race.

def racial_attrib_score():
  racial_attrib = (str_score + (Races['mountain_dwarf'].stat_mods['stre']))
  return int(racial_attrib)

str_score = racial_attrib_score()

print("str with racial score: " + str(str_score))   #test print to see if attribute adder worked