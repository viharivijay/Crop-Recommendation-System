"""
====================================================
Crop Advisory Module
====================================================
"""

import pandas as pd

from utils.data_loader import crop_advisory


# ====================================================
# Clean Dataset
# ====================================================

crop_advisory["crop"] = (

    crop_advisory["crop"]

    .astype(str)

    .str.strip()

    .str.lower()

)


# ====================================================
# Get Crop Advisory
# ====================================================

def get_crop_advisory(crop):

    crop = crop.strip().lower()

    df = crop_advisory[

        crop_advisory["crop"] == crop

    ]

    if df.empty:

        return None

    return df.copy()
# ====================================================
# Advisory Summary
# ====================================================

def get_advisory(crop):

    df = get_crop_advisory(crop)

    if df is None:

        return {

            "success": False,

            "message": "Advisory information not available."

        }

    row = df.iloc[0]

    return {

        "success": True,

        "crop": crop.title(),

        "advisory": row["advisory"],

        "fertilizer_recommendation": row["fertilizer_recommendation"],

        "irrigation_tip": row["irrigation_tip"],

        "best_practice": row["best_practice"]

    }


# ====================================================
# Get Fertilizer Recommendation
# ====================================================

def get_fertilizer(crop):

    result = get_advisory(crop)

    if not result["success"]:

        return None

    return result["fertilizer_recommendation"]


# ====================================================
# Get Irrigation Tip
# ====================================================

def get_irrigation_tip(crop):

    result = get_advisory(crop)

    if not result["success"]:

        return None

    return result["irrigation_tip"]
# ====================================================
# Get Best Practice
# ====================================================

def get_best_practice(crop):

    result = get_advisory(crop)

    if not result["success"]:

        return None

    return result["best_practice"]


# ====================================================
# Complete Advisory
# ====================================================

def get_complete_advisory(crop):

    return get_advisory(crop)


# ====================================================
# Testing
# ====================================================

if __name__ == "__main__":

    print("\n===================================")
    print(" CROP ADVISORY MODULE TEST ")
    print("===================================\n")

    crop = "Rice"

    result = get_advisory(crop)

    if result["success"]:

        print("Crop :", result["crop"])

        print("\nGeneral Advisory")
        print("---------------------------")
        print(result["advisory"])

        print("\nFertilizer Recommendation")
        print("---------------------------")
        print(result["fertilizer_recommendation"])

        print("\nIrrigation Tip")
        print("---------------------------")
        print(result["irrigation_tip"])

        print("\nBest Practice")
        print("---------------------------")
        print(result["best_practice"])

    else:

        print(result["message"])
