# analysis/correlation.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class CorrelationAnalyzer:
    def __init__(self, data_path="survey lung cancer.csv", output_dir="static/images"):
        self.data_path = data_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.df = pd.read_csv(self.data_path)

    def run_correlation(self):
        """
        Performs correlation analysis on the dataset.
        Saves the heatmap and returns the path.
        """
        # Encode categorical columns
        df_encoded = self.df.copy()
        categorical_cols = df_encoded.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            df_encoded[col] = pd.factorize(df_encoded[col])[0]

        # Keep only numeric columns
        numeric_df = df_encoded.select_dtypes(include=['int64', 'float64'])

        # Create correlation matrix
        correlation_matrix = numeric_df.corr()

        # Plot the heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Matrix (Including Categorical Variables)")

        # Save the figure
        output_path = os.path.join(self.output_dir, "correlation_heatmap.png")
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()

        return "images/correlation_heatmap.png"
