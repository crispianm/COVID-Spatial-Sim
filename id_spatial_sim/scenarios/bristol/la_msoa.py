#d From a LA list create a MSOA list
#d $ python3 la_msoa.py <path to la list.csv> <path output list.csv>
#d v. hacky

import pandas as pd
import sys
import os
import numpy as np

la_list = pd.read_csv(sys.argv[1])
msoaLookup_path = './data/NSPCL_AUG21_UK_LU.csv'
print('Loading msoaLookup table...')
msoaLookup = pd.read_csv(msoaLookup_path, encoding = "ISO-8859-1") #d not sure which enconding to use, but default does not work


msoa_list = {'msoa11cd':[],'msoa11nm':[]}
print('Iterating over local authorities...')
for la in la_list['LAD19NM']:
    print('...Finding MSOAs for '+str(la)+'...')
    i = msoaLookup.loc[msoaLookup['ladnm']==la]
    msoa_list['msoa11cd'].extend(list(i['msoa11cd']))
    msoa_list['msoa11nm'].extend(list(i['msoa11nm']))

print('Finished loading')

print('Creating data frame...')
msoa_df = pd.DataFrame.from_dict(msoa_list)
print('Filtering out non-unique rows...')
msoa_df = msoa_df.drop_duplicates()
print('Saving to csv...')
msoa_df.to_csv(sys.argv[2],index=False)