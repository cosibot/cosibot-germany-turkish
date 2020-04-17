#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Code to format answers as csv

from os import walk
import json
import csv

path='../data/answers/'

files = []
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)


files=[f  for f in files if f.startswith('de_')]
# files =['de_germany_precautions_schleswigholstein.json', 'de_work_infection.json']


file = path + 'output/all_answers.csv'
with open(file, 'w') as csv_out:
    wf = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for f in files:
        print(f.upper())
        with open(path + f) as json_file:
            data = json.load(json_file)
            lst=data['answers']
            intent = f.replace('de_', '').replace('.json', '')
            for i, d in  enumerate(lst):
                if d['type'] == 'ssml':
                    wf.writerow([intent , 'ssml', '',  d['ssml']])
                elif d['type']  == 'html':
                    wf.writerow([intent , 'html', '',  d['text']])
                elif d['type']  == 'text':
                    wf.writerow([intent, 'text','',d['text']])
                elif d['type'] == 'hints':
                    options = d['options']
                    for j, hnt in  enumerate(options):
                        wf.writerow([intent, 'hints', hnt['label'], hnt['value']])
                elif d['type'] == 'links':
                    options = d['links']
                    for j, lnk in  enumerate(options):
                        wf.writerow([intent, 'links', lnk['title'], lnk['url']])
