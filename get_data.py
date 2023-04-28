# Installed Pandas and openpyxl
import pandas

def get_dict_data(filename, sheet_name):
    file = "/Users/kkrueger/desktop/Asymmetry/data/"+ filename
    excel_data_df = pandas.read_excel(file, sheet_name= sheet_name, dtype='str').fillna('')
    return excel_data_df.to_dict(orient='records')

# check