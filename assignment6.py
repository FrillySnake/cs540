import random

# Author: Irakli Dokhnadze
# This program will generate a list of configurable size randomly containing object names from a
# configurable list and identify all unique (occurring only once) objects in the generated list.

GITHUB_LINK = 'https://github.com/FrillySnake/cs540'

def populate_list(size, obj_choices):
    # creates a list of given size and fills it with elements selected randomly from the given obj_choices list
    return random.choices(obj_choices, k=size)

def identify_unique(objects_list):
    # identifies all unique (occurring only once) elements in the given objects_list
    uniques = [obj for obj in objects_list if objects_list.count(obj) == 1]
    return uniques

LIST_SIZE = 100
OBJECTS = ["chair", "table", "lamp", "book", "pencil", "phone", "computer", "keyboard",
           "mouse", "backpack", "bottle", "cup", "plate", "fork", "spoon", "knife", "clock",
           "mirror", "window", "door", "shoe", "hat", "jacket", "umbrella", "wallet", "keys",
           "camera", "television", "remote", "couch", "guitar", "basket", "towel", "scissors",
           "notebook", "stapler", "calculator", "headphones", "pillow", "blanket", "toothbrush",
           "comb", "brush", "soap", "candle", "vase", "bicycle", "helmet", "flashlight"]

objs = populate_list(LIST_SIZE, OBJECTS)
print(f'Generated object list: {objs}')
unique_objs = identify_unique(objs)
print(f'Unique elements: {unique_objs}')
