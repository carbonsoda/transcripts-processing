import gc
import pandas as pd
from decimal import Decimal
from pathlib import Path
import pickle

root = r"Q:\PSY-LAB\Suanda\Rollins\9mos"
path = r"P:\Suanda\9master.txt"


def timetemp():
    temp = r"P:\Suanda\UtterAnalysis\time.pkl"
    if Path(temp).is_file():
        with open(temp, "rb") as f:
            return pickle.load(f)


times = timetemp()  # type = dict
calculated = []  # type = list


def analysis(filepath):
    punct = '!"#$%&\()*+-./:;<=>?@[\\]^_`{}~'
    transtab = str.maketrans(dict.fromkeys(punct, ''))

    df = pd.read_csv(filepath,
                     header=None,
                     # usecols=[2],
                     sep="\t",
                     names=["utter"]
                     )
    df['utter'] = '|'.join(df['utter'].tolist()).translate(transtab).split('|')
    allutters = df["utter"].str.lower().str.split()

    flat_list = [str(item) for utter in allutters for item in utter]
    subject = filepath[56:60].upper()
    rowcount = len(df.index)
    tokencount = sum(allutters.str.len())
    typecount = len(set(flat_list))
    avgtoken = round(Decimal(tokencount / rowcount), 3)
    avgtype = round(Decimal(typecount / rowcount), 3)

    sec = times[subject]
    mins = round(sec / 60, 4)
    tokensec = round(tokencount / sec, 5)
    tokenmin = round(tokencount / mins, 5)
    typesec = round(typecount / sec, 5)
    typemin = round(typecount / mins, 5)
    uttermin = round(rowcount / mins, 5)

    gc.collect()
    return (subject,
            sec, mins,
            rowcount,
            tokencount, typecount,
            avgtoken, avgtype,
            uttermin,
            tokensec, tokenmin,
            typesec, typemin
            )


master = []  # type = list

with open(path, "r") as f:
    master = f.read().splitlines()
    f.close()

for filepath in master:
    if filepath.endswith(".txt"):
        calculated.append(analysis(filepath))  # they all txt files
    gc.collect()

labels = [
    "Subject",
    "Time", "Time(min)",
    "Utterances",
    "Tokens", "Types",
    "Avg Token / Utterance", "Avg Type / Utterance",
    "Utt/min",
    "Tokens / sec", "Tokens / min",
    "Types / sec", "Types / min"
]
data = pd.DataFrame(calculated, columns=labels)
data.set_index("Subject", inplace=True)

root2 = r"Q:\PSY-LAB\Suanda\RA Work\AM\Data Files - TO VIEW\9mosAnalysis.xlsx"
data.to_excel(root2)