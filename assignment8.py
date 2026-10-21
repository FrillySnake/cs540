
# Author: Irakli Dokhnadze
# This program will read a list of numerical dollar amounts
# and their corresponding textual descriptions (akin to those found on a check)
# from a separate text file and identify any mismatches

GITHUB_LINK = 'https://github.com/FrillySnake/cs540'

number_words = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
                'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
                'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'one hundred': 100,}

with open('checks.txt', 'r', encoding='utf-8') as file:
    for line in file:
        og_text = line.strip()

        line = og_text.split('  ')

        for key, value in reversed(number_words.items()):
            line[1] = line[1].replace(key, str(value))

        line[1] = line[1].split(' ')
        line[1] = [line[1][1], line[1][4]]

        for index, item in enumerate(line[1]):
            item = item.split('-')
            if len(item) > 1:
                line[1][index] = str(int(item[0]) + int(item[1]))
            else:
                line[1][index] = item[0]

        if (len(line[1][1]) < 2):
            line[1][1] = '0' + line[1][1]

        line[1] = '.'.join(line[1])

        if (not line[0] == line[1]):
            print(f'Error found when validating "{og_text}": {line[0]} does not match {line[1]}')
            