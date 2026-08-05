"""
====================================================
Market Module
====================================================
"""

import pandas as pd

from utils.data_loader import market_history


# ====================================================
# Clean Dataset
# ====================================================

market_history["Commodity"] = (
    market_history["Commodity"]
    .astype(str)
    .str.strip()
)

market_history["Modal Price (Rs./Quintal)"] = pd.to_numeric(
    market_history["Modal Price (Rs./Quintal)"],
    errors="coerce"
)

market_history["Price Date"] = pd.to_datetime(
    market_history["Price Date"],
    format="%d %b %Y",
    errors="coerce"
)


# ====================================================
# Get Crop Data
# ====================================================

def get_market_data(crop):

    crop = crop.strip().lower()

    df = market_history[
        market_history["Commodity"]
        .str.lower()
        ==
        crop
    ]

    if df.empty:

        return None

    return df.copy()
# ====================================================
# Market Summary
# ====================================================

def get_market_summary(crop):

    df = get_market_data(crop)

    if df is None:

        return {

            "success": False,

            "message": "Market data not available."

        }

    # Remove invalid rows

    df = df.dropna(
        subset=[
            "Modal Price (Rs./Quintal)",
            "Price Date"
        ]
    )

    if df.empty:

        return {

            "success": False,

            "message": "No valid market records."

        }

    # Latest record

    latest = df.sort_values(
        by="Price Date",
        ascending=False
    ).iloc[0]

    average_price = float(round(

        df["Modal Price (Rs./Quintal)"].mean(),

        2

    ))

    highest_price = float(round(

        df["Modal Price (Rs./Quintal)"].max(),

        2

    ))

    lowest_price = float(round(

        df["Modal Price (Rs./Quintal)"].min(),

        2

    ))

    latest_price = float(

        latest["Modal Price (Rs./Quintal)"]

    )

    latest_market = str(

        latest["Market Name"]

    )

    latest_district = str(

        latest["District Name"]

    )

    latest_state = str(

        latest["State"]

    )

    first_price = float(

        df.sort_values(
            by="Price Date"
        ).iloc[0]["Modal Price (Rs./Quintal)"]

    )

    # ===============================================
    # Trend
    # ===============================================

    if latest_price > first_price:

        trend = "Increasing"

    elif latest_price < first_price:

        trend = "Decreasing"

    else:

        trend = "Stable"

    return {

        "success": True,

        "crop": crop.title(),

        "average_price": average_price,

        "highest_price": highest_price,

        "lowest_price": lowest_price,

        "latest_price": latest_price,

        "trend": trend,

        "market": latest_market,

        "district": latest_district,

        "state": latest_state,

        "records": len(df)

    }
# ====================================================
# Latest Market Records
# ====================================================

def get_latest_market_records(crop, limit=10):

    df = get_market_data(crop)

    if df is None:
        return pd.DataFrame()

    df = df.dropna(
        subset=[
            "Modal Price (Rs./Quintal)",
            "Price Date"
        ]
    )

    df = df.sort_values(
        by="Price Date",
        ascending=False
    )

    return df.head(limit)


# ====================================================
# Available Commodities
# ====================================================

def get_available_commodities():

    commodities = sorted(

        market_history["Commodity"]

        .dropna()

        .unique()

        .tolist()

    )

    return commodities


# ====================================================
# Available Districts
# ====================================================

def get_available_districts(crop):

    df = get_market_data(crop)

    if df is None:

        return []

    districts = sorted(

        df["District Name"]

        .dropna()

        .unique()

        .tolist()

    )

    return districts


# ====================================================
# Available Markets
# ====================================================

def get_available_markets(crop):

    df = get_market_data(crop)

    if df is None:

        return []

    markets = sorted(

        df["Market Name"]

        .dropna()

        .unique()

        .tolist()

    )

    return markets


# ====================================================
# Test
# ====================================================

if __name__ == "__main__":

    print("\n===================================")
    print(" MARKET MODULE TEST ")
    print("===================================\n")

    crop = "Rice"

    result = get_market_summary(crop)

    if result["success"]:

        print("Crop :", result["crop"])

        print("Average Price :", result["average_price"])

        print("Highest Price :", result["highest_price"])

        print("Lowest Price :", result["lowest_price"])

        print("Latest Price :", result["latest_price"])

        print("Trend :", result["trend"])

        print("Market :", result["market"])

        print("District :", result["district"])

        print("State :", result["state"])

        print("Records :", result["records"])

    else:

        print(result["message"])

    print("\nAvailable Commodities :")

    print(get_available_commodities()[:20])

    print("\nAvailable Markets for Rice :")

    print(get_available_markets("Rice"))

    print("\nAvailable Districts for Rice :")

    print(get_available_districts("Rice"))