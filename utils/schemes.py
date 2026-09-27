"""
====================================================
Government Schemes Module
====================================================
"""

from utils.data_loader import government_schemes


# ====================================================
# Clean Dataset
# ====================================================

government_schemes["scheme_name"] = (
    government_schemes["scheme_name"]
    .astype(str)
    .str.strip()
)

government_schemes["category"] = (
    government_schemes["category"]
    .astype(str)
    .str.strip()
)

government_schemes["benefit"] = (
    government_schemes["benefit"]
    .astype(str)
    .str.strip()
)

government_schemes["eligibility"] = (
    government_schemes["eligibility"]
    .astype(str)
    .str.strip()
)

government_schemes["official_website"] = (
    government_schemes["official_website"]
    .astype(str)
    .str.strip()
)


# ====================================================
# Get All Government Schemes
# ====================================================

def get_scheme_summary():

    schemes = []

    for _, row in government_schemes.iterrows():

        schemes.append({

            "scheme_name": row["scheme_name"],

            "category": row["category"],

            "benefit": row["benefit"],

            "eligibility": row["eligibility"],

            "official_website": row["official_website"]

        })

    return {

        "success": True,

        "total_schemes": len(schemes),

        "schemes": schemes

    }
# ====================================================
# Get Scheme Names
# ====================================================

def get_scheme_names():

    result = get_scheme_summary()

    if not result["success"]:

        return []

    names = []

    for scheme in result["schemes"]:

        names.append(

            scheme["scheme_name"]

        )

    return names


# ====================================================
# Get Official Websites
# ====================================================

def get_scheme_websites():

    result = get_scheme_summary()

    if not result["success"]:

        return []

    websites = []

    for scheme in result["schemes"]:

        websites.append(

            scheme["official_website"]

        )

    return websites


# ====================================================
# Get Scheme Count
# ====================================================

def get_scheme_count():

    result = get_scheme_summary()

    if not result["success"]:

        return 0

    return result["total_schemes"]


# ====================================================
# Get All Schemes
# ====================================================

def get_all_schemes():

    return get_scheme_summary()
# ====================================================
# Testing
# ====================================================

if __name__ == "__main__":

    print("\n===================================")
    print(" GOVERNMENT SCHEMES MODULE TEST ")
    print("===================================\n")

    result = get_scheme_summary()

    if result["success"]:

        print("Total Schemes :", result["total_schemes"])

        print("\nAvailable Scheme Names")
        print("----------------------------")

        for name in get_scheme_names():

            print("-", name)

        print("\nDetailed Information")
        print("----------------------------")

        for i, scheme in enumerate(result["schemes"], start=1):

            print(f"\nScheme {i}")

            print("----------------------------")

            print("Name :", scheme["scheme_name"])

            print("Category :", scheme["category"])

            print("Benefit :", scheme["benefit"])

            print("Eligibility :", scheme["eligibility"])

            print("Official Website :", scheme["official_website"])

    else:

        print("No government schemes available.")