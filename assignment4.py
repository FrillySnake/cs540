GITHUB_LINK = 'https://github.com/FrillySnake/cs540'

# Author: Irakli Dokhnadze
# This program will ask the user to pick a secret number and continuously guess numbers,
# using feedback from the user on whether the secret number is higher or lower, until it guesses (or is unable to guess) the secret number.

import time
import random

print('I\'ll give you 5 seconds to pick a secret number (an integer from 0-50)! After that, I\'ll try to guess it!')
time.sleep(5)

min = 0
max = 50

while True:
    if min > max:
        print('Hang on... you lied to me or picked an invalid number! No fair!')
        break
    guess = random.randint(min, max)
    print(f'My guess is... {guess}!')
    match input('Is my guess correct or is the secret number higher or lower than my guess? (C/H/L): '):
        case 'C' | 'c':
            print('Yay! Thanks for playing!')
            break
        case 'H' | 'h':
            print('Got it! Retrying...')
            min = guess+1
            time.sleep(3)
        case 'L' | 'l':
            print('Got it! Retrying...')
            max = guess-1
            time.sleep(3)
        case _:
            print('Irregular input detected, retrying...')
            time.sleep(3)
            continue