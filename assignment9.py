import re

# Author: Irakli Dokhnadze
# This program reads in the content of an HTML file and, using regex,
# prints out all included web links in alphabetical order.

GITHUB_LINK = 'https://github.com/FrillySnake/cs540'

with open('index.html', 'r', encoding='utf-8') as file:
    html = file.read()

body = re.search(r'< *body(.\n*)*< *\/body *>', html).group()

links_list = re.findall(r'href *= *".*?"', body)

for index, item in enumerate(links_list):
    links_list[index] = item.split('"')[1]

links_list.sort()

print('Web links found: ')
for i in links_list:
    print(i)
