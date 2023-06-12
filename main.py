import config.Settings as Config
from config.pandas_config import set_pandas_options
from importer.ImportExcel import ImportExcel
from inspect.InspectOLB import InspectOLB

settings = Config.Settings()
set_pandas_options()
file_reviews = []

if __name__ == '__main__':

    """
    Excel Importer implementation example
    """
    # importer the data from the Excel file, save the sheets as dataframes
    import_excel_sheets = ImportExcel('data/OLB.xlsx').import_data()

    # Iterate over the sheets in the Excel file and
    # run the tests adding the results to the file_reviews list
    for sheet_name, df in import_excel_sheets.items():
        file_reviews.append(InspectOLB(df).run_tests())

    # Print the results of the tests
    for file_review in file_reviews:
        print(file_review)
