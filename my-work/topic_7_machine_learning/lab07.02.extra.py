import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def parse_str(x):
    return x[1:-1]

def parse_datetime(x):
    dt = datetime.strptime(x[1:-1], '%d/%b/%Y:%H:%M:%S')
    return dt


df = pd.read_csv(
    r'C:\Users\tihan\OneDrive\Desktop\ATU\programming-for-data-analytics\my-work\topic_7_machine_learning\access.log.txt',
    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
    engine='python',
    na_values='-',
    header=None,
    usecols=[0,3,4,5,6,7,8],
    names=['ip','time','request','status','size','referer','user_agent'],
    converters={
    'time': parse_datetime,
    'request': parse_str,
    'status': int,
    'size': lambda x: int(x) if x.isdigit() else 0,
    'referer': parse_str,
    'user_agent': parse_str
}
)


print(df.head())


excelFilename = 'log.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')


request = df.pop('request').str.split()

df['resource'] = request.str[1]
df['method'] = request.str[0]


df['url'] = request.str[1].str.split('?').str[0]


dfbyhour = df.resample('H', on='time').sum()

dfbyhour['hour'] = dfbyhour.index.hour
dfbyhour['date'] = dfbyhour.index.date


sns.lmplot(x="hour", y="size", order=1, data=dfbyhour, x_jitter=0.5)
plt.show()


sns.residplot(x="hour", y="size", data=dfbyhour, order=1)
plt.show()
