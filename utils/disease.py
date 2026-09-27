"""
====================================================
Disease Module
====================================================
"""

import pandas as pd

from utils.data_loader import crop_disease


# ====================================================
# Clean Dataset
# ====================================================

crop_disease["crop"] = (

    crop_disease["crop"]

    .astype(str)

    .str.strip()

    .str.lower()

)


# ====================================================
# Get Disease Data
# ====================================================

def get_disease_data(crop):

    crop = crop.strip().lower()

    df = crop_disease[

        crop_disease["crop"] == crop

    ]

    if df.empty:

        return None

    return df.copy()
# ====================================================
# Disease Summary
# ====================================================

def get_disease_summary(crop):

    df = get_disease_data(crop)

    if df is None:

        return {

            "success": False,

            "message": "Disease information not available."

        }

    row = df.iloc[0]

    return {

        "success": True,

        "crop": crop.title(),

        "humidity_risk": row["high_humidity_risk"],

        "high_temperature_risk": row["high_temperature_risk"],

        "low_temperature_risk": row["low_temperature_risk"],

        "heavy_rainfall_risk": row["heavy_rainfall_risk"],

        "prevention": row["prevention"],

        "severity": row["severity"]

    }


# ====================================================
# Get Prevention Only
# ====================================================

def get_prevention(crop):

    result = get_disease_summary(crop)

    if not result["success"]:

        return None

    return result["prevention"]
# ====================================================
# Get Severity
# ====================================================

def get_severity(crop):

    result = get_disease_summary(crop)

    if not result["success"]:

        return None

    return result["severity"]


# ====================================================
# Get Disease Risks Only
# ====================================================

def get_risks(crop):

    result = get_disease_summary(crop)

    if not result["success"]:

        return None

    return {

        "high_humidity": result["humidity_risk"],

        "high_temperature": result["high_temperature_risk"],

        "low_temperature": result["low_temperature_risk"],

        "heavy_rainfall": result["heavy_rainfall_risk"]

    }


# ====================================================
# Testing
# ====================================================

if __name__ == "__main__":

    print("\n===================================")
    print(" DISEASE MODULE TEST ")
    print("===================================\n")

    crop = "Rice"

    result = get_disease_summary(crop)

    if result["success"]:

        print("Crop :", result["crop"])

        print("Severity :", result["severity"])

        print("\nDisease Risks")

        print("---------------------------")

        print("High Humidity :", result["humidity_risk"])

        print("High Temperature :", result["high_temperature_risk"])

        print("Low Temperature :", result["low_temperature_risk"])

        print("Heavy Rainfall :", result["heavy_rainfall_risk"])

        print("\nPrevention")

        print("---------------------------")

        print(result["prevention"])

    else:

        print(result["message"])