import json
import pandas as pd

dataset = []
in_json = []

for i in range(1, 92):
    # read a single dataset file
    try:
        real_filename = "dataset/buzzfeed/BuzzFeed_Real_%s-Webpage.json" % i
        fake_filename = "dataset/buzzfeed/BuzzFeed_Fake_%s-Webpage.json" % i

        # real
        print("Reading file %s" % real_filename)
        data = pd.read_json(real_filename, lines=True)
        json_data = {
            'text': data['text'].values[0],
            'label': 'Real'
        }
        data['label'] = 'Real'
        data = data[['text', 'label']]
        print("Completed: {0:.2f}%".format(((i / 91) * 100)))
        # set column structure for the global dataset
        dataset.append(data)
        in_json.append(json_data)

        # fake
        print("Reading file %s" % fake_filename)
        data = pd.read_json(fake_filename, lines=True)
        json_data = {
            'text': data['text'].values[0],
            'label': 'Fake'
        }
        data['label'] = 'Fake'
        data = data[['text', 'label']]
        print("Completed: {0:.2f}%".format(((i / 91) * 100)))

        # set column structure for the global dataset
        dataset.append(data)
        in_json.append(json_data)
    except:
        print(i)

    # dataset.loc[i] = data.loc[0]

print("Done!!!!!!!!!!!")
# merge dataset
dataset = pd.concat(dataset)
dataset.to_pickle("dataset/dataset.pkl")

# save json data file
with open('dataset/json_data.json', 'w') as f:
    temp = json.dumps(in_json)
    f.write(temp)

# dataset = pd.read_pickle("dataset.pkl")
# print(dataset)
