#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to pick up user questions with intents from Watson input file

import json
import re

file='../data/skill-COVID19-Bot-0-0-1-DE.json'
with open(file) as json_file:
    all_data  = json.load(json_file)

final_dict={'intents': all_data['intents']}
output_file = '../data/questions.json'
with open(output_file, 'w') as out:
    json.dump(final_dict , out, indent=4, ensure_ascii=False)
