import pandas as pd 
import pandas_flavor as pf 

@pf.register_dataframe_method
def display_tables(df):

    display(df.iloc[:, :20].head(),
            df.iloc[:, 20:40].head(),
            df.iloc[:, 40:60].head(),
            df.iloc[:, 60:].head())