import os
import sys
from urllib.request import urlopen, urlretrieve
import requests
import json

word = " ".join(str(arg) for arg in sys.argv[1:])
path_to_save = '/Users/artembogdan/Downloads'

def get_ipa(word):
    from wiktionaryparser import WiktionaryParser
    parser = WiktionaryParser()
    another_word = parser.fetch(word, 'french')
    try:
    	print(another_word[0]['pronunciations']['text'][0])
    except IndexError:
    	print("WIKI ERROR: THE INDEX IS OUT OF RANGE")


def download_word(word, path):
    frovo_url = f'https://apifree.forvo.com/key/bcfa84619ae534b16d2ae111d5dc9591/format/json/action/standard-pronunciation/word/{word}/language/fr'
    response = requests.get(frovo_url)
    json_resp = response.json()
    try:
        download_from = json_resp['items'][0]['pathmp3']
    except IndexError:
        print('NO STANDART')
        frovo_url = f'https://apifree.forvo.com/key/bcfa84619ae534b16d2ae111d5dc9591/format/json/action/word-pronunciations/word/{word}/language/fr'
        response = requests.get(frovo_url)
        json_resp = response.json()
        download_from = json_resp['items'][0]['pathmp3']


    mp3 = requests.get(download_from, stream = True)
    with open(os.path.join(path, f"{word}.mp3"),"wb") as mp3_f:
        for chunk in mp3.iter_content(chunk_size=1024):

             # writing one chunk at a time to pdf file
             if chunk:
                 mp3_f.write(chunk)
    print('DOWNLOADED')


get_ipa(word)
download_word(word, path_to_save)


