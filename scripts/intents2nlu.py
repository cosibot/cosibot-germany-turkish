#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv

prefix ='de_'
intents={}
output_file = 'nlu_out_3.md'

with open("../data/cosibot-intents-de-en-tr.csv") as f:
    src = csv.reader(f, delimiter=',')
    for row in src:
        type = row[1].replace(prefix, '')
        if type not in intents.keys():
            intents[type]= [row[0]]
        else:
            intents[type].append(row[0])


file = '../data/' + output_file
with open(file, 'w') as wf:
    for type, ints in intents.items():
         intents[type] = list(set(ints))
         # print('## intent:',type)
         wf.write('## intent: ' + type + '\n')
         for i in ints:
             wf.write('- ' + i + '\n')
             # print('- ', i)
         wf.write('\n')
         # print('\n')
