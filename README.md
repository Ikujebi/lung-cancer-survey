**##Lung Cancer Survey – Descriptive and Predictive Data Analysis**

**Introduction**

Lung cancer is one of the leading causes of cancer-related deaths worldwide. Early detection and identification of key risk factors can significantly improve prevention and treatment strategies.
This project uses a survey dataset to analyze patterns in demographics, lifestyle, and health indicators, and applies machine learning techniques to predict the likelihood of lung cancer among participants.

**Objective**

The primary objectives of this project are:

**1. Descriptive Analysis:** Explore the survey dataset to understand participant demographics, symptom prevalence, and lung cancer distribution.

**2. Correlation Analysis:** Identify relationships between symptoms, lifestyle factors, and lung cancer occurrence.

**3. Predictive Modeling:** Build a machine learning model (Logistic Regression) to predict lung cancer and highlight key risk factors for participants.

**4. Visualization:** Generate plots for better interpretation of findings and model performance.

**Dataset**

**File:** survey lung cancer.csv
**Source:** Kaggle
**Format:** CSV

Each record represents a survey response with demographic and health-related information.

**Key Columns:**

GENDER – Male or Female

AGE – Age of respondent

Symptom indicators (e.g., SMOKING, YELLOW_FINGERS, FATIGUE, ANXIETY)

LUNG_CANCER – Target variable (YES or NO)

**Project Structure**
**1. Descriptive Analysis**

Displays first few records, summary statistics, and missing values

Visualizes:

Age distribution

Gender breakdown

Lung cancer frequency

Gender vs lung cancer relationship

Symptom frequency

Crosstab of gender and lung cancer percentages

**2. Correlation Analysis**

Encodes categorical variables numerically

Generates a correlation heatmap including both categorical and numeric features

**3. Predictive Modeling**

Encodes gender and lung cancer columns

Scales numeric features using StandardScaler

Trains a Logistic Regression model

Evaluates model using:

Accuracy score

Confusion matrix

Classification report

ROC curve and AUC score


**Machine Learning Model**

**Algorithm Used: **Logistic Regression

**Training/Test Split:** 80% / 20%

**Evaluation Metrics:** Accuracy, Confusion Matrix, ROC-AUC

**Performance Visualization:** Feature importance, confusion matrix, and ROC curve



**Visualization Outputs**

**Age Distribution Histogram**
<img width="777" height="553" alt="Screenshot 2025-11-12 095945" src="https://github.com/user-attachments/assets/3490e95c-ee5d-4da8-a431-38a6c75331b8" />
**X-Axis (Age):**

Represents the ages of the participants in the dataset.

The range is approximately from twenty to eighty-five years.

**Y-Axis (Count):**

Represents the number of participants in each age interval (or bin).

The taller the bar, the more participants fall into that age group.

**Histogram Bars:**

Each bar shows how many participants are within a specific age range.

Example interpretation: The tallest bars appear between fifty-five and sixty-five years, meaning most participants are in that age range.

KDE Curve (Kernel Density Estimate):

The smooth curve overlaying the histogram shows the estimated probability density of the ages.

It gives an idea of the overall distribution pattern, showing where participants are concentrated without the blocky appearance of bars.

**Distribution Shape:**

The data appears slightly right-skewed:

Most participants are concentrated around fifty-five to sixty-five.

There are fewer participants at the younger and older ends (twenties and above eighty).

Right skew implies that while most participants are older adults, there are a few younger participants pulling the tail to the right.

**Insights / Interpretations:**

Age Concentration: Majority of participants are in their late fifties and early sixties.

Diversity of Ages: Participants range widely from early twenties to mid-eighties, suggesting a diverse age group.

Outliers: Very few participants under thirty or over eighty-five, indicating these are minority age groups.

Planning Implications: If this data is for a program, service, or survey, it indicates that materials or services should focus on middle-aged to older adults.



**Gender Breakdown Bar Chart**
<img width="589" height="458" alt="Screenshot 2025-11-12 095957" src="https://github.com/user-attachments/assets/a219bebe-4982-4a93-9965-4bc64ed117a2" />
**Description:**
This bar chart visualizes the gender distribution among the participants in the research.

**X-Axis **(Gender): Represents the gender of participants. M indicates male participants and F indicates female participants.

**Y-Axis** (Number of Participants): Shows the total count of participants in each gender category.

**Interpretation:**

There are approximately one hundred fifty-two male participants and one hundred forty-eight female participants.

The distribution is fairly balanced, with a slightly higher number of male participants compared to female participants.

This balance suggests that gender bias in the participant pool is minimal, which is useful for ensuring that findings or outcomes of the study are broadly representative.

**Lung Cancer Distribution**
<img width="564" height="436" alt="Screenshot 2025-11-12 100114" src="https://github.com/user-attachments/assets/0389403b-0119-4cc3-ab3d-3cc3b11d7935" />


**Symptom Frequency Chart**

**Correlation Matrix Heatmap**

**Feature Importance (Logistic Regression)
**
**Confusion Matrix Heatmap**

**ROC Curve**

**Results Summary**

Logistic Regression Accuracy: X% (replace with your actual score)

Top predictive factors: Smoking, Yellow Fingers, Fatigue, and Coughing

The model demonstrates reliable predictive performance and interpretability

**Tools and Libraries**

**Python**

**Pandas**

**Matplotlib**

**Seaborn**

**Scikit-learn**

**Project Summary**

This project analyzes a lung cancer survey dataset to explore patterns in demographics, lifestyle factors, and reported symptoms.

The workflow includes:

**1. Descriptive Analysis** – Examining participant age, gender, symptom prevalence, and lung cancer distribution.

**2. Correlation Analysis** – Identifying relationships between symptoms, lifestyle factors, and lung cancer occurrence using a correlation heatmap.

**3. Predictive Modeling **– Building a Logistic Regression model to predict lung cancer based on survey features. The model is evaluated using accuracy, confusion matrix, classification report, and ROC curve.

**4.Visualizatio**n – Generating plots for data distribution, feature importance, and model performance to aid interpretation.

The analysis highlights key risk factors and demonstrates how survey data can inform predictive insights for early lung cancer detection.

**Future Enhancements**

Integrate other models like Random Forest or Decision Tree for comparison

Implement hyperparameter tuning

Build an interactive web dashboard for predictions

**Running the Code**

**1. Clone or download** the project folder: git clone https://github.com/<your-username>/lung-cancer-survey.git
**2. Ensure the dataset** survey lung cancer.csv is in the same directory as the script or notebook.
**3. Install required packages** using pip if not already installed:  pip install pandas matplotlib seaborn scikit-learn

**Run the script **step-by-step or execute the notebook:

Each section corresponds to a part of the analysis: descriptive analysis, correlation analysis, and machine learning.

Visualizations and tables will appear inline for each analytical objective.

**Project Status**

**Complete** — The analysis, visualizations, and predictive models have been validated and are ready for reporting or presentation.

By analyzing participant demographics, lifestyle factors, symptom prevalence, and lung cancer occurrence, this project provides meaningful insights into the key risk factors and predictors of lung cancer.

The findings highlight critical characteristics associated with higher risk, which can help guide early detection strategies, preventive measures, and awareness campaigns.




**Author

Damilare Igbosanya**

**License**
This project is released for educational and portfolio purposes.

