import pandas as pd
#A function that creates a worksheet using data from another worksheet according to some constraint.
#ToD0: Consider passing row position instead of name
#creates a worksheet from another worksheet
def get_sheet(input_file,output_file,index_col,index_col_value,col_list):
    # Read excel file to extract rows and columns from
    df_registered_voters = pd.read_excel(
        io=input_file,
        engine='openpyxl',
        index_col=index_col
    )
    # Locate Rows and columns for given County: loc[[rows],[columns]]
    count_polling_stations = df_registered_voters.loc[[index_col_value.upper()], col_list]
    # Remove null cells
    count_polling_stations = count_polling_stations.dropna(
        subset=['REGISTRATION CENTRE NAME'], axis='rows', inplace=False)
    # Write the rows and columns into an excel file
    with pd.ExcelWriter(output_file, engine='openpyxl', mode='a') as writer:
        count_polling_stations.to_excel(writer, sheet_name=index_col_value.upper())
    print(count_polling_stations)


   
