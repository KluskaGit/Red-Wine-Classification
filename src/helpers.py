import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def values_percent(ser: pd.Series) -> pd.Series:
    return (ser.value_counts()/ser.shape[0]*100).round(2)

def create_percentage_plot(
        ser: pd.Series,
        x_limit=10,
        ax=None,
        bar_label=False,
        ) -> None:
    
    percents = values_percent(ser).head(x_limit)
    bars = sns.barplot(x=percents.index, y=percents, hue=percents.index, ax=ax)
    plt.ylabel('Percentage (%)')
    if bar_label:
        for container in bars.containers:
            bars.bar_label(container=container) # type: ignore
    plt.title('Percentage of values');


def quality_based_plot(df: pd.DataFrame, column: str):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), sharey=True) 
    sns.barplot(df, x='quality', y=column, hue='quality', ax=axes[0])
    sns.barplot(df, x='quality_bin', y=column, hue='quality_bin', ax=axes[1])

    fig.suptitle(f'Quality based on {column}')
    axes[1].tick_params(labelleft=True)
    axes[1].yaxis.label.set_visible(True)
    plt.tight_layout()