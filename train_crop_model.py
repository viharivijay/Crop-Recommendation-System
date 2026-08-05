import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# ==========================
# Load Dataset
# ==========================

dataset_path = os.path.join("dataset", "Crop_recommendation.csv")

df = pd.read_csv(dataset_path)

print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

# Show available crops
print("\nAvailable Crops:")
print(sorted(df["label"].unique()))

# ==========================
# Features and Target
# ==========================

X = df[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]

y = df["label"]

# ==========================
# Encode Labels
# ==========================

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

# ==========================
# Train-Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded,
)

# ==========================
# Train Model
# ==========================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# Evaluate
# ==========================

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy*100:.2f}%")

# ==========================
# Save Model
# ==========================

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/crop_model.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")

print("\nNew crop_model.pkl created successfully!")
print("New label_encoder.pkl created successfully!")