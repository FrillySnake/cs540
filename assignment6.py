import random

# Author: Irakli Dokhnadze
# This program will 

GITHUB_LINK = 'https://github.com/FrillySnake/cs540'

def populate_list(size=5, objects=['apple', 'banana', 'cup', 'tissue', 'pencil']):
    # creates a list of given size and fills it with elements selected randomly from the given objects list
    # object_list = []

    # for i in range(size):
    #     object_list.append(objects[random.choice[]])
    return random.choices(objects, k=size)

def identify_unique(objects_list):
    # identifies all unique (occurring only once) elements in the given objects_list
    uniques = [obj for obj in objects_list if objects_list.count(obj) == 1]
    return uniques

list_size = 100
objects = ["chair", "table", "lamp", "book", "pencil", "phone", "computer", "keyboard",
           "mouse", "backpack", "bottle", "cup", "plate", "fork", "spoon", "knife", "clock",
           "mirror", "window", "door", "shoe", "hat", "jacket", "umbrella", "wallet", "keys",
           "camera", "television", "remote", "couch", "guitar", "basket", "towel", "scissors",
           "notebook", "stapler", "calculator", "headphones", "pillow", "blanket", "toothbrush",
           "comb", "brush", "soap", "candle", "vase", "bicycle", "helmet", "flashlight"]

objs = populate_list(list_size, objects)
print(f'Generated object list: {objs}')
unique_objs = identify_unique(objs)
print(f'Unique elements: {unique_objs}')
