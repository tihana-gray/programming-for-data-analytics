import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np


# load the dataset
dataset = sns.load_dataset('tips') 

# print(dataset.head())

# for debugging
#print(dataset.head()) 

sns.set_style('whitegrid') 
# sns.lmplot(x='total_bill', y='tip', order=1, data=dataset)
# sns.lmplot(x='total_bill', y='tip', hue='smoker', data=dataset)
# sns.lmplot(x="size", y="tip", data=dataset)
# sns.lmplot(x="size", y="tip", data=dataset, x_jitter=.05)
sns.lmplot(x="size", y="tip", data=dataset, x_estimator=np.mean)

plt.show()

