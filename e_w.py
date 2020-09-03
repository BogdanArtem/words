import os
import sys
from urllib.request import urlopen, urlretrieve
import requests
import json

word = sys.argv[1].lower()



path_to_save = '/Users/artembogdan/Downloads'
frovo_url = f'https://apifree.forvo.com/key/bcfa84619ae534b16d2ae111d5dc9591/format/json/action/standard-pronunciation/word/{word}/language/en'

response = requests.get(frovo_url)
json_resp = response.json()
download_from = json_resp['items'][0]['pathmp3']

mp3 = requests.get(download_from, stream = True)

with open(os.path.join(path_to_save, f"{word}.mp3"),"wb") as mp3_f:
    for chunk in mp3.iter_content(chunk_size=1024):

         # writing one chunk at a time to pdf file
         if chunk:
             mp3_f.write(chunk)



from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()
another_word = parser.fetch(word, 'english')
try:
	print(another_word[0]['pronunciations']['text'][0])
except IndexError:
	print("THE INDEX IS OUT OF RANGE")
	print(another_word)



