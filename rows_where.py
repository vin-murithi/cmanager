import pandas as pd
from data import county_list

file = 'voters_per_polling_station.xlsx'
county = county_list[12].upper()

#get column names
df_cols = pd.read_excel(io=file,engine='openpyxl')
df_header = list(df_cols.columns)


# Read excel file to extract rows and columns from
df_registered_voters = pd.read_excel(
    io=file,
    engine='openpyxl',
    index_col =str(df_header[1])  
)
#Index the columns I want to search

#Locate Rows and columns for given County: loc[[rows],[columns]]
count_polling_stations = df_registered_voters.loc[[county], ['CONSTITUENCY NAME','CAW_NAME','POLLING STATION NAME','VOTERS PER POLLING STATION']]

#Write the rows and columns into a data structure for search and comparison, or to excel file


print(count_polling_stations)