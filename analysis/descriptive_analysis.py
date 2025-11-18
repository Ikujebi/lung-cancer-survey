# analysis/descriptive.py

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend to avoid warnings
import matplotlib.pyplot as plt
import seaborn as sns
import os

class DescriptiveAnalyzer:
    def __init__(self, data_path="survey lung cancer.csv", output_dir="static/images"):
        self.data_path = data_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.df = pd.read_csv(self.data_path)

    def run_descriptive(self):
        df = self.df
        desc_stats = df.describe().to_dict()
        plots = {}

        def save_plot(fig_name):
            """Helper to save plot to static/images and return relative path."""
            rel_path = f"images/{fig_name}"        # relative to 'static'
            full_path = os.path.join("static", rel_path)  # actual save path
            plt.savefig(full_path, bbox_inches='tight')
            plt.close()
            return rel_path

        # --- Age Distribution ---
        plt.figure(figsize=(8,5))
        sns.histplot(df["AGE"], kde=True, bins=20, color="skyblue")
        plt.title("Age Distribution of Participants")
        plt.xlabel("Age")
        plt.ylabel("Count")
        plots['age'] = save_plot("age_distribution.png")

        # --- Gender Breakdown ---
        plt.figure(figsize=(6,4))
        gender_counts = df["GENDER"].value_counts()
        sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="pastel")
        plt.title("Gender Breakdown")
        plt.xlabel("Gender")
        plt.ylabel("Number of Participants")
        plots['gender'] = save_plot("gender_breakdown.png")

        # --- Lung Cancer Distribution ---
        plt.figure(figsize=(6,4))
        cancer_counts = df["LUNG_CANCER"].value_counts()
        sns.barplot(x=cancer_counts.index, y=cancer_counts.values, palette="muted")
        plt.title("Lung Cancer Distribution")
        plt.xlabel("Lung Cancer Status")
        plt.ylabel("Count")
        plots['lung_cancer'] = save_plot("lung_cancer_distribution.png")

        # --- Gender vs Lung Cancer ---
        plt.figure(figsize=(6,4))
        sns.countplot(x="GENDER", hue="LUNG_CANCER", data=df, palette="cool")
        plt.title("Lung Cancer Occurrence by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Count")
        plots['gender_vs_lung'] = save_plot("gender_vs_lung.png")

        # --- Symptom Frequency ---
        symptom_columns = df.columns[2:-1]  # excluding GENDER, AGE, LUNG_CANCER
        symptom_sums = df[symptom_columns].apply(lambda x: (x==2).sum())
        plt.figure(figsize=(10,6))
        sns.barplot(x=symptom_sums.index, y=symptom_sums.values, palette="viridis")
        plt.xticks(rotation=90)
        plt.title("Frequency of Reported Symptoms")
        plt.xlabel("Symptom")
        plt.ylabel("Count of 'Yes' Responses")
        plots['symptoms'] = save_plot("symptom_frequency.png")

        # --- Lung Cancer Counts & Percentages ---
        lung_counts = df["LUNG_CANCER"].value_counts()
        lung_pct = (lung_counts / lung_counts.sum() * 100).round(2)
        plt.figure(figsize=(6,5))
        sns.barplot(x=lung_counts.index, y=lung_counts.values, palette="pastel")
        for i, (count, pct) in enumerate(zip(lung_counts.values, lung_pct.values)):
            plt.text(i, count + 1, f"{count} ({pct}%)", ha='center', va='bottom', fontweight='bold')
        plt.title("Lung Cancer Participants: Count and Percentage")
        plt.xlabel("Lung Cancer Status")
        plt.ylabel("Number of Participants")
        plt.ylim(0, lung_counts.max()*1.15)
        plots['lung_pct'] = save_plot("lung_cancer_pct.png")

        # --- Gender x Lung Cancer Crosstab ---
        gender_cancer_table = pd.crosstab(df["GENDER"], df["LUNG_CANCER"], normalize="index") * 100
        gender_cancer_melted = gender_cancer_table.reset_index().melt(
            id_vars="GENDER", var_name="LUNG_CANCER", value_name="Percentage"
        )
        plt.figure(figsize=(6,4))
        sns.barplot(x="GENDER", y="Percentage", hue="LUNG_CANCER", data=gender_cancer_melted, palette="coolwarm")
        plt.title("Lung Cancer Occurrence by Gender (%)")
        plt.ylabel("Percentage (%)")
        plt.xlabel("Gender")
        plt.ylim(0,100)
        plt.legend(title="Lung Cancer Status")
        plots['gender_lung_pct'] = save_plot("gender_lung_pct.png")

         # --- GROUPED SUMMARY ---
        groups = {
            "Lifestyle": ["SMOKING", "ALCOHOL_CONSUMING"],
            "Symptoms": ["FATIGUE", "WHEEZING", "SHORTNESS_OF_BREATH"],
            "Medical History": ["CHRONIC_DISEASE", "ALLERGY"]
        }

        def yes_percentage(series):
            """Assume 1=No, 2=Yes"""
            return round((series == 2).mean() * 100, 1)

        grouped_summary = {}
        for group_name, features in groups.items():
            grouped_summary[group_name] = {}
            for feature in features:
                percent = yes_percentage(df[feature])
                if group_name == "Lifestyle":
                    grouped_summary[group_name][feature.replace("_", " ").title()] = f"Yes {percent}%, No {100 - percent}%"
                else:
                    grouped_summary[group_name][feature.replace("_", " ").title()] = f"{percent}% experience"

        # Return all data for template
        return {
            "desc_stats": desc_stats,
            "plots": plots,
            "grouped_summary": grouped_summary
        }