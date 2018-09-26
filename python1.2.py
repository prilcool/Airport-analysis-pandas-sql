
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

#https://codeburst.io/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e

'''IN and NOT IN filter options '''

data[data.type.isin(['heliport', 'balloonport'])]
data[~data.type.isin(['heliport', 'balloonport'])]


'''
GROUP BY, ORDER BY, COUNT
.count() will return number of non-null and NaN values 

To get same result as SQL count, use. size()  
'''

data.groupby(['iso_country', 'type']).size()

data.groupby(['iso_country', 'type'])\
    .size().to_frame('size')\
    .reset_index().sort_values(['iso_country', 'size']
                               , ascending=[True, False])

'''
HAVING clause 
In pandas, can use .filter() function and provide a Python function
that will return True if group should be included into the result  
'''

data[data.iso_country == 'US']\
    .groupby('type').filter(lambda g: len(g) > 100)\
    .groupby('type').size().sort_values(ascending=False)

'''
Top N records 
'''
data.head(3)

# Order things by airport count and select only top 10 countries

data.nlargest(10, columns = 'elevation_ft')
data.nlargest(20, columns = 'elevation_ft').tail(10)

'''
Aggregate functions 
(Minimum, Maximum and Mean estimates) 
'''
runway_data.agg({'length_ft': ['min', 'max', 'mean', 'median']}).T

'''
JOIN - Using merge() to join pandas dataframes. 
'''

data_freq.merge(data[data.ident=='KLAX'][['id']],
                left_on='airport_ref',
                right_on = 'id',
                how = 'inner')[['airport_ident', 'type',
                                'description', 'frequency_mhz']]
'''
UNION ALL & UNION 
'''

pd.concat([data[data.ident == 'KLAX']
           [['name', 'municipality']], data[data.ident == 'KLGB'][['name', 'municipality']]])

'''
INSERT statements 

'''