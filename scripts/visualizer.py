import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_count(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=column)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.xlabel(f'{column}', fontsize=17)
    plt.ylabel("Count", fontsize=17)
    plt.show()