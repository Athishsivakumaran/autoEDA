import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

def run_bivariate_analysis(df):
    """
    Perform bivariate analysis on the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the dataset.
    
    Returns:
    None
    """
    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(exclude='number').columns

    # Scatter Plots
    for i in range(len(numeric_cols)):
        for j in range(i+1, len(numeric_cols)):
            sns.scatterplot(data=df, x=numeric_cols[i], y=numeric_cols[j])
            plt.title(f'Scatter: {numeric_cols[i]} vs {numeric_cols[j]}')
            plt.savefig(f'scatter_{numeric_cols[i]}_{numeric_cols[j]}.png')
            plt.clf()

    # Correlation Heatmap
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('correlation_heatmap.png')
    plt.clf()

    # Box & Violin Plots
    for num in numeric_cols:
        for cat in categorical_cols:
            sns.boxplot(data=df, x=cat, y=num)
            plt.title(f'Box: {num} by {cat}')
            plt.xticks(rotation=45)
            plt.savefig(f'box_{num}_by_{cat}.png')
            plt.clf()

            sns.violinplot(data=df, x=cat, y=num)
            plt.title(f'Violin: {num} by {cat}')
            plt.xticks(rotation=45)
            plt.savefig(f'violin_{num}_by_{cat}.png')
            plt.clf()

    # Categorical vs Categorical
    for i in range(len(categorical_cols)):
        for j in range(i+1, len(categorical_cols)):
            cross = pd.crosstab(df[categorical_cols[i]], df[categorical_cols[j]])
            cross.plot(kind='bar', stacked=False)
            plt.title(f'Grouped Bar: {categorical_cols[i]} vs {categorical_cols[j]}')
            plt.savefig(f'groupedbar_{categorical_cols[i]}_{categorical_cols[j]}.png')
            plt.clf()

            mosaic(df, [categorical_cols[i], categorical_cols[j]])
            plt.title(f'Mosaic: {categorical_cols[i]} vs {categorical_cols[j]}')
            plt.savefig(f'mosaic_{categorical_cols[i]}_{categorical_cols[j]}.png')
            plt.clf()