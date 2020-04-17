#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


a_ints=[]
path = "../data/output/"
file="intentlist_from_answers.txt"
with open(path + file) as f:
    for x in f:
        a_ints.append(x)

q_ints=[]
path = "../data/output/"
file="intentlist_from_questions.txt"
with open(path + file) as f:
    for x in f:
        q_ints.append(x)

in_a = sorted(list(set(a_ints)-set(q_ints)))
in_q = sorted(list(set(q_ints)-set(a_ints)))

in_both =  sorted([x for x in a_ints if x not in in_a])
# print(in_a)
# print(in_q)
# print(in_both)


file = 'intents_list.txt'
with open(path + file, 'w') as wf:

    wf.write('## Intents in questions but not in answers\n')
    for x in in_q:
        wf.write(x)
    wf.write('\n\n')
    wf.write('## Intents in answers but not in questions\n')
    for x in in_a:
        wf.write(x)
    wf.write('\n\n')
    wf.write('## Intents in both,  answers and questions\n')
    for x in in_both:
        wf.write(x)
