'''
Sorts through transcript to find all unique words, then writes to text file (creates if not existing)

To-do: 
This is just for right now, afterwards I'll rework it to check for duplicates
Then I can also readjust for root words + types of words (fish noun vs verb)

-remove dups
- accept input of filedirectory
    - or should go through entire age folder?
    - if so, ask for how many months:
    filepath = "Q:/..../.../" + age + "mos/" 
'''

import pandas as pd
import numpy as np
from itertools import chain
import os

filename = r"Q:\PSY-LAB\Suanda\Rollins\9mos\cd09\Data\Transcriptions\CD09_trans_final.xlsx"
labels = ["start", "end", "utter", "over-parsing", "under-parsing"]

data = pd.read_excel(filename, header=None, names=labels)
df = pd.DataFrame(data, columns=["utter"]).dropna(how='any', axis=0)

dictionarypath = os.path.join(os.environ["USERPROFILE"], "Desktop") + os.sep + "dictionary9mos.txt"

def rows():
    phrasesList = list(df.utter.str.split(expand=False)) # returns as 2 dimensional list

    for i in range(1, len(phrasesList)):
            if type(phrasesList[i]) is list:
                for j in range(len(phrasesList[i])):
                    # would probs want to run duplicate remover once there's tags assigned (ie verb, noun)
                    filewriter(phrasesList[i][j])

def filewriter(word):
    with open(dictionarypath, 'a+') as d:
        print(word, file=d)

def duplicteremove(textfile):
    pass


rows()