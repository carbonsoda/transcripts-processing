import os
import gc
import pandas as pd
from decimal import Decimal

root = r"Q:\PSY-LAB\Suanda\Rollins\9mos"
path = r"P:\Suanda\1Sort\9master.txt"

calculated = []  # type = list

punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~'
transtab = str.maketrans(dict.fromkeys(punct, ''))


def analysis(filepath):
    df = pd.read_csv(filepath, header=None, usecols=[2], sep="\t", names=["utter"])
    df['utter'] = '|'.join(df['utter'].tolist()).translate(transtab).split('|')
    allutters = df["utter"].str.lower().str.split()

    flat_list = [str(item) for utter in allutters for item in utter]
    subject = filepath[56:60]
    rowcount = len(df.index)
    tokencount = sum(allutters.str.len())
    typecount = len(set(flat_list))
    avgtoken = round(Decimal(tokencount / rowcount), 3)
    avgtype = round(Decimal(typecount / rowcount), 3)

    gc.collect()
    return (subject, rowcount, tokencount, typecount, avgtoken, avgtype)


master = [] # type = list

with open(path, "r") as f:
    master = f.read().splitlines()
    f.close()

for filepath in master:
    if filepath.endswith(".txt"):
        calculated.append(analysis(filepath))  # they all txt files
    gc.collect()

labels = [
    "Subject",
    "Utterances",
    "Tokens",
    "Types",
    "Avg Token / Utterance",
    "Avg Type / Utterance",
]
data = pd.DataFrame(calculated, columns=labels)
data.set_index("Subject", inplace=True)
data.to_excel(os.path.join(root, "9mosAnalysis.xlsx"))
