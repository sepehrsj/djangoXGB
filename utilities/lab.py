from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import pandas as pd
import xgboost as xgb
import joblib
from utilities.transformer import CustomTransformer


if __name__ == "__main__":
    df = pd.read_csv("Telco_customer_churn.csv")
    df.columns = df.columns.str.replace(" ", "_")
    
    X = df.drop(columns=["Churn_Value"])
    y = df["Churn_Value"].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    # Compute imbalanced class weight ratio (~2.72)
    scale_pos_weight = (len(y_train) - y_train.sum()) / y_train.sum()

    # 6. Define model & grid
    model = xgb.XGBClassifier(
        enable_categorical=True,
        objective="binary:logistic",
        seed=42,
        scale_pos_weight=scale_pos_weight,
        eval_metric="aucpr",
        tree_method="hist", 
    )

    pipeline = Pipeline(steps=[
        ("preprocessor", CustomTransformer()),
        ("xgbClassfier", model)
    ])

    # FIXED: Added the "xgbClassfier__" prefix to all parameters for GridSearchCV
    params = {
        "xgbClassfier__learning_rate": [0.1, 0.05, 0.01],
        "xgbClassfier__n_estimators": [100, 200],
        "xgbClassfier__max_depth": [3, 5, 7],
        "xgbClassfier__subsample": [0.7, 0.9],
        "xgbClassfier__colsample_bytree": [0.8, 0.9],
        "xgbClassfier__reg_alpha": [0.1, 1.0, 5.0]
    }

    clf = GridSearchCV(
        pipeline, params, cv=5, scoring="average_precision", n_jobs=-1
    )
    clf.fit(X_train, y_train)
    
    print("Best Parameters:", clf.best_params_)
    print("Best PR AUC Score:", clf.best_score_)
    
    best_model = clf.best_estimator_
    joblib.dump({
        "model": best_model,
        "dtypes": X_train.dtypes
    }, "best_telco_model.joblib")
