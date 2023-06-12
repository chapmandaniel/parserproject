import config.Settings as Config
from config.pandas_config import set_pandas_options
from importer.ImportExcel import ImportExcel
from importer.ImportCSV import ImportCSV
from analysis.InspectOLB import InspectOLB

settings = Config.Settings()
set_pandas_options()
file_reviews = []

if __name__ == '__main__':

    """
    Import and analyze the csv files
    """

    # scan the data directory for csv files and import them
    # return a list of dataframes
    cvs_dataframes = ImportCSV(settings.get_data_path(), settings.get_setting('delimiter')).load_csv_dataframes()

    # Iterate over the dataframes and run the tests adding the results to the file_reviews list
    for df in cvs_dataframes:
        file_reviews.append(InspectOLB(df).run_tests())

    # Print the results of the tests
    for file_review in file_reviews:
        print(file_review)
