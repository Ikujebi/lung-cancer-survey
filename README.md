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

 **Explanation of the Chart Components**
Component,Description
Y-axis,Count - Represents the absolute number of individuals (frequency). The scale ranges from 0 to over 250.
X-axis,"Lung Cancer Status - Represents the categorical variable, which has two possible values: YES (diagnosed with lung cancer) and NO (not diagnosed with lung cancer)."
Bars,Two vertical bars represent the count for each category.
Blue Bar,Corresponds to the YES status (Individuals with Lung Cancer).
Orange Bar,Corresponds to the NO status (Individuals without Lung Cancer).

**Interpretation and Key Findings**
**High Prevalence of Lung Cancer: ** The most striking observation is the significant imbalance between the two categories.The "YES" bar (Lung Cancer Positive) is visibly much taller, with a Count of approximately 270.The "NO" bar (Lung Cancer Negative) is very short, with a Count of approximately 40.
**Dataset Imbalance: ** This chart clearly indicates a highly imbalanced dataset. The number of individuals with lung cancer substantially outweighs those without it.
**Specific Counts:Count** (YES):270
Count (NO):40
Total Sample Size:270 + 40 = 310

**Percentage Representation** :
<img width="564" height="490" alt="Screenshot 2025-11-12 100657" src="https://github.com/user-attachments/assets/22593f6c-abbb-4d84-8498-c7212d91d747" />

Percentage of YES:87.38%
Percentage of NO:12.62%
This shows that the dataset contains about 87% positive cases and 13% negative cases.

**percentage by gender representation**
Interpretation and Key Findings
High Cancer Occurrence in Both Genders:

For Females (F), the "YES" segment (light red) is dominant, indicating that a large percentage of females in the sample have lung cancer. The "NO" segment (light blue) is very small.

For Males (M), the pattern is nearly identical: the "YES" segment is dominant, and the "NO" segment is small.

Quantifying the Proportions (Approximate):Female (F):YES (Light Red): approx 85% NO (Light Blue):15%
Conclusion: Approximately 85% of the female participants in the sample have lung cancer.

Male (M):YES (Light Red):85% (Light Blue):10% Conclusion: Approximately 85% to 90% of the male participants in the sample have lung cancer.

**Gender as a Poor Differentiator (Minimal Association):
**
The most important finding is that the proportional distribution of lung cancer status is very similar between females and males.

There appears to be no significant difference in the rate of lung cancer occurrence (as a percentage of the total for each gender) between F and M.

Insight: Based on this chart, Gender alone is likely not a strong predictor of lung cancer status, as the outcome is highly positive for both groups.


**Symptom Frequency Chart** <img width="1919" height="1026" alt="Screenshot 2025-11-12 100235" src="https://github.com/user-attachments/assets/bb6d070a-c7ca-4623-8edc-6e82d96d0b62" />

**Component,Description**
**Title,Frequency of Reported Symptoms** - Clearly indicates the focus is on how often symptoms/factors were present.
**Y-axis,**Count of 'Yes' Responses - Represents the absolute number of people who confirmed having that symptom/factor. The scale goes up to over 200.
**X-axis**,"Symptoms/Factors - Lists the features being analyzed:** SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH,** **SWALLOWING_DIFFICULTY, and CHEST_PAIN."**
Bars,"Each bar represents the total count of ""YES"" responses for the corresponding symptom/factor, color-coded using a gradient (from dark purple to bright lime green)."

This image is a stacked bar chart titled **"Lung Cancer Occurrence by Gender (%)"**. It visualizes the distribution of Lung Cancer Status (YES/NO) within each gender group (F for Female, M for Male), expressed as a percentage of that gender's total count.

Here is a detailed explanation and interpretation suitable for a README and a presentation:

***

##  Lung Cancer Occurrence by Gender (%)

This stacked bar chart, also labeled **"Figure 1"**, examines the relationship between the categorical variable **Gender** and the target variable **Lung Cancer Status**.

###  Explanation of the Chart Components

| Component | Description |
| :--- | :--- |
| **Title** | **Lung Cancer Occurrence by Gender (%)** - Indicates the visualization shows the proportion of cancer cases within each gender group. |
| **Y-axis** | **Percentage (%)** - Represents the proportion of individuals within each gender category (F or M). The total height of each bar is 100%. |
| **X-axis** | **Gender** - The categorical variable being analyzed, with values **F** (Female) and **M** (Male). |
| **Legend** | **Lung Cancer Status** - Identifies the colors used for the two classes: |
| **Light Blue** | **NO** (Individuals without Lung Cancer). |
| **Light Red/Orange** | **YES** (Individuals with Lung Cancer). |
| **Stacked Bars** | Two bars (one for F, one for M) where the segments sum up to 100%. |

###  Interpretation and Key Findings

1.  **High Cancer Occurrence in Both Genders:**
    * For **Females (F)**, the "YES" segment (light red) is dominant, indicating that a large percentage of females in the sample have lung cancer. The "NO" segment (light blue) is very small.
    * For **Males (M)**, the pattern is nearly identical: the "YES" segment is dominant, and the "NO" segment is small.

2.  **Quantifying the Proportions (Approximate):**

    * **Female (F):**
        * **YES** (Light Red): $\approx 85\%$
        * **NO** (Light Blue): $\approx 15\%$
        * *Conclusion: Approximately 85% of the female participants in the sample have lung cancer.*

    * **Male (M):**
        * **YES** (Light Red): $\approx 85\%$
        * **NO** (Light Blue): $\approx 10\%$
        * *Conclusion: Approximately 85% to 90% of the male participants in the sample have lung cancer.*

3.  **Gender as a Poor Differentiator (Minimal Association):**
    * The most important finding is that the proportional distribution of lung cancer status is **very similar** between females and males.
    * There appears to be **no significant difference** in the *rate* of lung cancer occurrence (as a percentage of the total for each gender) between F and M.
    * *Insight:* Based on this chart, **Gender alone is likely not a strong predictor** of lung cancer status, as the outcome is highly positive for both groups.




**Correlation Matrix Heatmap**  <img width="1842" height="968" alt="Screenshot 2025-11-12 101602" src="https://github.com/user-attachments/assets/7e6aa72e-61a0-4a44-aebe-ba2e5f8b6c2b" />

**Feature Correlation Matrix Heatmap**
This heatmap visualizes the linear relationship (correlation) between every feature in the dataset. Correlation coefficients range from -1.00 (perfect negative correlation, shown in dark blue) to +1.00 (perfect positive correlation, shown in dark red). 0.00 (no linear correlation) is represented by white/light colors.

Component,Description
**Title**:"Correlation Matrix (Including Categorical Variables) - Indicates the chart shows correlations for all variables, including those converted from categorical to numerical (like Gender and the binary symptoms)."
A**xes:** Both the X and Y axes list all 15 features (14 predictors + 1 target variable).
**Diagonal:** Always shows 1.00 (dark red) because a variable is perfectly correlated with itself.
**Color Bar:** The legend on the right indicates the strength and direction of the correlation based on color.

This image is a **Correlation Matrix Heatmap** titled **"Correlation Matrix (Including Categorical Variables)"**. It displays the Pearson correlation coefficients ($r$) between all pairs of features, including the symptoms, risk factors, demographic features (GENDER, AGE), and the target variable (LUNG\_CANCER).

Here is a detailed explanation and interpretation suitable for a README and a presentation:

***

##  Feature Correlation Matrix Heatmap

This heatmap visualizes the linear relationship (correlation) between every feature in the dataset. Correlation coefficients range from **-1.00** (perfect negative correlation, shown in dark blue) to **+1.00** (perfect positive correlation, shown in dark red). **0.00** (no linear correlation) is represented by white/light colors.

###  Explanation of the Chart Components

| Component | Description |
| :--- | :--- |
| **Title** | **Correlation Matrix (Including Categorical Variables)** - Indicates the chart shows correlations for all variables, including those converted from categorical to numerical (like Gender and the binary symptoms). |
| **Axes** | Both the X and Y axes list all 15 features (14 predictors + 1 target variable). |
| **Diagonal** | Always shows **1.00** (dark red) because a variable is perfectly correlated with itself. |
| **Color Bar** | The legend on the right indicates the strength and direction of the correlation based on color. |

###  Interpretation and Key Findings

The interpretation focuses on two key areas: the correlation between **Predictor Variables** (internal relationships) and the correlation between **Predictors and the Target Variable** (predictive power).

#### I. Correlation with the Target Variable (LUNG\_CANCER)

This row/column (the last one) is crucial as it identifies which features are best associated with a Lung Cancer diagnosis.

1.  **Strongest Positive Predictors (Red/High r):**
    * **YELLOW\_FINGERS** ($r \approx 0.37$): Moderate positive correlation.
    * **ANXIETY** ($r \approx 0.39$): Moderate positive correlation.
    * **PEER\_PRESSURE** ($r \approx 0.37$): Moderate positive correlation.
    * **CHEST\_PAIN** ($r \approx 0.36$): Moderate positive correlation.
    * *Insight:* These symptoms/factors are the **most promising individual predictors** for a positive lung cancer diagnosis in this dataset.

2.  **Weakest/Negligible Predictors (White/Light Blue/Low r):**
    * **GENDER** ($r \approx 0.07$): Very weak positive correlation. This confirms the finding from the stacked bar chart that gender is not a strong differentiator.
    * **AGE** ($r \approx 0.07$): Very weak positive correlation.
    * **COUGHING** ($r \approx 0.02$): Negligible correlation.
    * **SHORTNESS\_OF\_BREATH** ($r \approx 0.06$): Very weak positive correlation.
    * *Insight:* Features like GENDER, AGE, COUGHING, and SHORTNESS\_OF\_BREATH have **minimal linear association** with the target variable, suggesting they may have low predictive value on their own.

#### II. Internal Feature Correlations (Multicollinearity)

This refers to the correlation among the predictor variables themselves (off-diagonal values). High internal correlation (multicollinearity) can destabilize models like linear regression.

1.  **Highest Internal Correlation (Dark Red):**
    * **YELLOW\_FINGERS** and **ANXIETY** ($r \approx 0.57$): Strong positive correlation.
    * **ANXIETY** and **PEER\_PRESSURE** ($r \approx 0.57$): Strong positive correlation.
    * **SWALLOWING\_DIFFICULTY** and **CHEST\_PAIN** ($r \approx 0.49$): Moderate-to-strong positive correlation.
    * **ALCOHOL\_CONSUMING** and **COUGHING** ($r \approx 0.37$): Moderate positive correlation.
    * **WHEEZING** and **ALCOHOL\_CONSUMING** ($r \approx 0.27$): Moderate positive correlation.

2.  **Highest Negative Correlation (Dark Blue):**
    * **GENDER** and **AGE** ($r \approx -0.14$): Very weak negative correlation.

*Insight:* The strong correlations among variables like YELLOW\_FINGERS, ANXIETY, and PEER\_PRESSURE suggest that these symptoms often occur together. For model building, this multicollinearity should be noted; while they are all good individual predictors of the target, including all of them might not improve model performance significantly over using just one or two, especially in simpler models.



**Feature Importance** **(Logistic Regression)** <img width="1919" height="976" alt="Screenshot 2025-11-12 111019" src="https://github.com/user-attachments/assets/4733eaa3-7972-47af-87f5-4d6266754ecc" />

This bar chart shows the coefficients assigned to each feature by the Logistic Regression model. The coefficient's magnitude indicates the feature's importance, and its sign (positive or negative) indicates the direction of its influence on the prediction of Lung Cancer.

Feature                                    Coefficient Value,                                                                        Interpretation
**SWALLOWING_DIFFICULTY**                          ≈1.1                                                                           Highest positive influence. This feature is the strongest predictor for a positive cancer diagnosis.
**CHRONIC_DISEASE **                              ≈1.0                                                                                       Strong positive influence.
**FATIGUE **                                       ≈1.0                                                                                     Strong positive influence.
**COUGHING**                                      ≈0.9                                                                                      High positive influence.
**ALCOHOL_CONSUMING**                             ≈0.75                                                                                        Moderate positive influence.
**YELLOW_FINGERS**                               ≈0.6                                                                                          Moderate positive influence.
**... (Remaining positive)**                     0.2 to 0.6                                                                  "Symptoms like ALLERGY, SMOKING, ANXIETY, CHEST_PAIN, and WHEEZING all positively increase the likelihood of a cancer diagnosis."
**AGE**                                         ≈−0.1                                                                     "Slight negative influence. Age slightly decreases the predicted likelihood of cancer (surprisingly, or due to data specific to this sample)."
**SHORTNESS_OF_BREATH**                        ≈−0.15           "Negative influence. A negative coefficient means the presence of this symptom slightly decreases the predicted odds of cancer (counter-intuitive, suggesting complex interactions not captured by correlation)."
**GENDER_M**                                   ≈−0.2                               Strongest negative influence. Being Male (GENDER_M = 1) is associated with the largest decrease in the predicted likelihood of cancer. This aligns with the weak correlation observed earlier.

**Key Takeaway from Feature Importance:**
**SWALLOWING_DIFFICULTY, CHRONIC_DISEASE, and FATIGUE **are the most critical features driving the positive prediction of Lung Cancer. GENDER and SHORTNESS_OF_BREATH have the least impact, or even a negative impact.


**Confusion Matrix Heatmap** <img width="1919" height="976" alt="Screenshot 2025-11-12 111019" src="https://github.com/user-attachments/assets/d1704e6e-54e8-4b53-8f62-4505191a4f84" />
The Confusion Matrix evaluates the model's classification performance on the test data.

                                    ** Predicted:No Cancer**                                                                                 ** Predicted: Cancer**
**Actual:No Cancer**                     1 (True Negative)                                                                                     1 (False Positive)
**Actual:Cancer**                        1 (False Negative)                                                                                   59 (True Positive)

Metric                                                      Calculation / Value                                                                           Interpretation
**Accuracy (Overall)**                                           **96.77% **                                                                             Reported below the matrix: (1+1+1+59)(1+59)​
**Sensitivity (Recall)**                                          59+159​=0.983                                                                           The model correctly identified 98.3% of all actual cancer cases. This is excellent.
**Specificity**                                                    1+11​=0.50                                                                             The model correctly identified 50% of all actual non-cancer cases.
**False Positive Rate**                                            1+11​=0.50                                                                             The model incorrectly flagged 50% of non-cancer cases as cancer (Type I Error).

**Key Takeaway from Confusion Matrix:**
**The model is highly effective at identifying positive cancer cases (high Sensitivity),** but its performance on the minority class ("No Cancer") is poor (low Specificity). This result is characteristic of a model trained on a highly imbalanced dataset where the classification threshold is optimized towards the majority class.

    
**ROC Curve**  <img width="1919" height="976" alt="Screenshot 2025-11-12 111019" src="https://github.com/user-attachments/assets/00b36fbc-a132-479c-85e3-833386d8e91e" />

The Receiver Operating Characteristic (ROC) curve plots the **True Positive Rate (Sensitivity)** against the **False Positive Rate (1 - Specificity)** at various threshold settings.

**AUC (Area Under the Curve): 0.92**

**The Curve:** The line quickly rises towards the top-left corner, indicating high performance.

**Interpretation:** An AUC of **0.92** signifies that there is a **92% probability **that the model will rank a randomly chosen positive instance (Cancer) higher than a randomly chosen negative instance (No Cancer). This is **a very strong result** and indicates that the model has high discriminative power.


**Results Summary**

Logistic Regression Accuracy: X% (96.77%)

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

**1. Clone or download** the project folder: git clone https://github.com/Holymichael99/lung-cancer-survey.git
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

