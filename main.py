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


#print("unmodified str score: " +str(str_score))   #prints str_score for tests

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

#skills will go here
Skills = {
  'strength': ['athletics',],
  'dexterity': ['acrobatics', 'sleight_of_hand', 'stealth'],
  'intelligence': ['arcana', 'history', 'investigation', 'nature', 'religion'],
  'wisdom': ['animal_handling', 'insight', 'medicine', 'perception', 'survival'],
  'charisma': ['deception', 'intimidation', 'performance', 'persuasion']
   }

#creating a class for the player character as a whole. Need to call the following classes into this somehow later: character_class, race, attributes (not built yet), Skills into this.
class PlayerCharacter:
  def __init__(self, *attributes, **kw):
    self.character_name = None
    self.total_character_level = None
    self.prof_bonus = None
    self.attributes = None
    self.attribute_bonuses = None
    self.armor_class = None
    self.initiative = None
    self.total_hit_dice = None
    self.max_hit_points = None
    self.languages = None
    self.background = None
    self.ideas = None
    self.bonds = None
    self.flaws = None
    self.traits = None
  
  def character_name(self):
    character_name = input("What is your name?\n")
    return (character_name)

  def calc_prof_bonus(self):
    if self.total_character_level >= 1 and self.total_character_level <= 4:
      self.prof_bonus = 2
    elif self.total_character_level >= 5 and self.total_character_level <= 8:
      self.prof_bonus = 3
    elif self.total_character_level >= 9 and self.total_character_level <= 12:
      self.prof_bonus = 4
    elif self.total_character_level >= 13 and self.total_character_level <= 16:
      self.prof_bonus = 5
    elif self.total_character_level >= 17 and self.total_character_level <= 20:
      self.prof_bonus = 6
    return self.prof_bonus


new_char = PlayerCharacter()
#new_char.character_name()

new_char.total_character_level = 12
new_char.calc_prof_bonus()
print (new_char.prof_bonus)


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

#def racial_attrib_score():
 # racial_attrib = (str_score + (Races['mountain_dwarf'].stat_mods['stre']))
  #return int(racial_attrib)

#str_score = racial_attrib_score()

#print("str with racial score: " + str(str_score))   #test print to see if attribute adder worked



#Contains features common to all classes. Proficiencies contains armor, weapons, tools, saving throws, skills
class CharacterClass:
  def __init__(self, character_class, **kw):
    self.character_class = character_class
    self.class_features = None
    self.hit_dice = None
    self.proficiencies = None
    self.class_level = 1



#Fighter is an instance of the CharacterClass class, this will go for all classes unless I use a JSON file.
Fighter = CharacterClass("fighter")

Fighter.class_features = {
  'fight_lvl_1': ['fighting_style', 'second_wind'],
  'fight_lvl_2': ['action_surge_1'],
  'fight_lvl_3': ['martial_archetype'],
  'fight_lvl_4': ['asi_1'],
  'fight_lvl_5': ['extra_attack_1'],
  'fight_lvl_6': ['asi_2'],
  'fight_lvl_7': ['martial_archetype_feature_1'],
  'fight_lvl_8': ['asi_3'],
  'fight_lvl_9': ['indomitable_1'],
  'fight_lvl_10': ['martial_archetype_feature_2'],
  'fight_lvl_11': ['extra_attack_2'],
  'fight_lvl_12': ['asi_4'],
  'fight_lvl_13': ['indomitable_2'],
  'fight_lvl_14': ['asi_5'],
  'fight_lvl_15': ['martial_archetype_feature_3'],
  'fight_lvl_16': ['asi_6'],
  'fight_lvl_17': ['action_surge_2', 'indomitable_3'],
  'fight_lvl_18': ['martial_archetype_feature_4'],
  'fight_lvl_19': ['asi_7'],
  'fight_lvl_20': ['extra_attack_3'],
}

Fighter.hit_dice = 10


Fighter.proficiencies = {
  'armor': ['light_armor', 'medium_armor', 'heavy_armor'],
  'weapons': ['simple_weapons', 'martial_weapons'],
  'saving_throws': ['strength', 'constitution'],
  'skills': ['acrobatics', 'animal_handling', 'athletics', 'history', 'insight', 'intimidation', 'perception', 'survival']
  }

#test of starting hp roll function for fighter
#def d10_starting_hp():
#  _ = Fighter.hit_dice + con_mod
#  return(_)

#d10_starting_hp = starting_hp()
#print(starting_hp)

#print(Fighter.class_features['fight_lvl_1'])
#print(Fighter.proficiencies['weapons'])