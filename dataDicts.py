from s3References import client, MasterData, dfMasterData, MetadataDB, dfMetadataDB
from LakeIDGenerator import lakeNames, instNames

masterFile = "data/MasterData.csv"



#dicts used for matching upload variable names to accepted variable names


variable_Options = {

    'Secchi Depth (m)' : ['Secchi Depth (m)', 'Secchi'],
    'Total Nitrogen (ug/L)' : ['Total Nitrogen (ug/L)', 'Nitrogen, total'],
    'Total Phosphorus (ug/L)' : ['Total Phosphorus (ug/L)', 'Phosphorus, total'],
    'Total Chlorophyll a (ug/L)' : ['Total Chlorophyll a (ug/L)', 'Chlorophyll a'],
    'Microcystin (ug/L)' : ['Microcystin (ug/L)', 'Microcystin'],
    'NO3 NO2 (mg/L)' : ['NO3 NO2 (mg/L)', 'Nitrogen, nitrite (NO2) + nitrate (NO3)'],
    'NH4 (mg/L)' : ['NH4 (mg/L)', 'Nitrogen, NH4'],
    'PO4 (ug/L)' : ['PO4 (ug/L)', 'Phosphorus, total'],
    'Surface Temperature (degrees celsius)' : ['Surface Temperature (degrees celsius)', 'Temperature']


}