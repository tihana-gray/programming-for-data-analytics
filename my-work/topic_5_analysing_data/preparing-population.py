# Preparing the population data for analysis
# The CSO data is quite clean 
# All we realy have to do is group it
# Author: Tihana Gray

import pandas as pd 
from pathlib import Path

FILENAME="cso-populationbyage.csv"
DATADIR= Path(r"C:\Users\tihan\OneDrive\Desktop\ATU\programming-for-data-analytics\data")
FULLPATH =  DATADIR / FILENAME

df = pd.read_csv(FULLPATH)

drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"]
#df = df.drop(columns=drop_col_list)
df.drop(columns=drop_col_list, inplace=True)

df = df[df["Single Year of Age"] != "All ages"]
df["Single Year of Age"] = df["Single Year of Age"].str.replace('Under 1 year', '0')
df["Single Year of Age"] = df["Single Year of Age"].str.replace(r'\D', '', regex=True)

df['Single Year of Age']=df['Single Year of Age'].astype('int64')

#df_anal =pd.crosstab(df.loc[:, 'Administrative Counties'], df.loc[:, 'Single Year of Age'])
df_anal = pd.pivot_table(df, 'VALUE',"Single Year of Age","Administrative Counties")
print (df_anal.head(10))
df_anal.to_csv("population_for_analysis.csv")