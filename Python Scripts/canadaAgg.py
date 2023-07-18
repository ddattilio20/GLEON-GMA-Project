import pandas as pd
import os
import numpy as np

metadata = pd.read_excel("canadaData.xlsx", sheet_name=0)
df1 = pd.read_excel("canadaData.xlsx", sheet_name=1)
df2 = pd.read_excel("canadaData.xlsx", sheet_name=2)
df3 = pd.read_excel("canadaData.xlsx", sheet_name=3)
df4 = pd.read_excel("canadaData.xlsx", sheet_name=4)
df5 = pd.read_excel("canadaData.xlsx", sheet_name=5)
df6 = pd.read_excel("canadaData.xlsx", sheet_name=6)
df7 = pd.read_excel("canadaData.xlsx", sheet_name=7)
df8 = pd.read_excel("canadaData.xlsx", sheet_name=8)
df9 = pd.read_excel("canadaData.xlsx", sheet_name=9)
df10 = pd.read_excel("canadaData.xlsx", sheet_name=10)
df11 = pd.read_excel("canadaData.xlsx", sheet_name=11)
df12 = pd.read_excel("canadaData.xlsx", sheet_name=12)
df13 = pd.read_excel("canadaData.xlsx", sheet_name=13)
df14 = pd.read_excel("canadaData.xlsx", sheet_name=14)
df15 = pd.read_excel("canadaData.xlsx", sheet_name=16)
df16 = pd.read_excel("canadaData.xlsx", sheet_name=17)
dfLakeData = pd.read_excel("canadaData.xlsx", sheet_name=19)

frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16]


maindf = pd.concat(frames)
maindf = maindf.drop(columns='COMMENT')

mcMeth = maindf.groupby(['MC_ID'])

elisa = mcMeth.get_group("ELISA")
ppia = mcMeth.get_group("PPIA")
hplc = mcMeth.get_group("HPLC")


elisaSampleMeth = elisa.groupby(['SMETHOD_ID'], dropna=False)
ppiaSampleMeth = ppia.groupby(['SMETHOD_ID'], dropna=False)
hplcSampleMeth = hplc.groupby(['SMETHOD_ID'], dropna=False)

#elisaINEUP = elisaSampleMeth.get_group("INEUP")
elisaSGRAB = elisaSampleMeth.get_group("SGRAB")
elisaSGRAB = elisaSampleMeth.get_group("surface")
#elisaDISZ = elisaSampleMeth.get_group("DISZ")
#elisaINWC = elisaSampleMeth.get_group("INWC")
elisaINEPI = elisaSampleMeth.get_group("INEPI")
elisaINEPI = elisaSampleMeth.get_group("int epi")
#elisaNaN = elisaSampleMeth.get_group()


#ppiaINEUP = ppiaSampleMeth.get_group("INEUP")
ppiaSGRAB = ppiaSampleMeth.get_group("SGRAB")
#ppiaSGRAB = ppiaSampleMeth.get_group("surface")
#ppiaDISZ = ppiaSampleMeth.get_group("DISZ")
ppiaINWC = ppiaSampleMeth.get_group("INWC")
ppiaINEPI = ppiaSampleMeth.get_group("INEPI")
#ppiaINEPI = ppiaSampleMeth.get_group("int epi")
#ppiaNaN = ppiaSampleMeth.get_group(np.NaN)

hplcINEUP = hplcSampleMeth.get_group("INEUP")
#hplcSGRAB = hplcSampleMeth.get_group("SGRAB")
#hplcSGRAB = hplcSampleMeth.get_group("surface")
hplcDISZ = hplcSampleMeth.get_group("DISZ")
#hplcINWC = hplcSampleMeth.get_group("INWC")
#hplcINEPI = hplcSampleMeth.get_group("INEPI")
#hplcINEPI = hplcSampleMeth.get_group("int epi")
##hplcNaN = hplcSampleMeth.get_group(np.NaN)


#elisa = pd.merge(elisa, dfLakeData, how='left', on='LAKE_ID')
#ppia = pd.merge(ppia, dfLakeData, how='left', on='LAKE_ID')
#hplc = pd.merge(hplc, dfLakeData, how='left', on='LAKE_ID')

#elisaINEUP.to_csv('CanadaAggregatedElisa_INEUP.csv')
elisaSGRAB = pd.merge(elisaSGRAB, dfLakeData, how='left', on='LAKE_ID')
elisaSGRAB.to_csv('CanadaAggregatedElisa_SGRAB.csv')

#elisaDISZ.to_csv('CanadaAggregatedElisa_DISZ.csv')
#elisaINWC.to_csv('CanadaAggregatedElisa_INWC.csv')
elisaINEPI = pd.merge(elisaINEPI, dfLakeData, how='left', on='LAKE_ID')
elisaINEPI.to_csv('CanadaAggregatedElisa_INEPI.csv')
#elisaNaN.to_csv('CanadaAggregatedElisa_NaN.csv')

#ppiaINEUP.to_csv('CanadaAggregatedPPIA_INEUP.csv')
ppiaSGRAB = pd.merge(ppiaSGRAB, dfLakeData, how='left', on='LAKE_ID')
ppiaSGRAB.to_csv('CanadaAggregatedPPIA_SGRAB.csv')
#ppiaDISZ.to_csv('CanadaAggregatedPPIA_DISZ.csv')
ppiaINWC = pd.merge(ppiaINWC, dfLakeData, how='left', on='LAKE_ID')
ppiaINWC.to_csv('CanadaAggregatedPPIA_INWC.csv')
ppiaINEPI = pd.merge(ppiaINEPI, dfLakeData, how='left', on='LAKE_ID')
ppiaINEPI.to_csv('CanadaAggregatedPPIA_INEPI.csv')
#ppiaNaN.to_csv('CanadaAggregatedPPIA_NaN.csv')

hplcINEUP = pd.merge(hplcINEUP, dfLakeData, how='left', on='LAKE_ID')
hplcINEUP.to_csv('CanadaAggregatedHPLC_INEUP.csv')
#hplcSGRAB.to_csv('CanadaAggregatedHPLC_SGRAB.csv')
hplcDISZ = pd.merge(hplcDISZ, dfLakeData, how='left', on='LAKE_ID')
hplcDISZ.to_csv('CanadaAggregatedHPLC_DISZ.csv')
#hplcINWC.to_csv('CanadaAggregatedHPLC_INWC.csv')
#hplcINEPI.to_csv('CanadaAggregatedHPLC_INEPI.csv')
#hplcNaN.to_csv('CanadaAggregatedHPLC_NaN.csv')

