import os
import csv

path = os.getcwd()
prefix ='de_'
intents={}

with open(path + "/cosibot-intents-de-en-tr.csv") as f:
    src = csv.reader(f, delimiter=',')
    for row in src:
        type = row[1].replace(prefix, '')
        if type not in intents.keys():
            intents[type]= [row[0]]
        else:
            intents[type].append(row[0])

for type, ints in intents.items():
     intents[type] = list(set(ints))
     print('## intent:',type)
     for i in ints:
         print('- ', i)
     print('\n')
