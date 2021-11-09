# python3 dataSum.py <dir> <laList> <outPath> <areaName>
import pandas as pd
import sys

laList = pd.read_csv(sys.argv[2])

df_all = pd.DataFrame()

for i,x in enumerate(laList['LAD19CD']):
    try:
        df_tmp_path = sys.argv[1]+x+'.csv'
        print(df_tmp_path)
        df_tmp = pd.read_csv(df_tmp_path)
        df_all = pd.concat([df_all,df_tmp])
    except:
        print('Failed to load a csv for '+laList['LAD19NM'][i])

print(df_all)

df_all = df_all.groupby('date').sum()
df_all['areaName'] = sys.argv[4]
df_all.to_csv(sys.argv[3])
#df_combined = pd.DataFrame(columns=df_all.columns)
