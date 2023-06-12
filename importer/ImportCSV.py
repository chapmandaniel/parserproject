import os
import pandas as pd


class ImportCSV:
    def __init__(self, directory):
        self.directory = directory

    def load_csv_dataframes(self):
        csv_dataframes = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.csv'):
                csv_path = os.path.join(self.directory, filename)
                csv_dataframes.append(pd.read_csv(csv_path))
        return csv_dataframes
