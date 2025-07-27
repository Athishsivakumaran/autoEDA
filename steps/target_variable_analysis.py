import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_target_variable_analysis(df, target_col):
    # Drop rows where target is missing
    df = df[df[target_col].notna()]
    
    # Detect target type
    is_categorical = df[target_col].dtype == 'object' or df[target_col].nunique() < 10

    if is_categorical:
        print("🔍 Target is CATEGORICAL\n")
        
        # Class distribution
        class_counts = df[target_col].value_counts()
        print("Class Distribution:\n", class_counts)

        # Class distribution plot
        plt.figure(figsize=(6, 4))
        sns.countplot(x=target_col, data=df)
        plt.title("Class Distribution")
        plt.savefig('target_class_distribution.png')
        plt.clf()

        # Boxplots for numeric features
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        for col in numeric_cols:
            if col == target_col: continue
            if df[col].isna().all(): continue  # skip if feature is entirely missing
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=target_col, y=col, data=df)
            plt.title(f"{col} vs {target_col}")
            plt.savefig(f'box_{col}_vs_target.png')
            plt.clf()

    else:
        print("🔍 Target is NUMERICAL\n")

        # Target distribution
        plt.figure(figsize=(6, 4))
        sns.histplot(df[target_col].dropna(), kde=True, bins=30)
        plt.title("Distribution of Target")
        plt.savefig('target_distribution.png')
        plt.clf()

        # Numeric features
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if target_col in numeric_cols:
            numeric_cols.remove(target_col)

        # Drop rows with missing values in numeric columns for correlation
        corr_df = df[numeric_cols + [target_col]].dropna()
        correlations = corr_df.corr()[target_col].drop(target_col)
        print("Correlation with Target:\n", correlations.sort_values(ascending=False))

        # Correlation heatmap
        plt.figure(figsize=(8, 4))
        sns.heatmap(correlations.to_frame(), annot=True, cmap='coolwarm')
        plt.title("Feature-Target Correlation")
        plt.savefig('target_correlation_heatmap.png')
        plt.clf()

        # Scatter plots
        for col in numeric_cols:
            if df[col].isna().all(): continue
            plt.figure(figsize=(6, 4))
            sns.scatterplot(x=col, y=target_col, data=df)
            plt.title(f"{col} vs {target_col}")
            plt.savefig(f'scatter_{col}_vs_target.png')
            plt.clf()
