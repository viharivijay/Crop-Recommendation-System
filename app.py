"""
=========================================================
AI Crop Recommendation System
Flask Application
=========================================================
"""

from flask import Flask
from flask import render_template
from flask import request

from utils.predictor import predict_crop
from utils.predictor import predict_specific_crop

from utils.market import get_market_summary
from utils.disease import get_disease_summary
from utils.advisor import get_advisory
from utils.schemes import get_scheme_summary

from utils.data_loader import district_master


# ==========================================================
# Flask App
# ==========================================================

app = Flask(__name__)


# ==========================================================
# Home Page
# ==========================================================

@app.route("/")
def home():

    districts = sorted(

        district_master["district"]

        .dropna()

        .unique()

        .tolist()

    )

    return render_template(

        "index.html",

        districts=districts

    )
# ==========================================================
# Predict
# ==========================================================

@app.route("/predict", methods=["POST"])
def predict():

    district = request.form.get("district", "").strip()

    selected_crop = request.form.get("crop", "").strip()

    # --------------------------------------------------
    # Validate District
    # --------------------------------------------------

    if district == "":

        return render_template(

            "result.html",

            success=False,

            message="Please select a district."

        )

    # --------------------------------------------------
    # AI Prediction
    # --------------------------------------------------

    prediction = predict_crop(district)

    if not prediction["success"]:

        return render_template(

            "result.html",

            success=False,

            message=prediction["message"]

        )

    # --------------------------------------------------
    # Recommended Crop
    # --------------------------------------------------

    recommended_crop = prediction["recommended_crop"]

    recommended_crop_kn = prediction["recommended_crop_kn"]

    # --------------------------------------------------
    # Market Information
    # --------------------------------------------------

    market = get_market_summary(

        recommended_crop

    )

    # --------------------------------------------------
    # Disease Information
    # --------------------------------------------------

    disease = get_disease_summary(

        recommended_crop

    )

    # --------------------------------------------------
    # Crop Advisory
    # --------------------------------------------------

    advisory = get_advisory(

        recommended_crop

    )

    # --------------------------------------------------
    # Government Schemes
    # --------------------------------------------------

    schemes = get_scheme_summary()

    # --------------------------------------------------
    # User Selected Crop
    # --------------------------------------------------

    user_crop_result = None

    if selected_crop != "":

        user_crop_result = predict_specific_crop(

            district,

            selected_crop

        )

    # --------------------------------------------------
    # Render Result
    # --------------------------------------------------

    return render_template(

        "result.html",

        success=True,

        district=prediction["district"],

        soil_type=prediction["soil_type"],

        weather=prediction["weather"],

        soil=prediction["soil"],

        recommended_crop=recommended_crop,

        recommended_crop_kn=recommended_crop_kn,

        top_predictions=prediction["top_predictions"],

        user_crop=user_crop_result,

        market=market,

        disease=disease,

        advisory=advisory,

        schemes=schemes

    )