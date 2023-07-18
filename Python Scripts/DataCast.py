import pandas as pd
import os


df = pd.read_csv('test.csv')


##current iteration
new_dbdf = pd.pivot_table(data = df, index=['DATETIME', 'Body of Water', 'DataContact', 'LAT', 'LONG'], columns='lagos_variablename', values='datavalue')

print(new_dbdf)
new_dbdf.to_csv('newTesting.csv')