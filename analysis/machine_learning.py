# analysis/machine_learning.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class MLAnalyzer:
    def __init__(self, data_path="survey lung cancer.csv"):
        self.data_path = data_path
        self.model = None
        self.scaler = None
        self.accuracy = None
        self.feature_names = None  # Save the feature names for prediction
        self.categorical_columns = None  # Save categorical columns
        self._train_model()

    def _train_model(self):
        """
        Trains a logistic regression model on the lung cancer dataset.
        Stores the trained model, scaler, accuracy, and feature names.
        """
        df = pd.read_csv(self.data_path)

        # Remove any leading/trailing spaces in column names
        df.columns = df.columns.str.strip()

        # Ensure the target exists
        target_col = "LUNG_CANCER"
        if target_col not in df.columns:
            raise ValueError(f"Target column '{target_col}' not found. Columns are: {df.columns.tolist()}")

        # Identify categorical columns except the target
        self.categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()
        if target_col in self.categorical_columns:
            self.categorical_columns.remove(target_col)

        # Encode categorical features without dropping any dummy
        df_encoded = pd.get_dummies(df, columns=self.categorical_columns, drop_first=False)

        # Target column is already numeric (1 = Yes, 2 = No), use directly
        y = df_encoded[target_col].map({"YES": 1, "NO": 0})
        X = df_encoded.drop(target_col, axis=1)

        # Save feature names for later
        self.feature_names = X.columns.tolist()

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale features
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Train logistic regression
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X_train_scaled, y_train)

        # Evaluate
        y_pred = self.model.predict(X_test_scaled)
        self.accuracy = accuracy_score(y_test, y_pred)

    def predict(self, **kwargs):
        """
        Predicts lung cancer based on input features.
        Automatically fills missing features with 0.
        Accepts named arguments for all features (like GENDER="M", AGE=50, SMOKING=1, etc.)
        Returns 'YES' or 'NO'.
        """
        if self.model is None or self.scaler is None:
            raise ValueError("Model has not been trained yet.")

        # Initialize all features to 0
        input_dict = {f: 0 for f in self.feature_names}

        # Handle categorical features dynamically
        for col in self.categorical_columns:
            value = kwargs.get(col)
            if value is not None:
                dummy_col = f"{col}_{value}"
                if dummy_col in input_dict:
                    input_dict[dummy_col] = 1

        # Handle numeric features
        for col in kwargs:
                if col in input_dict:
                    input_dict[col] = kwargs[col]

        # Convert to DataFrame
        df_input = pd.DataFrame([input_dict])

        # Scale input
        X_scaled = self.scaler.transform(df_input)

        # Predict
        pred = self.model.predict(X_scaled)[0]
        return "YES" if pred == 1 else "NO"
