"""
====================================================
AI Crop Recommendation System
Model Training Script
====================================================
"""

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# =====================================================
# Project Paths
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "Crop_recommendation.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

os.makedirs(MODEL_DIR, exist_ok=True)


# =====================================================
# Load Dataset
# =====================================================

print("\nLoading Dataset...")

df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded Successfully\n")

print(df.head())


# =====================================================
# Features & Target
# =====================================================

X = df[
    [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"
    ]
]

y = df["label"]


# =====================================================
# Encode Labels
# =====================================================

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)


# =====================================================
# Train Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)


# =====================================================
# Train Random Forest
# =====================================================

print("\nTraining Random Forest Model...\n")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    max_depth=20
)

model.fit(X_train, y_train)

print("Training Completed Successfully")


# =====================================================
# Prediction
# =====================================================

y_pred = model.predict(X_test)


# =====================================================
# Accuracy
# =====================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print(f"Accuracy : {accuracy*100:.2f}%")
print("==============================\n")


# =====================================================
# Classification Report
# =====================================================

print(classification_report(
    y_test,
    y_pred,
    target_names=label_encoder.classes_
))


# =====================================================
# Confusion Matrix
# =====================================================

print("Confusion Matrix\n")

print(confusion_matrix(
    y_test,
    y_pred
))


# =====================================================
# Save Model
# =====================================================

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "crop_model.pkl"
)

ENCODER_PATH = os.path.join(
    MODEL_DIR,
    "label_encoder.pkl"
)

joblib.dump(model, MODEL_PATH)

joblib.dump(label_encoder, ENCODER_PATH)

print("\nModel Saved Successfully")

print(MODEL_PATH)

print(ENCODER_PATH)


# =====================================================
# Feature Importance
# =====================================================

importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance\n")

print(importance)


# =====================================================
# Sample Prediction
# =====================================================

sample = [[
    90,
    42,
    43,
    27,
    82,
    6.5,
    210
]]

prediction = model.predict(sample)

crop = label_encoder.inverse_transform(prediction)

print("\nSample Prediction")

print("Recommended Crop :", crop[0])


print("\nTraining Finished Successfully")