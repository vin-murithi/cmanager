import pandas as pd

# get row where column is equal to a given value
def get_row(file, column, value, sheet_name):
    # read in the file as dataframe
    df = pd.read_excel(file, sheet_name=sheet_name)
    # locate the column
    df_row = df.loc[df[column]==value]
    return df_row
