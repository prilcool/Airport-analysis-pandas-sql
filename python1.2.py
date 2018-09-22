
'''
Using a SQL database with Python and Pandas
SQL database allows you to run queries on large datasets more efficiently
than if the data were to be stored in a csv format

data source: http://ourairports.com/data/
~!~!~!~! Containing information on all airports on the website

~!~!~~! Containing information on listing communication frequencies
'''

import pandas as pd
data = pd.read_csv("airports.csv")
data_freq = pd.read_csv("airport-frequencies.csv")
runway_data = pd.read_csv("runways.csv")

data.head(3)
data[data.ident == 'KLAX'].id
data.describe()
data.type.unique()

# Select with multiple conditions equivalent

data[(data.iso_region == 'US-CA')
         & (data.type == 'seaplane_base')]

data[(data.iso_region == 'US-CA') &
         (data.type == 'large_airport')][['ident', 'name', 'municipality']]


#ORDER BY ~ by default Pandas will sort in ascending order

data_freq[data_freq.airport_ident == 'KLAX'].\
    sort_values('id', ascending=False)
