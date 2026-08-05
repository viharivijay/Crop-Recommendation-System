"""
=========================================================
AI Crop Recommendation System
Predictor Module
=========================================================
"""

import os
import joblib
import pandas as pd
import numpy as np

from utils.data_loader import district_master
from utils.data_loader import soil_profile
from utils.weather import weather_report
from utils.translations import crop_translation


# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "crop_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "label_encoder.pkl"
)


# ==========================================================
# LOAD MODEL
# ==========================================================

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model not found: {MODEL_PATH}"
    )

if not os.path.exists(ENCODER_PATH):
    raise FileNotFoundError(
        f"Encoder not found: {ENCODER_PATH}"
    )

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)


# ==========================================================
# GET SOIL TYPE
# ==========================================================

def get_soil_type(district):
    """
    Returns soil type from district_master.csv
    """

    row = district_master[
        district_master["district"].str.lower()
        ==
        district.lower()
    ]

    if row.empty:
        return None

    return row.iloc[0]["soil_type"]


# ==========================================================
# GET SOIL NPK VALUES
# ==========================================================

def get_soil_values(soil_type):
    """
    Returns:
    Nitrogen
    Phosphorus
    Potassium
    pH
    """

    row = soil_profile[
        soil_profile["soil_type"].str.lower()
        ==
        soil_type.lower()
    ]

    if row.empty:
        return None

    nitrogen = float(row.iloc[0]["nitrogen"])
    phosphorus = float(row.iloc[0]["phosphorus"])
    potassium = float(row.iloc[0]["potassium"])
    ph = float(row.iloc[0]["ph"])

    return (
        nitrogen,
        phosphorus,
        potassium,
        ph
    )


# ==========================================================
# PREPARE MODEL INPUT
# ==========================================================

def prepare_input(
    nitrogen,
    phosphorus,
    potassium,
    temperature,
    humidity,
    ph,
    rainfall
):
    """
    Creates dataframe exactly like training data.
    """

    sample = pd.DataFrame([{

        "N": nitrogen,
        "P": phosphorus,
        "K": potassium,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall

    }])

    return sample
# ==========================================================
# PREDICT CROP
# ==========================================================

def predict_crop(district):
    """
    Predicts the best crops for a district using:
    - Soil type
    - Soil nutrients
    - Live weather
    """

    # -------------------------
    # Get Live Weather
    # -------------------------

    weather = weather_report(district)

    if not weather["success"]:
        return weather

    temperature = float(weather["temperature"])
    humidity = float(weather["humidity"])
    rainfall = float(weather["rainfall"])

    # -------------------------
    # Get Soil Type
    # -------------------------

    soil_type = get_soil_type(district)

    if soil_type is None:
        return {
            "success": False,
            "message": "District not found in district_master.csv"
        }

    # -------------------------
    # Get Soil Nutrients
    # -------------------------

    soil = get_soil_values(soil_type)

    if soil is None:
        return {
            "success": False,
            "message": "Soil profile not found."
        }

    nitrogen, phosphorus, potassium, ph = soil

    # -------------------------
    # Prepare Model Input
    # -------------------------

    sample = prepare_input(
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    )

    # -------------------------
    # Prediction
    # -------------------------

    prediction = model.predict(sample)

    predicted_crop = label_encoder.inverse_transform(
        prediction
    )[0]

    predicted_crop_kn = crop_translation.get(
        predicted_crop.lower(),
        predicted_crop
    )

    # -------------------------
    # Prediction Probability
    # -------------------------

    probabilities = model.predict_proba(sample)[0]

    sorted_index = np.argsort(probabilities)[::-1]

    top_predictions = []

    for index in sorted_index[:3]:

        crop_name = label_encoder.inverse_transform(
            [index]
        )[0]

        crop_name_kn = crop_translation.get(
            crop_name.lower(),
            crop_name
        )

        confidence = float(
            round(probabilities[index] * 100, 2)
        )

        top_predictions.append({

            "crop": crop_name,

            "crop_kn": crop_name_kn,

            "confidence": confidence

        })

    # -------------------------
    # Final Result
    # -------------------------

    result = {

        "success": True,

        "district": district,

        "soil_type": soil_type,

        "weather": {

            "temperature": temperature,

            "humidity": humidity,

            "rainfall": rainfall

        },

        "soil": {

            "nitrogen": nitrogen,

            "phosphorus": phosphorus,

            "potassium": potassium,

            "ph": ph

        },

        "recommended_crop": predicted_crop,

        "recommended_crop_kn": predicted_crop_kn,

        "top_predictions": top_predictions

    }

    return result
# ==========================================================
# CHECK USER SELECTED CROP
# ==========================================================

def predict_specific_crop(district, crop_name):
    """
    Checks whether the farmer's selected crop
    matches the AI recommendation.
    """

    result = predict_crop(district)

    if not result["success"]:
        return result

    crop_name = crop_name.strip().lower()

    recommended = result["recommended_crop"].lower()

    suitable = False
    confidence = 0.0

    for item in result["top_predictions"]:

        if item["crop"].lower() == crop_name:

            suitable = True
            confidence = item["confidence"]

            break

    return {

        "success": True,

        "district": district,

        "selected_crop": crop_name.title(),

        "recommended_crop": result["recommended_crop"],

        "recommended_crop_kn": result["recommended_crop_kn"],

        "recommended": suitable,

        "confidence": confidence,

        "top_predictions": result["top_predictions"]

    }


# ==========================================================
# GET ONLY TOP 3 CROPS
# ==========================================================

def get_top_crops(district):

    result = predict_crop(district)

    if not result["success"]:
        return result

    return result["top_predictions"]


# ==========================================================
# GET WEATHER ONLY
# ==========================================================

def get_weather(district):

    result = predict_crop(district)

    if not result["success"]:
        return result

    return result["weather"]


# ==========================================================
# GET SOIL DETAILS
# ==========================================================

def get_soil(district):

    result = predict_crop(district)

    if not result["success"]:
        return result

    return {

        "soil_type": result["soil_type"],

        "soil": result["soil"]

    }


# ==========================================================
# TESTING
# ==========================================================

if __name__ == "__main__":

    district = "Mysuru"

    result = predict_crop(district)

    if result["success"]:

        print("\n==============================")
        print("AI CROP RECOMMENDATION SYSTEM")
        print("==============================")

        print("\nDistrict :", result["district"])

        print("Soil Type :", result["soil_type"])

        print("\nWeather")
        print(result["weather"])

        print("\nSoil")
        print(result["soil"])

        print("\nRecommended Crop")
        print(
            f"{result['recommended_crop']} "
            f"({result['recommended_crop_kn']})"
        )

        print("\nTop 3 Predictions")

        for i, crop in enumerate(result["top_predictions"], start=1):

            print(
                f"{i}. {crop['crop']} "
                f"({crop['crop_kn']}) "
                f"- {crop['confidence']}%"
            )

    else:

        print(result["message"])