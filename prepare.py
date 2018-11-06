# from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import json
import pandas as pd


class Prepare:

    def __init__(self, data):
        self.data = data

    def tokenizeAndRemovePunct(self):
        tok = RegexpTokenizer("[\w']+")
        filterArr = tok.tokenize(self.data['text'])
        filterArr = [x.lower() for x in filterArr]
        self.data['text'] = filterArr


# ====================read data, tokenize and clean=============================================================

in_json = []

# read file
with open('dataset/json_data.json', 'r') as f:
    data = json.load(f)

# map through the data and tokenize
for datum in data:
    currData = Prepare(datum)
    currData.tokenizeAndRemovePunct()
    json_data = {
        'text': currData.data['text'],
        'label': currData.data['label']
    }
    in_json.append(json_data)

# save json to file
with open('prepared_dataset/json_data.json', 'w') as f:
    temp = json.dumps(in_json)
    f.write(temp)


# ===============================form number to unique word dictionary============================

uniqueWordsArr = []
uniqueWordsMap = {}
number = 0

with open('prepared_dataset/json_data.json', 'r') as f:
    data = json.load(f)

for datum in data:
    for i in datum['text']:
        if not i in uniqueWordsArr:
            number = number + 1
            uniqueWordsArr.append(i)
            uniqueWordsMap[number] = i

with open('prepared_dataset/numToWord.json', 'w') as f:
    temp = json.dumps(uniqueWordsMap)
    f.write(temp)


# ==================================replace words with numbers===========================================

in_json2 = []

with open('prepared_dataset/json_data.json', 'r') as f:
    data = json.load(f)

with open('prepared_dataset/numToWord.json', 'r') as f:
    num_data = json.load(f)

# map through the data and tokenize
for datum in data:
    numarr = []
    for row in datum['text']:
        # get the key
        key = [key for key, value in num_data.items() if value == row]

        # append to numarr
        numarr.append(key[0])

    print(numarr)
    # new json data
    json_data = {
        'text': numarr,
        'label': datum['label']
    }

    in_json2.append(json_data)

# save json to file
with open('prepared_dataset/num_json_data.json', 'w') as f:
    temp = json.dumps(in_json2)
    f.write(temp)
