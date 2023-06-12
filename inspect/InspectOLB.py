"""
InspectOLB class
- receives the imported data as a dataframe
- runs tests defined in self.tests
- returns a prettytable object that contains the results
"""

from datetime import datetime
from prettytable import PrettyTable
import config.Settings as Settings

settings = Settings.Settings()


class InspectOLB:
    def __init__(self, df):
        self.df = df
        self.start_date = settings.get_start_date()
        self.end_date = settings.get_end_date()

        self.tests = {
            'FATAL: Date out of Range': self.check_date,
            'FATAL: Missing Customer ID': self.check_olb_id,
            'FATAL: Missing Target ID': self.check_core_customer_id
        }

    def check_date(self):
        begin = datetime.strptime(self.start_date, '%Y-%m-%d')
        end = datetime.strptime(self.end_date, '%Y-%m-%d')
        invalid_date_rows = self.df[(self.df['Date/Time'] < end) & (self.df['Date/Time'] > begin)]
        return len(invalid_date_rows)

    def check_olb_id(self):
        empty_olb_user_id_rows = self.df[self.df['OLB User ID'].isnull() | (self.df['OLB User ID'] == '')]
        return len(empty_olb_user_id_rows)

    def check_core_customer_id(self):
        empty_core_customer_id_rows = self.df[
            self.df['Core Customer ID'].isnull() | (self.df['Core Customer ID'] == '')]
        return len(empty_core_customer_id_rows)

    def run_tests(self):
        table = PrettyTable()
        table.clear_rows()
        table.field_names = ["Test", "Number of Issues Found"]
        for test_name, test_func in self.tests.items():
            issues_found = test_func()
            table.add_row([test_name, issues_found])
        return table
