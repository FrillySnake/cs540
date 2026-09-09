GITHUB_LINK = 'https://github.com/FrillySnake/cs540'

import sys
import random

names = []

def validateName(name):
    return all(c.isalpha() or c in ' -\'' for c in name)

try:
    for i in range(9):
        name = input('Enter a student\'s name: ').strip()
        if name == '':
            raise Exception('Name cannot be an empty or blank string!')
        if not validateName(name):
            raise Exception('Name contains an illegal character!')
        if not len(name.split()) == 2:
            raise Exception('Name must consist of two words: a first and last name!')
        if name in names:
            raise Exception('Cannot put the same name twice!')
        names.append(name)
except Exception as e: 
    print(f'Error: {e}')
    sys.exit()

# Uncomment the below line to use a default list of 9 names instead (ideally comment out the try-except block above as well)
# names = ['Osian Sanders', 'Giovanni Macdonald', 'Milo Stevenson', 'Ayden Moyer', 'Arron Sampson', 'Wesley Hood', 'Joan Cannon', 'Rae Mcdermott', 'Colby Forrest']

def nameFunc(name):
    return name.split()[-1]

sortedNames = sorted(names, key=nameFunc)
sortedCopy = sortedNames[:]

groups = [[], [], []]
i = 0

while sortedNames:
    if i == 100:
        groups = [[], [], []]
        sortedNames = sortedCopy[:]
    name = sortedNames[-1]
    group = random.randint(0, 2)
    try:
        pos = sortedCopy.index(name)
    except ValueError:
        print('Something went wrong...')
    if (pos > 0 and sortedCopy[pos-1] in groups[group]) or (pos+1 < len(sortedCopy) and sortedCopy[pos+1] in groups[group]) or len(groups[group]) == 3:
        i = i + 1
        continue
    sortedNames.pop()
    i = 0
    groups[group].append(name)

# Uncomment the below line to have the sorted list of names also be displayed (mainly for confirmation)
# print(f'Sorted names: {sortedCopy}')
print(f'Group 1: {groups[0]}')
print(f'Group 2: {groups[1]}')
print(f'Group 3: {groups[2]}')