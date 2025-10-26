# code snippets for lectures
# Author: Tihana Gray

import pandas as pd
# up two levels past topic04 and then down into data

datadir = r"C:\Users\tihan\OneDrive\Desktop\ATU\programming-for-data-analytics\my-work\topic_4_cleaning_data_and_regular_expressions\data\\"

filename="people-100.csv"


df= pd.read_csv(datadir+filename)

# Detect missing values
print(df.isnull().sum())

# Drop rows with missing values
#df.dropna(inplace=True)

# Fill missing values
df.fillna(value='default_value', inplace=True)

# drop duplicate rows
df.drop_duplicates(inplace=True)
df.to_csv( "temp_file.csv")