import pandas as pd
from IPython.display import display
def data_audit (dataset):
    print(
      f"number of rows: {dataset.shape[0]}\n"
      f"number of columns: {dataset.shape[1]}\n" 
      f"columns names:\n {dataset.columns}\n" 
      f"percentage missing values by column:\n{dataset.isna().mean().sort_values(ascending=False).map(lambda value: f'{value:.2%}').to_string()}\n"
      f"missing values by column count:\n{dataset.isna().sum()}\n" 
      f"dublicates:{dataset.duplicated().sum()}\n\n"
      f"distinct values\n{dataset.nunique().sort_values()}\n"
      f"describe\n{dataset.describe(include="all").T.to_string()}\n"
      )
    print("info")
    display(dataset.info())
    display("the first 5 rows",dataset.head())
          
  
         
def convert_utc_index_to_madrid (dataframe):
    return dataframe.index.tz_convert("Europe/Madrid")



