import pandas as pd


def set_pandas_options():
    # print the entire dataframe without column truncation
    pd.set_option('display.max_columns', None)

    # print the entire dataframe vertically without row truncation
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
