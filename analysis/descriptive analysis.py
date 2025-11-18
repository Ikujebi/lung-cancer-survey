# Descriptive Analysis for Lung Cancer Survey Data

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
df = pd.read_csv("survey lung cancer.csv")

# --- Basic Overview ---
print("First 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# --- Check for Missing Values ---
print("\nMissing Values per Column:")
print(df.isnull().sum())

# --- Age Distribution ---
plt.figure(figsize=(8, 5))
sns.histplot(df["AGE"], kde=True, bins=20, color="skyblue")
plt.title("Age Distribution of Participants")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# --- Gender Breakdown ---
plt.figure(figsize=(6, 4))
gender_counts = df["GENDER"].value_counts()
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="pastel")
plt.title("Gender Breakdown")
plt.xlabel("Gender")
plt.ylabel("Number of Participants")
plt.show()

# --- Frequency of Lung Cancer Cases ---
plt.figure(figsize=(6, 4))
cancer_counts = df["LUNG_CANCER"].value_counts()
sns.barplot(x=cancer_counts.index, y=cancer_counts.values, palette="muted")
plt.title("Lung Cancer Distribution")
plt.xlabel("Lung Cancer Status")
plt.ylabel("Count")
plt.show()

# --- Gender vs Lung Cancer ---
plt.figure(figsize=(6, 4))
sns.countplot(x="GENDER", hue="LUNG_CANCER", data=df, palette="cool")
plt.title("Lung Cancer Occurrence by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# --- Symptom Frequency ---
symptom_columns = df.columns[2:-1]  # All columns except GENDER, AGE, and LUNG_CANCER
symptom_sums = df[symptom_columns].apply(lambda x: (x == 2).sum())  # Assuming 2 = Yes
plt.figure(figsize=(10, 6))
sns.barplot(x=symptom_sums.index, y=symptom_sums.values, palette="viridis")
plt.xticks(rotation=90)
plt.title("Frequency of Reported Symptoms")
plt.xlabel("Symptom")
plt.ylabel("Count of 'Yes' Responses")
plt.show()

# --- Percentage of Participants with Lung Cancer ---
lung_cancer_percentage = (df["LUNG_CANCER"].value_counts(normalize=True) * 100).round(2)
print("\nPercentage of Participants with Lung Cancer:")
print(lung_cancer_percentage)
# Counts and Percentages of Lung Cancer Participants
lung_cancer_counts = df["LUNG_CANCER"].value_counts()
lung_cancer_percentage = (lung_cancer_counts / lung_cancer_counts.sum() * 100).round(2)

plt.figure(figsize=(6, 5))
sns.barplot(x=lung_cancer_counts.index, y=lung_cancer_counts.values, palette="pastel")

# Add count and percentage labels on top of bars
for i, (count, pct) in enumerate(zip(lung_cancer_counts.values, lung_cancer_percentage.values)):
    plt.text(i, count + 1, f"{count} ({pct}%)", ha='center', va='bottom', fontweight='bold')

plt.title("Lung Cancer Participants: Count and Percentage")
plt.xlabel("Lung Cancer Status")
plt.ylabel("Number of Participants")
plt.ylim(0, lung_cancer_counts.max() * 1.15)  # Add space for labels
plt.show()


# --- Gender and Lung Cancer Crosstab ---
gender_cancer_table = pd.crosstab(df["GENDER"], df["LUNG_CANCER"], normalize="index") * 100
print("\nLung Cancer Occurrence by Gender (%):")
print(gender_cancer_table)

# Gender and Lung Cancer Crosstab Plot
plt.figure(figsize=(6, 4))

# Convert percentages to a DataFrame for plotting
gender_cancer_table_plot = gender_cancer_table.reset_index()

# Melt the DataFrame for Seaborn
gender_cancer_melted = gender_cancer_table_plot.melt(id_vars="GENDER", var_name="LUNG_CANCER", value_name="Percentage")

sns.barplot(x="GENDER", y="Percentage", hue="LUNG_CANCER", data=gender_cancer_melted, palette="coolwarm")

plt.title("Lung Cancer Occurrence by Gender (%)")
plt.ylabel("Percentage (%)")
plt.xlabel("Gender")
plt.ylim(0, 100)
plt.legend(title="Lung Cancer Status")
plt.show()

