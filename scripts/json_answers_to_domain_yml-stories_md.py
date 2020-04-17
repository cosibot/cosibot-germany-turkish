#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to create the followings from answers.json :
# - domain.yml
# - stories.yml
# - list of intents seen in asnwers.json

import sys
import json
import yaml
from yaml.representer import Representer

lan=sys.argv[1]

path='../data/output/'
f = 'answers_translated_'+ lan +'.json'


with open(path + f) as json_file:
    answers  = json.load(json_file)

utter_answers={}
for intent, val in answers.items():
    utter_answers['utter_' + intent] = {'custom': val}

final_dict = {'responses': utter_answers}

## Prepare domain file
outfile_name = path + 'domain_'+ lan +'_out.yml'
with open(outfile_name, 'w') as domainfile:
    yaml.dump(final_dict, domainfile, allow_unicode=True)

# Prepare stories from answers intents
outfile_name = path + 'stories_'+ lan +'_out.md'
with open(outfile_name, 'w') as storiesfile:
    for intent in answers:
        storiesfile.write('## '+ intent + ' path'+ '\n')
        storiesfile.write('* ' + intent + '\n')
        storiesfile.write('     - utter_' + intent + '\n\n')

#Output list for the intents in intents to compare to intents in asnwers
outfile_name = path + 'intentlist_from_answers.txt'
with open(outfile_name, 'w') as outfile:
    for intent in answers:
        outfile.write( '- '+ intent + '\n')
