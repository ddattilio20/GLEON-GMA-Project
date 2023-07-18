import pandas as pd
import os
import re
import numpy as np


#print('here')
df = pd.read_csv('Final_NLA_Data.csv', encoding='ISO-8859-1')
#print('here')
a = ['La','Secchi','Nitrogen, total','Phosphorus, total','Chlorophyll a','Microcystin','Nitrogen, nitrite (NO2) + nitrate (NO3)','Nitrogen, NH4','Temperature','Carbon, dissolved organic']

newdf = df[['SITE_ID','sampledate','LAT_DD','LON_DD','lagos_variablename','datavalue']].copy()
print(round(49.13782,3))
newdf = newdf[newdf['lagos_variablename'].isin(a)]
for i in newdf.index:
    newdf['LAT_DD'][i] = round(newdf['LAT_DD'][i],4)
    newdf['LON_DD'][i] = round(newdf['LON_DD'][i],4)
    #print(type(newdf['LAT_DD'][i]))

newdf = pd.pivot_table(data = newdf, index=['SITE_ID', 'sampledate', 'LAT_DD', 'LON_DD'], columns='lagos_variablename', values='datavalue')
#newdf = newdf.groupby('SITE_ID')
#newdf1 = newdf.groupby('SITE_ID')





print(newdf)


newdf.to_csv('out.csv')