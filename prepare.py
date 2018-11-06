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


# =================================================================================
# empty array
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

# save file to json
with open('prepared_dataset/json_data.json', 'w') as f:
    temp = json.dumps(in_json)
    f.write(temp)


uniqueWordsArr = []
uniqueWordsMap = {}
number = 0

# form number to unique word dictionary
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
