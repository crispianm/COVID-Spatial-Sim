# $ python3 dataMerge.py <inDir> <extension> <outPath> <existingToMerge>
from datetime import date
import os
import sys
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np


df = pd.DataFrame(columns=['date'])

for x in os.listdir(sys.argv[1]):
    if x.startswith(sys.argv[2]) and '_' in x:
        try:
            print(sys.argv[1]+x)
            df_tmp = pd.read_csv(sys.argv[1]+x)
            df = pd.merge(df,df_tmp,how='outer')
        except:
            print('Failed to merge '+sys.argv[1]+x)

print(df)
la_name =list(df['areaName'])[0]


print(type(la_name))
print(la_name)

cases_df = pd.read_csv('./ltla_2021-08-22.csv')
cases_df_la = cases_df.loc[cases_df['areaName']==la_name] #d eww, this is a very hacky way to do this
includeAge = ['00_59','60+']

df['cases'] = NaN

for t in np.unique(df['date']):
    x = cases_df_la.loc[cases_df_la['date']==t]
    x = [x.loc[x['age']==a]['cases'] for a in includeAge]
    r = np.sum(x)
    df.loc[df['date']==t,'cases'] = r # now this was a palava to get working

print('Saving to '+sys.argv[3]+' ...')
df.to_csv(sys.argv[3])