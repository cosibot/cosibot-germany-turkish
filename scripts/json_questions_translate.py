#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to translate questions via google api

from os import walk
import json
import html
import sys
import time
import re

# from google.cloud import translate_v2 as translate
# translate_client = translate.Client.from_service_account_json('account_credentials.json')
# target = sys.argv[1]


def translate(text):
    # return html.unescape(translate_client.translate(text, target_language= target)['translatedText'])
    return text.upper()

file='../data/questions.json'
with open(file) as json_file:
    data  = json.load(json_file)


outfile_name = '../data/output/questions_translated.json'
with open(outfile_name, 'w') as outfile:
    for d in data['intents']:
        d['intent'] = re.sub(r'^de_', '', d['intent'])
        for e in  d['examples']:
            e['text'] = translate(e['text'])
        time.sleep(1)
    json.dump(data, outfile, indent=4, ensure_ascii=False)
