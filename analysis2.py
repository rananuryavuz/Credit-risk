import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_colwidth', 1000, 'display.max_rows', None, 'display.max_columns', None)

%matplotlib inline
mpl.style.use('ggplot')
sns.set(style='whitegrid')

df=pd.read_csv('Ir_test.csv')
df.info()

df['Acc_row_number'].value_counts(dropna=False)

df['Date_5_Amount'].describe()

df['ID']

df = df.sort_values(by=['ID', 'Date2'])
df

df.Date2 = np.where(df.Date2 == 99999999, np.nan, df.Date2)
df.Date2

df.Date2 = df.Date2.dropna().apply(lambda x: pd.to_datetime(x, format='%Y%m%d.0'))
df.Date2

df.Date_5 = pd.to_datetime(df.Date_5)
df.Date_5

df.Date_5 = df.Date_5.fillna(df.groupby('ID').Date_5.transform('max'))
df.Date_5

df.Date_5 = np.where((df.ID.shift() == df.ID) & (~df.Date_5.isna()), (df.Date_5.fillna(method='bfill')), df.Date_5)
df.Date_5
