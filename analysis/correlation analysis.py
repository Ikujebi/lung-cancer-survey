# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("survey lung cancer.csv")

# --- Correlation Analysis including categorical columns ---
df_encoded = df.copy()
categorical_cols = df_encoded.select_dtypes(include=['object']).columns

for col in categorical_cols:
    df_encoded[col] = pd.factorize(df_encoded[col])[0]  # Converts categories to numbers

numeric_df = df_encoded.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(12, 8))
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix (Including Categorical Variables)")
plt.show()
