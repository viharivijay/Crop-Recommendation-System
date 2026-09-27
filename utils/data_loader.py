import os
import pandas as pd

# ==========================
# Project Paths
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")


# ==========================
# Helper Function
# ==========================

def load_csv(filename):
    """
    Load a CSV file from the dataset folder.
    Raises an error if the file is missing.
    """
    path = os.path.join(DATASET_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {filename}")

    return pd.read_csv(path)


# ==========================
# Load All Datasets
# ==========================

try:

    crop_dataset = load_csv("Crop_recommendation.csv")

    crop_requirements = load_csv("crop_requirements.csv")

    crop_information = load_csv("crop_information.csv")

    crop_advisory = load_csv("crop_advisory.csv")

    crop_disease = load_csv("crop_disease_risk.csv")

    district_master = load_csv("district_master.csv")

    government_schemes = load_csv("government_schemes.csv")

    market_history = load_csv("market_history.csv")

    seasonal_calendar = load_csv("seasonal_calendar.csv")

    soil_profile = load_csv("soil_profile.csv")

    print("✅ All datasets loaded successfully.")

except Exception as e:
    print(f"\n❌ Error loading datasets:\n{e}")
    raise


# ==========================
# Function to return all data
# ==========================

def load_all_data():

    return {
        "crop_dataset": crop_dataset,
        "crop_requirements": crop_requirements,
        "crop_information": crop_information,
        "crop_advisory": crop_advisory,
        "crop_disease": crop_disease,
        "district_master": district_master,
        "government_schemes": government_schemes,
        "market_history": market_history,
        "seasonal_calendar": seasonal_calendar,
        "soil_profile": soil_profile
    }