import pandas as pd
import os
import re
import numpy as np


#print('here')
df = pd.read_csv('out.csv', encoding='ISO-8859-1')
#print('here')


for i in range(4,13):
    for j in df.index:
        if pd.isnull(df.iloc[j,i]) == False:
            df.iloc[j,i] = round( df.iloc[j,i],2)
    #print(type(newdf['LAT_DD'][i]))






#print(df)

print(len(df.columns))
#newdf.to_csv('out.csv')