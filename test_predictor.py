from utils.predictor import (
    predict_crop,
    predict_specific_crop,
    get_top_crops,
    get_weather,
    get_soil
)

print("=" * 60)
print("AI CROP RECOMMENDATION SYSTEM")
print("=" * 60)

district = "Mysuru"

# -------------------------------------------------
# Full Prediction
# -------------------------------------------------

print("\n1. Full Prediction\n")

result = predict_crop(district)

if result["success"]:

    print("District :", result["district"])
    print("Soil Type :", result["soil_type"])

    print("\nWeather")
    print(result["weather"])

    print("\nSoil")
    print(result["soil"])

    print("\nRecommended Crop")
    print(result["recommended_crop"])

    print("\nTop 3 Predictions")

    for crop in result["top_predictions"]:
        print(
            f"{crop['crop']} --> {crop['confidence']}%"
        )

else:

    print(result["message"])


# -------------------------------------------------
# Top 3 Crops
# -------------------------------------------------

print("\n" + "=" * 60)
print("2. Top 3 Crops")
print("=" * 60)

top = get_top_crops(district)

print(top)


# -------------------------------------------------
# Weather
# -------------------------------------------------

print("\n" + "=" * 60)
print("3. Weather")
print("=" * 60)

weather = get_weather(district)

print(weather)


# -------------------------------------------------
# Soil
# -------------------------------------------------

print("\n" + "=" * 60)
print("4. Soil")
print("=" * 60)

soil = get_soil(district)

print(soil)


# -------------------------------------------------
# Check User Crop
# -------------------------------------------------

print("\n" + "=" * 60)
print("5. User Selected Crop")
print("=" * 60)

selected = predict_specific_crop(
    district,
    "Rice"
)

print(selected)


print("\n")
print("=" * 60)
print("TEST COMPLETED SUCCESSFULLY")
print("=" * 60)