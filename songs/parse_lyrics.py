import json

import os

lyrics = []

directory_in_str = os.path.dirname(os.path.realpath(__file__))
directory = os.fsencode(directory_in_str)


def get_lyrics(data):
    return data['songs'][0]['lyrics']


for filename in os.listdir(directory):
    filename = filename.decode("utf-8")
    print(filename)
    if filename.endswith(".json"):
        with open(filename, 'r') as f:
            data = json.load(f)
        lyrics.append(get_lyrics(data))

with open('oxxymiron.txt', 'w') as f:
    f.write(' '.join(lyrics))