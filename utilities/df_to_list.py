from enum import unique
import pandas as pd
from .create_sheet import get_sheet

#A function to return a list of values of a given column 
# Takes in the Excel file and the column name: returns column values as list
def get_column_values(file,sheet_name,selected_column,second_column=None,second_column_value=None):
    try:
        #read file
        df = pd.read_excel(file, sheet_name=sheet_name.upper())
        #get headers
        df_header = list(df.columns)
        df = pd.read_excel(file, sheet_name=sheet_name.upper(),names=df_header)
        #get desired column's list of values: df.value_to_list.tolist()
        if second_column==None:
            values = df[selected_column].values.tolist()
        else:
            values = df.loc[df[second_column] == second_column_value, selected_column].values.tolist()
        values = set(values)
    except ValueError:
        #create the missing sheet
        input_file = 'voters_per_polling_station.xlsx'
        output_file = 'registered_voters.xlsx'
        index_col = 'COUNTY NAME'
        index_col_value = sheet_name
        col_list =  ['CONSTITUENCY NAME', 'CAW_NAME', 'REGISTRATION CENTRE NAME', 'VOTERS PER REGISTRATION CENTRE']
        get_sheet(input_file,output_file,index_col,index_col_value,col_list)
        values = ['Reselect your option to get updated datasets']
    return values
