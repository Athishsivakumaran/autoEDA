import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

def run_multivariate_analysis(df):
    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(exclude='number').columns

    # Grouped Box Plot (First 2 cats and 1 num)
    if len(categorical_cols) >= 2 and len(numeric_cols) >= 1:
        sns.boxplot(data=df, x=categorical_cols[0], y=numeric_cols[0], hue=categorical_cols[1])
        plt.title('Grouped Box Plot')
        plt.savefig('grouped_box_plot.png')
        plt.clf()

    # Facet Grid
    if len(categorical_cols) >= 2 and len(numeric_cols) >= 2:
        g = sns.FacetGrid(df, col=categorical_cols[0], row=categorical_cols[1])
        g.map_dataframe(sns.scatterplot, x=numeric_cols[0], y=numeric_cols[1])
        plt.savefig('facet_scatter.png')
        plt.clf()

    # 3D Scatter
    if len(numeric_cols) >= 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(df[numeric_cols[0]], df[numeric_cols[1]], df[numeric_cols[2]])
        ax.set_xlabel(numeric_cols[0])
        ax.set_ylabel(numeric_cols[1])
        ax.set_zlabel(numeric_cols[2])
        plt.title('3D Scatter Plot')
        plt.savefig('3d_scatter.png')
        plt.clf()

    # PCA
    # Standardize numeric columns
        scaler = StandardScaler()
        scaled = scaler.fit_transform(df[numeric_cols])

        # PCA with 2 components
        pca = PCA(n_components=2)
        pcs = pca.fit_transform(scaled)

        # DataFrame for PCA result
        pca_df = pd.DataFrame(pcs, columns=['PC1', 'PC2'])

        # Plot PCA scatter
        plt.figure(figsize=(10, 7))
        sns.scatterplot(data=pca_df, x='PC1', y='PC2', s=50)

        # Plot loadings (feature contributions)
        loadings = pca.components_.T  # shape: (num_features, 2)
        for i, feature in enumerate(numeric_cols):
            plt.arrow(0, 0,
                    loadings[i, 0] * 3,  # multiply to make arrows more visible
                    loadings[i, 1] * 3,
                    color='red', alpha=0.7, head_width=0.1)
            plt.text(loadings[i, 0] * 3.2,
                    loadings[i, 1] * 3.2,
                    feature,
                    color='red', ha='center', va='center', fontsize=9)

        plt.title('PCA Projection with Feature Loadings')
        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.grid(True)
        plt.axhline(0, color='gray', linestyle='--', linewidth=1)
        plt.axvline(0, color='gray', linestyle='--', linewidth=1)
        plt.tight_layout()
        plt.savefig('pca_projection_with_loadings.png')
        plt.clf()

    # KMeans Clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    pca_df['Cluster'] = kmeans.fit_predict(pcs)
    sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Cluster', palette='Set2')
    plt.title('KMeans Clusters on PCA')
    plt.savefig('kmeans_clusters.png')
    plt.clf()
