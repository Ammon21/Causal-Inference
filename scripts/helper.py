import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder

def plot_outlier(df,columns,title):
    sns.set(style="whitegrid")
    data_frame = pd.melt(df, id_vars='diagnosis', value_vars=columns)
    plt.figure(figsize=(12, 6))
    res=sns.boxplot(x='variable', y='value',hue='diagnosis', data=data_frame,palette=["gold", "purple"])
    plt.title(title, size=18, fontweight='bold')
    res.set_xticklabels(res.get_xmajorticklabels(), fontsize = 15)
    res.set_yticklabels(res.get_ymajorticklabels(), fontsize = 15)
    plt.show()

def fix_outlier(df):
    column_name=list(df.columns[2:])
    for i in column_name:
        upper_quartile=df[i].quantile(0.75)
        lower_quartile=df[i].quantile(0.25)
        df[i]=np.where(df[i]>upper_quartile,df[i].median(),np.where(df[i]<lower_quartile,df[i].median(),df[i]))
    return df

def encoding_data(df):
  for column in df.columns:
    if df[column].dtype == np.int64 or df[column].dtype == np.float64:
      continue
    df[column] = LabelEncoder().fit_transform(df[column])
  
  return df    

def check_for_outliers(df: pd.DataFrame, print_out: bool = True) -> list:
    """
    A method to check for outliers. 
    TODO: try to really understand this method.

    Parameters
    ----------
    df: pandas data frame
        The data frame to check outliers from

    Returns
    -------
    outliers: python list
        A list that contains the outlier features
    """
    tmp_info = df.describe()

    Q1 = np.array(tmp_info.iloc[4,:].values.flatten().tolist())
    Q3 = np.array(tmp_info.iloc[6,:].values.flatten().tolist())

    # calculate the Inerquartile range.
    IQR = Q3-Q1
    L_factor = IQR*1.5
    H_factor = IQR*3

    # Minor Outliers will lie outside the Inner fence
    Inner_Low = Q1-L_factor
    Inner_High = Q3 + L_factor
    inner_fence = [Inner_Low, Inner_High]

    # Major Outliers will lie outside the Outer fence
    Outer_Low = Q1-H_factor
    Outer_High = Q3+H_factor
    outer_fence = [Outer_Low, Outer_High]
    
    outliers = []
    for col_index in range(df.shape[1]):
        inner_count = 0
        outer_count = 0
        tmp_list = df.iloc[:,col_index].tolist()
        for value in tmp_list:
            if((value < inner_fence[0][col_index]) or (value > inner_fence[1][col_index])):
                inner_count = inner_count + 1
            elif((value < outer_fence[0][col_index]) or (value > outer_fence[1][col_index])):
                outer_count = outer_count + 1

        outliers.append({df.columns[col_index]:[inner_count, outer_count]})
    if print_out:
        print(outliers)
    return outliers


 