import pandas as pd

# get row where column is equal to a given value
def get_row(file, sheet_name, column, value,column2=None,value2=None):
    # read in the file as dataframe
    df = pd.read_excel(file, sheet_name=sheet_name.upper())
    # locate the column
    if not column2:
        df_row = df.loc[df[column]==value]
    elif column2 and value2:
        df_row = df.loc[(df[column]==value) & (df[column2]==value2)]
    return df_row
