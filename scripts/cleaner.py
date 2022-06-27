#Cleaner Scripts
import pandas as pd
import numpy as np


def percent_missing(df: pd.DataFrame):
    # Calculate total  number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    return print("The dataset contains", round(((totalMissing / totalCells) * 100), 2), "%", "missing values.")