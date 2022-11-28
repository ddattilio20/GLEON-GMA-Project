from s3References import client, MasterData, dfMasterData, MetadataDB, dfMetadataDB
from LakeIDGenerator import lakeNames, instNames
import pandas as pd
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
    'PO4 (ug/L)' : ['PO4 (ug/L)', 'orthoP','orthophosphorus', 'OP'],
    'Surface Temperature (degrees celsius)' : ['Surface Temperature (degrees celsius)', 'Temperature'],
    'LAT' : ['Lat', 'LAT', 'Latitude', 'LATITUDE'],
    'LONG' : ['LONG', 'Long', 'Longitude', 'LONGITUDE'],
    'pH' : ['pH', 'ph', 'PH'],
    'Dissolved organic carbon' : ['Dissolved organic carbon', 'Dissolved Organic Carbon']



}


def varCheck(dataframe):
    for i in range (0, len(dataframe.columns)):
        try:
            if dataframe.iat[i,6] in variable_Options.values():
                tempKey = get_key(dataframe.iat[i,6])
                dataframe.iat[i,6] = tempKey
        except Exception as e:
            print(e)
            return "One of your variables is not an acceptable variable name."
            


def get_key(val):
    for key, value in variable_Options.items():
        if val == value:
            return key