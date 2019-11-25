import requests
from dateutil.parser import parse
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
def loaddata (seriesid, DataName):
    URL = "http://api.eia.gov/series/?api_key=f0aba5aabaa6bdc89d05019d0f93ecca&series_id=" + seriesid
    response = requests.get(url = URL)
    data = response.json()
    EIAData = data['series'][0]['data']
    dfEIAData = pd.DataFrame(EIAData)
    dfEIAData.columns = ['date',str(DataName)]
    dfEIAData['date'] = pd.to_datetime(dfEIAData['date'])
    dfEIAData= dfEIAData.set_index(dfEIAData['date'])
    dfEIAData = dfEIAData.drop('date', axis =1)
    return dfEIAData;
#load data
dfTotal = loaddata('NG.NW2_EPG0_SWO_R48_BCF.W',"Total")
dfEast = loaddata('NG.NW2_EPG0_SWO_R31_BCF.W',"East")
dfWest = loaddata('NG.NW2_EPG0_SWO_R35_BCF.W',"West")
dfSouth = loaddata('NG.NW2_EPG0_SWO_R33_BCF.W',"South")
dfNonsalt = loaddata('NG.NW2_EPG0_SNO_R33_BCF.W',"Nonsalt")
dfSalt = loaddata('NG.NW2_EPG0_SSO_R33_BCF.W',"Salt")
dfMountain = loaddata('NG.NW2_EPG0_SWO_R34_BCF.W',"Mountain")
dfMidwest = loaddata('NG.NW2_EPG0_SWO_R32_BCF.W',"Midwest")
# make dataframe
df = pd.concat([dfTotal, dfEast, dfWest, dfSouth, dfNonsalt, dfSalt, dfMountain, dfMidwest], axis=1)
# add year and month
df['year'] = df.index.year
df['month'] = df.index.month
df['day'] = df.index.day
years = df['year'].unique()
df['date'] = df.index
df['date_plot'] = df['date'].apply(lambda x: x.replace(year = 2018))
print (years)
print (len(years))
print (df.head())
df.info()