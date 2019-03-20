import os
import gc
import pandas as pd
import re

def masterget(path):
    temp = []
    with open(path, "r") as f:
        temp = f.read().splitlines()
        f.close()
    return temp


path = r"C:\Users\mille\Desktop\master\9master.txt"
master = masterget(path)
df = pd.DataFrame(index=master, columns=["subject", "B", "C", "D", "E", "F"])

data = {}
def typesort():
    for item in master:
        if "xlsx" in master:
            pass
        else: # logically only other possibility is txt
            print(item)
            pass