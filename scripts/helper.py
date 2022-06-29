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

 