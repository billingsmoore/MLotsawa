import pyewts
import json

converter=pyewts.pyewts()

with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/bing/response.json') as f:
    d = json.load(f)

tib = []

for entry in d:
    tib.append(converter.toWylie(entry['translations'][0]['text']))

eng = []

with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/ankhi/bing-batches/mini-batches/mini-batches0.txt', 'r') as f:
    for line in f:
        eng.append(line)

pairs = []

for i in range(len(tib)):
    pairs.append((tib[i], eng[i]))

with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/bing/minibatch0-pairs.txt', 'w') as f: # make sure to change to 'a'
    f.writelines('\n'.join(str(pair).replace('\'', '')
                                    .replace('\\n', '')
                                    .replace('(', '')
                                    .replace(')', '')
                                    .replace('/', '')
                                    .replace(' ,', ',')
                                    .replace('"', '')  for pair in pairs))