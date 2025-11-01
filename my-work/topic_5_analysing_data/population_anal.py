# analysisng population wrong
# Author: Tihana Gray

import pandas as pd 
from pathlib import Path

FILENAME="population_for_analysis.csv"
DATADIR= Path(r"C:\Users\tihan\OneDrive\Desktop\ATU\programming-for-data-analytics\data")
FULLPATH =  DATADIR / FILENAME

df = pd.read_csv(FULLPATH)

#print (df.head(3))
headers = df.columns[1:]
print (headers)
district = headers[0]
print (df[district].describe())
print(df[district])