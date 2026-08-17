# Django XGBoost Churn Prediction API

A production-grade **RESTful API service** built with Django REST Framework (DRF) that serves an XGBoost machine learning pipeline for customer churn prediction. Designed with robust input validation, automated testing, inference auditing, and structured logging.

---

## Features

* **Dual Request Support:** Efficiently handles both single-sample objects and multi-sample batch prediction payloads.
* **Rigorous Validation:** Implements custom serializers and field-level validation to safely reject malformed or invalid data before it reaches the ML pipeline.
* **Inference Auditing & Logging:** Captures structured logs and persists a complete audit trail of incoming requests and model outputs directly into the database.
* **Comprehensive Test Suite:** Fully tested using `pytest`, covering edge cases, data types, missing fields, null values, and batch validation logic.

---

## Tech Stack

* **Python** 3.10+
* **Django** 6.0+ & **Django REST Framework**
* **XGBoost** & **Scikit-Learn**
* **Pandas** & **NumPy**
* **Pytest**

---

## Project Structure

```text
djangoXGB/
│
├── xgb/                      # Core Django app for predictions & auditing
│   ├── migrations/           # Database migration history
│   ├── __init__.py
│   ├── admin.py              # Django admin configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Inference audit log models
│   ├── serializers.py        # Input & audit log DRF serializers
│   ├── tests.py              # Comprehensive pytest suite
│   ├── urls.py               # API routing
│   └── views.py              # Prediction API endpoints & logging logic
│
├── xgbTree/                  # Main project settings & configuration
│   ├── __init__.py
│   ├── settings.py           # Includes custom LOGGING configuration
│   ├── urls.py
│   └── wsgi.py
│
├── utilities/                # Custom ML transformers & preprocessing pipelines
├── best_telco_model.joblib   # Serialized XGBoost ML model pipeline
├── Telco_customer_churn.csv  # Telco customer churn dataset
├── pytest.ini                # Pytest configuration file
├── .gitignore
├── manage.py
└── requirements.txt
