def data_audit (dataset):
    print(
      f"number of rows: {dataset.shape[0]}\n"
      f"number of columns: {dataset.shape[1]}\n" 
      f"columns names:\n {dataset.columns}\n" 
      f"percentage missing values by column:\n{dataset.isna().mean().sort_values(ascending=False)}\n"
      f"missing values by column count:\n{dataset.isna().sum()}\n" 
      f"dublicates:{dataset.duplicated().sum()}\n\n"
      f"distinct values\n{dataset.nunique().sort_values()}\n"
      f"describe\n{dataset.describe(include="all").T}\n"
      )
    print("info")
    dataset.info()
    print(f"the first 5 rows\n {dataset.head()}\n"
          f"end of data audit")

def rerunnable_insert(dataset,loc,column_name,value):
    if column_name in dataset.columns:
       dataset.drop(columns=[column_name],inplace=True)

    dataset.insert(loc,column_name,value)
    
         
