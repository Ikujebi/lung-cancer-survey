import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
df = pd.read_csv("survey lung cancer.csv")
from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# --- Feature Importance ---
feature_importance = pd.Series(model.coef_[0], index=X.columns).sort_values(ascending=False)

# Create subplots
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
# Add accuracy text
axs[1].text(0.5, -0.3, f'Accuracy: {accuracy*100:.2f}%', ha='center', va='center', transform=axs[1].transAxes, fontsize=12, fontweight='bold')

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
