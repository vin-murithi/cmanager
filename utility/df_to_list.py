import pandas as pd

#file
file = 'county_list.csv'

#get columns from file
def get_headers_from_file():
    #read file
    df = pd.read_csv(file)
    #get headersC
    df_header = list(df.columns)
    print(df_header)
    df = pd.read_csv(file, names=df_header)
    selected_column = input("Which column's values would you like to get?\n")
    get_column_values(selected_column,df)

#get values for selected column
def get_column_values(selected_column,df):
    #get desired column's list of values: df.value_to_list.tolist()
    values = df[selected_column].values.tolist()
    print(values)

get_headers_from_file()
