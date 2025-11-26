import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19) 
print(df.head(3))

# No correlation. Linear correlation can't be used to measure non-linear correlation.

cleandf = df[["month", "wdsp"]]

cleandf['wdsp'] = cleandf.loc[:, ('wdsp')].replace(' ', np.nan)
cleandf.dropna(inplace=True)

cleandf['wdsp'] = cleandf['wdsp'].astype(float)

sns.set_style('whitegrid') 
#sns.scatterplot(x='total_bill',y='tip',data=dataset) 
sns.lmplot(x='month', y='wdsp', order=3, data=cleandf) 
plt.show()