import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/project-co-work/repo/main/Data/Raw/S%26P500.csv?token=AQQXYUGCTNQTF2XIRFONLQ2725AJA')
print(df.tail())
df.dropna(how='any').shape
