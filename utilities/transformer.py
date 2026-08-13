from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.drop_cols_ = None

    def fit(self, X, y=None):
        X_copy = X.copy()
        X_copy.columns = X_copy.columns.str.replace(" ", "_")
        static_drop = ["Churn_Label", "Churn_Score", "CLTV", "Churn_Reason", "CustomerID", "Lat_Long", "City", "Zip_Code"]
        low_variance_cols = [col for col in X_copy.columns if X_copy[col].nunique() <= 1]
        self.drop_cols_ = list(set(static_drop + low_variance_cols))
        return self
 
    def transform(self, X):
        X = X.copy()
        X.columns = X.columns.str.replace(" ", "_")
        X = X.drop(columns=[col for col in self.drop_cols_ if col in X.columns], errors="ignore")
        
        
        # 2. Clean Numerical Fields
        numeric_cols = ["Latitude", "Longitude", "Tenure_Months", "Monthly_Charges", "Total_Charges"]
        for col in numeric_cols:
            if col in X.columns:
                X[col] = pd.to_numeric(X[col].astype(str).str.strip(), errors="coerce")

                
        # 3. Clean Categorical Fields (String cast, strip, lower, category type)
        categorical_cols = X.select_dtypes(include=["object", "string"]).columns
        for col in categorical_cols:
            X[col] = X[col].astype(str).str.strip().str.lower().astype("category")
            
        return X