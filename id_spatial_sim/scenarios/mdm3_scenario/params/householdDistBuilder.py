import pandas as pd

# Load original ons data
ogPath = '../../data/ons-hh-ages.csv'
d = pd.read_csv(ogPath)

print(sum(d['hh-size']*d['freq']))

# redist
rd = 0
rd_tmp = 0
pr = 0.5 # probability of redistribution


rdList = [[0,3,0],[1,3,0],[0,4,0],[2,3,0]]
rdPr = [1/3,1/4,1/2,1/5]
# 0,3,0)]['freq
def f(x,d):
    return d['freq'][x]

for i in range(len(rdList)):
    ls_tmp = rdList[i]
    i_tmp = d.index[(d['a0-19']==ls_tmp[0]) &( d['a20-64']==ls_tmp[1]) &( d['a65+']==ls_tmp[2])]
    rd_tmp = int(pr * rdPr[i] * f(i_tmp,d))
    d['freq'][i_tmp] -= rd_tmp
    i_tmp = d.index[(d['a0-19']==ls_tmp[0]) &( d['a20-64']==ls_tmp[1]-1) &( d['a65+']==ls_tmp[2])]
    d['freq'][i_tmp] += rd_tmp
    rd += rd_tmp
print(rd)
# split evenly between 010 and 020
ls_tmp = [0,1,0]
i_tmp = d.index[(d['a0-19']==ls_tmp[0]) &( d['a20-64']==ls_tmp[1]) &( d['a65+']==ls_tmp[2])]
rd_tmp = int((1/3)*rd) # 1/3 add to single households, and therefore 1
d['freq'][i_tmp] += rd_tmp

# split evenly between 010 and 020
ls_tmp = [0,2,0]
i_tmp = d.index[(d['a0-19']==ls_tmp[0]) &( d['a20-64']==ls_tmp[1]) &( d['a65+']==ls_tmp[2])]
print(d['freq'][i_tmp])
d['freq'][i_tmp] += rd_tmp
print(d['freq'][i_tmp])



print(sum(d['hh-size']*d['freq']))

# output to new localised area
outPath = './data/ons-hh-ages.csv'
d.to_csv(outPath,index=False)