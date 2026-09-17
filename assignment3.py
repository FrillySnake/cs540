GITHUB_LINK = 'https://github.com/FrillySnake/cs540'

import sys

studentsDict = {}

def validateName(name):
    return all(c.isalpha() or c in ' -\'' for c in name)

try:
    for i in range(9):
        # ask for student name
        name = input('Enter a student\'s name: ').strip()
        if name == '':
            raise Exception('Name cannot be an empty or blank string!')
        if not validateName(name):
            raise Exception('Name contains an illegal character!')
        if not len(name.split()) == 2:
            raise Exception('Name must consist of two words: a first and last name!')
        if name in studentsDict.keys():
            raise Exception('Cannot put the same name twice!')

        # ask for number of courses being taken by student
        courses = input(f'Number of courses being taken by {name}: ')
        if not courses.isdigit():
            raise Exception('Number of courses must be an integer with no decimals (even if just zeros)!')
        studentsDict[name] = int(courses)
except Exception as e: 
    print(f'Error: {e}')
    sys.exit()

# Uncomment the below line to use a default list of 9 names and courses taken instead (ideally comment out the try-except block above as well)
# studentsDict = {'Osian Sanders': 3, 'Giovanni Macdonald': 2, 'Milo Stevenson': 5, 'Ayden Moyer': 9, 'Arron Sampson': 0, 'Wesley Hood': 100, 'Joan Cannon': 1, 'Rae Mcdermott': 4, 'Colby Forrest': 4}

def fullTime(student):
    return (studentsDict[student] > 2)

for student in studentsDict.keys():
    print(f'{student}: {'Full-time' if fullTime(student) else 'Part-time'}')