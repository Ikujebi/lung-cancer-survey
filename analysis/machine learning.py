# --- Import Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc

# --- Load the Dataset ---
df = pd.read_csv("survey lung cancer.csv")

# --- Encode Categorical Variables (e.g., GENDER) ---
df_encoded = pd.get_dummies(df, columns=["GENDER"], drop_first=True)

# --- Define Features and Target ---
X = df_encoded.drop("LUNG_CANCER", axis=1)

# Convert LUNG_CANCER column to numeric (NO = 0, YES = 1)
y = df_encoded["LUNG_CANCER"].map({"NO": 0, "YES": 1})


# --- Split into Train and Test Sets ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Scale Features ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- Train Logistic Regression Model ---
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# --- Predict on Test Set ---
y_pred = model.predict(X_test_scaled)

# --- Evaluate Model ---
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("\nLogistic Regression Accuracy:", round(accuracy * 100, 2), "%")
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", report)

# --- Feature Importance ---
feature_importance = pd.Series(model.coef_[0], index=X.columns).sort_values(ascending=False)

# --- Create Subplots ---
fig, axs = plt.subplots(1, 3, figsize=(22, 6))

# 1. Feature Importance
sns.barplot(x=feature_importance.values, y=feature_importance.index, palette="viridis", ax=axs[0])
axs[0].set_title("Feature Importance (Logistic Regression)")
axs[0].set_xlabel("Coefficient Value")
axs[0].set_ylabel("Feature")

# 2. Confusion Matrix
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["No Cancer", "Cancer"],
            yticklabels=["No Cancer", "Cancer"], ax=axs[1])
axs[1].set_title("Confusion Matrix")
axs[1].set_xlabel("Predicted")
axs[1].set_ylabel("Actual")

# Add Accuracy Text Below the Matrix
axs[1].text(0.5, -0.3, f'Accuracy: {accuracy*100:.2f}%', ha='center', va='center',
            transform=axs[1].transAxes, fontsize=12, fontweight='bold')

# 3. ROC Curve
y_prob = model.predict_proba(X_test_scaled)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
axs[2].plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
axs[2].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
axs[2].set_title("ROC Curve")
axs[2].set_xlabel("False Positive Rate")
axs[2].set_ylabel("True Positive Rate")
axs[2].legend(loc="lower right")

plt.tight_layout()
plt.show()