import pandas as pd
import matplotlib.pyplot as plt
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


def plot_residuals(actual, predictions, model_name):
    residuals = actual - predictions

    plt.figure(figsize=(12, 5))
    plt.scatter(predictions, residuals, alpha=0.3, s=10)
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Predicted price (€/MWh)")
    plt.ylabel("Residual: actual − predicted (€/MWh)")
    plt.title(f"{model_name} residuals")
    plt.show()

def plot_residuals_over_time(actual, predictions, model_name):
    residuals = actual - predictions

    plt.figure(figsize=(12, 5))
    plt.scatter(actual.index, residuals, alpha=0.3, s=10)
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Date")
    plt.ylabel("Residual: actual − predicted (€/MWh)")
    plt.title(f"{model_name} residuals over time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def actual_vs_predictions_results(actual,predictions):
    table=pd.DataFrame({
        "actual":actual,
        "predictions":predictions
    })
    
    table[["actual","predictions"]].plot(figsize=(15, 5),alpha=0.8)
    plt.ylabel("Settlement price (€/MWh)")
    plt.title("Actual versus predicted settlement prices")
    plt.grid()
    plt.show()

    return table


def display_random_forest_fine_tuning_results(search, number_of_results=None):
    
    if not hasattr(search, "cv_results_"):
        raise ValueError("search must be fitted before its results can be displayed")
    
    search_results = pd.DataFrame(search.cv_results_)
    results_table = pd.DataFrame({
        
        "Mean CV RMSE": -search_results["mean_test_rmse"],
        "Fold RMSE SD": search_results["std_test_rmse"],
        "n_estimators": search_results["param_randomforestregressor__n_estimators"],
        "max_depth": search_results["param_randomforestregressor__max_depth"],
        "min_samples_leaf": search_results["param_randomforestregressor__min_samples_leaf"],
        "max_features": search_results["param_randomforestregressor__max_features"],
    
    }).sort_values("Mean CV RMSE").reset_index(drop=True)

    if number_of_results is not None:
        results_table = results_table.head(number_of_results)

    display(results_table)
    return results_table
