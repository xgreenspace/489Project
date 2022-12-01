import csv
import pandas as pd
import numpy as np
import glob
from pathlib import Path
import os




df = pd.DataFrame()
path = os.path.dirname(os.path.realpath(__file__))


for i in range(1,4):
    files = glob.glob(path + '\Person{0}\*.BMP'.format(i))
    for filename in files:
        print(os.path.basename(filename))
        df = pd.concat([df, pd.DataFrame([[os.path.basename(filename), i - 1]])])

print(df)
df.to_csv('directories.csv', index=False)