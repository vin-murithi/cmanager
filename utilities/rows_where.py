import pandas as pd
from data.data import county_list

#Take in file and county
file = 'voters_per_polling_station.xlsx'
county = county_list[12].upper()

# get column names
df_cols = pd.read_excel(io=file, engine='openpyxl')
df_header = list(df_cols.columns)


# Read excel file to extract rows and columns from
df_registered_voters = pd.read_excel(
    io=file,
    engine='openpyxl',
    index_col=str(df_header[1])
)
# Index the columns I want to search

# Locate Rows and columns for given County: loc[[rows],[columns]]
count_polling_stations = df_registered_voters.loc[[county], [
    'CONSTITUENCY NAME', 'CAW_NAME', 'REGISTRATION CENTRE NAME', 'VOTERS PER REGISTRATION CENTRE']]
# Remove null cells
count_polling_stations = count_polling_stations.dropna(
    subset=['REGISTRATION CENTRE NAME'], axis='rows', inplace=False)

# Write the rows and columns into an excel file
sheet = str(county)
with pd.ExcelWriter('registered_voters.xlsx', engine='openpyxl', mode='a') as writer:
    count_polling_stations.to_excel(writer, sheet_name=sheet)

print(count_polling_stations)
