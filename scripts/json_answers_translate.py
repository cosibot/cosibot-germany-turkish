#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to translate answers via google api

from os import walk
import json
import csv
import html
import sys
import time

from google.cloud import translate_v2 as translate
translate_client = translate.Client.from_service_account_json('account_credentials.json')
target = sys.argv[1]


def translate(text):
    return html.unescape(translate_client.translate(text, target_language= target)['translatedText'])

path='../data/answers/'
files = []
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)

files=[f  for f in files if f.startswith('de_')]
# files =['de_germany_precautions_schleswigholstein.json', 'de_work_infection.json']


translated = {}

outfile_name = path + '../data/output/answers_translated_' + target + '.json'
with open(outfile_name, 'w') as outfile:
    for f in files:
        intent = f.replace('de_', '').replace('.json', '')
        # print(intent.upper())
        with open(path + f) as json_file:
            translated[intent]  = json.load(json_file)
            lst = translated[intent]['answers']

            for i, d in  enumerate(lst):
                if d['type'] == 'ssml':
                    d['ssml'] =translate(d['ssml'])
                elif d['type'] in ['html', 'text']:
                    d['text'] =translate(d['text'])
                elif d['type'] == 'hints':
                    options = d['options']
                    for j, hnt in  enumerate(options):
                        hnt['label'] =translate(hnt['label'])
                        hnt['value'] =translate(hnt['value'])
                elif d['type'] == 'links':
                    options = d['links']
                    for j, lnk in  enumerate(options):
                        lnk['title'] =translate(lnk['title'])
        print(f)
        time.sleep(1)
    json.dump(translated, outfile, indent=4, ensure_ascii=False)
