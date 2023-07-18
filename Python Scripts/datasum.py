import pandas as pd
import os


df = pd.read_csv('Mantzouki_et_al_2018_GLEON_GMA_data.csv',encoding='ISO-8859-1')

for i in df.index:
    if pd.isnull(df['Microcystin (ug/L)'][i]):
        df['Microcystin (ug/L)'][i] = df['Microcystin YR (ug/L)'][i] + df['Microcystin dmRR (ug/L)'][i] + df['Microcystin RR (ug/L)'][i] + df['Microcystin dmLR (ug/L)'][i]
        + df['Microcystin LR (ug/L)'][i] + df['Microcystin LY (ug/L)'][i] + df['Microcystin LW (ug/L)'][i] + df['Microcystin LF (ug/L)'][i]
    print(df['Microcystin (ug/L)'][i])

df.to_csv('SummedMantz.csv')