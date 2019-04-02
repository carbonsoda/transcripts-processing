import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

install("pandas")

import pandas as pd
import gc
import os
import pickle
from pathlib import Path


class Setup:

    def __init__(self):
        self.dictionary = []
        self.wordsmaster = {}
        self.templabels = [
            "subject",
            "timeS",
            "timeE",
            "utter"
        ]
        self.picklepath = r"Q:\PSY-LAB\Suanda\RA Work\AM\Tasks\WordSearch"
        self.dictpath = os.path.join(
            self.picklepath, "dict.pkl")
        self.wordspath = os.path.join(
            self.picklepath, "wordsmaster.pkl")

        self.dictsetup()
        self.wordssetup()
        self.picklesave()

    def getdictionary(self):
        return self.dictionary

    def getwordsmaster(self):
        return self.wordsmaster

    def dictsetup(self):
        dictpath = r"Q:\PSY-LAB\Suanda\RA Work\AM\Data Files - TO VIEW\9mosDictionary.txt"
        with open(dictpath, "r") as f:
            self.dictionary = f.read().splitlines()
            f.close()

    def sorting(self, filepath):
        df = pd.read_csv(
            filepath,
            header=None,
            sep="\t",
            names=self.templabels
        )

        subject = filepath[56:60]

        for row in df.itertuples():
            for word in self.dictionary:
                if word in row[3].lower():
                    self.wordsmaster[word].append(tuple((
                        subject,
                        row[1],
                        row[2],
                        row[3])
                    ))

    def wordssetup(self):
        path = r"Q:\PSY-LAB\Suanda\RA Work\AM\Tasks\WordSearch\9master.txt"

        filelist = []  # type = list

        with open(path, "r") as f:
            filelist = f.read().splitlines()
            f.close()

        self.wordsmaster = {key: [] for key in self.dictionary}

        for filepath in filelist:
            self.sorting(filepath)
        gc.collect()

    def picklesave(self):
        if not self.dictionary:  # if empty
            with open(self.dictpath, "wb") as f:
                pickle.dump(self.dictionary, f)
        if not self.wordsmaster:  # if empty
            with open(self.wordspath, "wb") as f:
                pickle.dump(self.wordsmaster, f)

    def pickles(self):
        # actually i think i don't need dictionary but w/e

        if Path(self.dictpath).is_file() and Path(self.wordspath).is_file():
            with open(self.dictpath, "rb") as f:
                self.dictionary = pickle.load(f)
            with open(self.wordspath, "rb") as f:
                self.wordsmaster = pickle.load(f)
        else:
            print("\n setup went wrong!! \n")


# setup
# should modify so it checks if sqlite db is empty, then run setup
initial = Setup()
if not initial.wordsmaster:
    initial.pickles()

dictionary = initial.getdictionary()  # type = list
wordsmaster = initial.getwordsmaster()  # type = dict with format key:[list of tuples]
gc.collect()


def questioning():
    while True:
        token = input("What word/token are you exactly looking for?").lower()
        print(token)
        if token in dictionary:
            break
        else:  # Asks question again
            print("That word does not exist in any of the transcripts. \n Please check the spelling and try again.")
            continue
    return token


token = questioning().lower()

wordlist = wordsmaster[token]
df = pd.DataFrame.from_records(
    wordlist,
    columns=[
        "Subject",
        "Time Start",
        "Time End",
        "Utterance"
    ]
)

root = r"Q:\PSY-LAB\Suanda\RA Work\AM\Data Files - TO VIEW\Words" + os.sep + token
file = token + "records.xlsx"

df.to_excel(r"Q:\PSY-LAB\Suanda\RA Work\AM\Tasks\WordSearch\Words" + os.sep + token + "record.xlsx", index=False)
