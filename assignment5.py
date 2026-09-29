GITHUB_LINK = 'https://github.com/FrillySnake/cs540'

# Author: Irakli Dokhnadze
# This program will provide a cipher function, which will cipher a sentence by removing all spaces and capitalizing all letters,
# and a decipher function to convert the cipher back into its original sentence.

def cipher_sentence(sentence):
    spaceIndices = []

    for index, char in enumerate(sentence):
        if char == ' ':
            spaceIndices.append(index)

    cipher = ''.join(sentence.split()).upper()
    return cipher, spaceIndices

def decipher_sentence(cipher, spaceIndices):
    sentence = cipher

    for index, char in enumerate(sentence):
        if index in spaceIndices:
            sentence = sentence[:index] + ' ' + sentence[index:]

    return sentence.capitalize()

sentence = 'The world population is increasing rapidly'
cipher, indices = cipher_sentence(sentence)

print(f'Ciphering "{sentence}" => "{cipher}"; spaces removed at {indices}')

print(f'Deciphering "{cipher}" => "{decipher_sentence(cipher, indices)}"')