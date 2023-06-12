"""
The ExcelImporter class is used to importer data from Excel files.
It supports an Excel file with multiple sheets.
It opens each sheet and creates a dataframe for that sheet.
It stores the dataframe in a dictionary with the sheet name as the key.
It returns key value pairs of the sheet name and the dataframe.
"""

import pandas as pd


class ImportExcel:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.sheet_dataframes = {}

    def import_data(self):
        # Load the Excel file
        xls = pd.ExcelFile(self.excel_file)

        # Iterate over the sheet names in the Excel file
        for sheet_name in xls.sheet_names:
            # Create a dataframe for each sheet
            df = xls.parse(sheet_name)

            # Store the dataframe in the dictionary with the sheet name as the key
            self.sheet_dataframes[sheet_name] = df

        # Return the dictionary of dataframes
        return self.sheet_dataframes
