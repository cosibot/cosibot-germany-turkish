#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to create the followings from questions.json :
# - nlu.md
# - list of intents seen in questions.json

from os import walk
import json
import html
import sys
import time
import re

lan=sys.argv[1]
path='../data/output/'

file= path + 'questions_translated_'+ lan +'.json'
with open(file) as json_file:
    data  = json.load(json_file)

# Correct cases appearing due to the translation
correction_map = {
  'tr': {
    '@De_languages': '@de_languages',
    '@de_languages': '@de_languages',
    '@ Dillere': '@de_languages',
    '@ dillere': '@de_languages',
    '@ dillerde': '@de_languages',
    "@de_languages'da": '@de_languages',
    '@ Diller': '@de_languages',
    '@Languages': '@de_languages',
    '@De_langauages': '@de_languages',
    '@De_games': '@de_games',
    '@de_games': '@de_games',
    '@De_Erdkunde': '@de_Erdkunde',
    '@En_politics': '@en_politics',
    '@De_expressions_negative': '@de_expressions_negative',
    '@ @__ionsions_positive': '@de_expressions_positive',
    '@De_expressions_positive': '@de_expressions_positive',
    '@De_countries': '@de_countries',
    '@Cities': '@cities',
    'Covid 19 inç @cities':"Covid 19 @cities'de",
     "Corona in @cities":"Corona @cities'de",
     "Aşk tanrısı": "Cupid"
     }
    }

def correct_data(x, lan):
    if lan in correction_map:
        for k,v in correction_map[lan].items():
            x = x.replace(k,v)
    return x

#Prepare nlu file from intents and questions
outfile_name = path + 'nlu_'+ lan +'_out.md'
with open(outfile_name, 'w') as outfile:
    for d in data['intents']:
        outfile.write('## intent: ' + d['intent'] + '\n')
        d['examples']= list(set([e['text']  for e in d['examples'] ]))
        for e in  d['examples']:
            e=correct_data(e, lan)
            outfile.write('- ' + e + '\n')
        outfile.write('\n')

#Output list for the intents in intents to compare to intents in asnwers
outfile_name = path + 'intentlist_from_intents.txt'
with open(outfile_name, 'w') as outfile:
    for d in data['intents']:
        outfile.write('- ' + d['intent'] + '\n')
