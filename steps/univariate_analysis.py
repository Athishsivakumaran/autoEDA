import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


def run_univariate_analysis(df = pd.DataFrame()) -> None:
    """
    This function performs univariate analysis on the provided DataFrame.
    It generates plots for numerical and categorical features and saves them to a directory.
    """ 
    os.makedirs("eda_univariate_plots", exist_ok=True)

    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # ---------- ANALYSIS FOR NUMERICAL FEATURES ----------
    for col in numerical_cols:
        print(f"\n📊 Analyzing Numerical Column: {col}")
        plt.figure(figsize=(15, 5))

        # Histogram
        plt.subplot(1, 3, 1)
        sns.histplot(df[col].dropna(), kde=False, bins=30, color='skyblue')
        plt.title(f'Histogram of {col}')

        # KDE Plot
        plt.subplot(1, 3, 2)
        sns.kdeplot(df[col].dropna(), fill=True, color='green')
        plt.title(f'KDE Plot of {col}')

        # Box Plot
        plt.subplot(1, 3, 3)
        sns.boxplot(x=df[col], color='lightcoral')
        plt.title(f'Box Plot of {col}')

        plt.tight_layout()
        plt.savefig(f"eda_univariate_plots/{col}_numerical_plots.png")
        plt.close()

        # Outlier Detection (IQR Method)
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        print(f"🔍 {len(outliers)} potential outliers detected in {col} (using IQR method)")

    # ---------- ANALYSIS FOR CATEGORICAL FEATURES ----------
    for col in categorical_cols:
        print(f"\n📦 Analyzing Categorical Column: {col}")
        value_counts = df[col].value_counts(dropna=False)
        print(value_counts)

        # Bar Plot
        plt.figure(figsize=(10, 5))
        sns.countplot(y=col, data=df, order=value_counts.index, palette='viridis')
        plt.title(f'Bar Plot of {col}')
        plt.tight_layout()
        plt.savefig(f"eda_univariate_plots/{col}_bar_plot.png")
        plt.close()

        # Optional: Pie Chart (only if few categories)
        if value_counts.shape[0] <= 10:
            plt.figure(figsize=(6, 6))
            df[col].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
            plt.title(f'Pie Chart of {col}')
            plt.ylabel('')
            plt.savefig(f"eda_univariate_plots/{col}_pie_chart.png")
            plt.close()
