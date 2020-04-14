#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:17:53 2020

@author: jennifer
"""

import pandas as pd
from collections import defaultdict
import yaml
from yaml.representer import Representer
import re

output_file = 'domain_out.yml'

#so we can print yaml with defaultdict settings
yaml.add_representer(defaultdict, Representer.represent_dict)

# df = pd.read_excel('../data/Cosibot-Answers-DE-TR.xlsx')
df = pd.read_csv('../data/Cosibot-Answers-DE-TR.csv', header=0)

def get_response_type(response):
    if response.startswith('<speak>'):
        rtype = 'ssml'
    elif response.startswith('<p>'):
        rtype = 'html'
    else:
        rtype = 'text'
    return rtype

domain_dict = defaultdict(list)
for index, row in df.iterrows():
    category = str(row["Node Title"]).lower()
    answer = str(row["Answer"]).replace('XXXXX', 'nan') #some data cleaning XXXX

    # if intent == 'nan':
    #     intent = str(row["ParentTitle"]).lower()

    # we ignore asnwers where Node Title is NAN
    # Alterantively we could assign them ParentTitle as intent but these cases seems to correspond to testing and other process related situation
    if answer != 'nan' and category != 'nan':
        #take care of duplications
        if answer not in domain_dict[category]:
            domain_dict[category].append(answer)

domain_responses = defaultdict(list)

for category, responses in domain_dict.items():
    category = re.sub(r'^de_', '', category)
    domain_responses['utter_' + category] = [{
        'custom': {
            'answers': [{'type': get_response_type(response),
                         'text':  response} for response in responses]
        }
    }]

final_dict = {'responses': domain_responses}

file = '../data/' + output_file
with open(file, 'w') as wfile:
    #add intents from intent.txt file
    wfile.write('intents:\n')
    with open('../bot/data/nlu.md', 'r') as nluf:
        for line in nluf:
            if '##' in line:
                wfile.write(line.replace('## intent:', '- '))
    # add responses
    documents = yaml.dump(final_dict, wfile, allow_unicode=True)
