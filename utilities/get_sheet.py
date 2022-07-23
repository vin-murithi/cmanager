import pandas as pd

def get_sheet_df(file,sheet_name):
    df = pd.read_excel(file, sheet_name=sheet_name.upper())
    return df