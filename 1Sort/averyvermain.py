import pandas as pd
import numpy as np
from itertools import chain
import os



rootbasic = 'Q:\PSY-LAB\Suanda\Rollins'

# modular by age for right now, later maybe can do all at once
age = input("Input how many months \n") + "mos"
root = os.path.join(rootbasic, age)

i = 0
for subjects in os.walk(root):
    print ()
    # if os.path.isdir()
    print (subjects)
    i = i + 1
    if i is 5:
        break
    # filename = os.path.join(root,)
