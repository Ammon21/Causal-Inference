import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_count(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(6, 6))
    sns.countplot(data=df, x=column, facecolor=(0, 0, 0, 0), linewidth=5,  edgecolor=sns.color_palette("pastel", 3))
    plt.title(f'Distribution of {column}', size=18, fontweight='bold')
    plt.xlabel(f'{column}', fontsize=17)
    plt.ylabel("Count", fontsize=17)
    plt.show()
