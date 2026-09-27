"""
weather.py

Fetches live weather using Open-Meteo API
based on district selected by the user.

Author: AI Crop Recommendation System
"""

import requests

from utils.data_loader import district_master


# ==========================================================
# Get Latitude & Longitude from district_master.csv
# ==========================================================

def get_location(district):
    """
    Returns latitude and longitude for a district.
    """

    row = district_master[
        district_master["district"].str.lower() == district.lower()
    ]

    if row.empty:
        return None

    latitude = float(row.iloc[0]["latitude"])
    longitude = float(row.iloc[0]["longitude"])

    return latitude, longitude


# ==========================================================
# Fetch Weather from Open-Meteo
# ==========================================================

def get_live_weather(district):
    """
    Returns live weather dictionary.

    Parameters
    ----------
    district : str

    Returns
    -------
    dict
    """

    location = get_location(district)

    if location is None:

        return {
            "success": False,
            "message": "District not found."
        }

    latitude, longitude = location

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current="
        "temperature_2m,"
        "relative_humidity_2m,"
        "precipitation,"
        "wind_speed_10m,"
        "weather_code"
    )

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        current = data["current"]

        weather = {

            "success": True,

            "district": district,

            "temperature": current["temperature_2m"],

            "humidity": current["relative_humidity_2m"],

            "rainfall": current["precipitation"],

            "wind_speed": current["wind_speed_10m"],

            "weather_code": current["weather_code"]

        }

        return weather

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }


# ==========================================================
# Weather Code Description
# ==========================================================

def weather_description(code):
    """
    Converts Open-Meteo weather code
    into readable description.
    """

    weather_codes = {

        0: "Clear Sky",

        1: "Mainly Clear",

        2: "Partly Cloudy",

        3: "Cloudy",

        45: "Fog",

        48: "Fog",

        51: "Light Drizzle",

        53: "Moderate Drizzle",

        55: "Dense Drizzle",

        56: "Freezing Drizzle",

        57: "Heavy Freezing Drizzle",

        61: "Light Rain",

        63: "Rain",

        65: "Heavy Rain",

        66: "Freezing Rain",

        67: "Heavy Freezing Rain",

        71: "Light Snow",

        73: "Snow",

        75: "Heavy Snow",

        77: "Snow Grains",

        80: "Rain Showers",

        81: "Heavy Rain Showers",

        82: "Violent Rain Showers",

        85: "Snow Showers",

        86: "Heavy Snow Showers",

        95: "Thunderstorm",

        96: "Thunderstorm with Hail",

        99: "Severe Thunderstorm"

    }

    return weather_codes.get(code, "Unknown")


# ==========================================================
# Complete Weather Report
# ==========================================================

def weather_report(district):
    """
    Returns complete weather report.
    """

    weather = get_live_weather(district)

    if not weather["success"]:
        return weather

    weather["description"] = weather_description(
        weather["weather_code"]
    )

    return weather


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    report = weather_report("Mysuru")

    print()

    print("LIVE WEATHER")

    print("--------------------------")

    for key, value in report.items():

        print(f"{key} : {value}")