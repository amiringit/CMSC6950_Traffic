from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import wget

#download data
wget.download('https://opensky-network.org/datasets/covid-19/flightlist_20200201_20200229.csv.gz')
wget.download('https://opensky-network.org/datasets/covid-19/flightlist_20200301_20200331.csv.gz')
wget.download('https://opensky-network.org/datasets/covid-19/flightlist_20200401_20200430.csv.gz')
wget.download('https://opensky-network.org/datasets/covid-19/flightlist_20200501_20200531.csv.gz')

#read data as csv
data_feb = pd.read_csv('flightlist_20200201_20200229.csv.gz', compression='gzip')
data_mar = pd.read_csv('flightlist_20200301_20200331.csv.gz', compression='gzip')
data_apr = pd.read_csv('flightlist_20200401_20200430.csv.gz', compression='gzip')
data_may = pd.read_csv('flightlist_20200501_20200531.csv.gz', compression='gzip')

#append data for 4 months and make new dataframe
flightslist = pd.concat([data_feb,data_mar, data_apr, data_may])

#reread "day" column as datetime
flightslist["day"] = pd.to_datetime(flightslist["day"], utc=True)
flightslist

