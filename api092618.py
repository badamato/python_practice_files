##Chris's code for calling the GOT api
import requests
import json
import time


URL = 'https://anapioficeandfire.com/api/characters?page=%d&pageSize=100'
DELAY = 1
OUTPUT = 'got.json'

chars = []
clean_chars = []

##make request to the API
for page in range(1, 50):
    print('Making request for page %d' % page)
    r = requests.get(URL % page)
    new_chars = r.json()
    if len(new_chars) == 0:
        break
    chars.extend(r.json())
    print('Sleeping...\n\n')
    time.sleep(DELAY)

##only people with names
for char in chars:
    if len(char['name']) > 0:
        clean_chars.append(char)

print('Got %d characters!' % len(clean_chars))