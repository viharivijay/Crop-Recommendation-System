
# 🌾 AgroXAI – Explainable AI Crop Recommendation System

### Empowering Smart and Sustainable Agriculture Through Artificial Intelligence

AgroXAI is an AI-powered agricultural decision-support system designed to help farmers make informed farming decisions through Machine Learning, data analysis, and Natural Language Processing (NLP).

The system analyzes soil nutrients and climatic conditions to recommend suitable crops while providing additional agricultural insights such as crop disease information, market price analysis, weather-based advisory, government schemes, and Kannada language translation.

By integrating Artificial Intelligence with agricultural data, AgroXAI aims to support smarter, more accessible, and sustainable farming practices.

---

## 📌 Project Overview

Agriculture plays a vital role in India's economy. However, farmers often face challenges in selecting suitable crops, understanding soil conditions, accessing market information, and identifying appropriate agricultural schemes.

AgroXAI addresses these challenges through an integrated AI-based platform that combines predictive Machine Learning models with agricultural datasets and intelligent advisory features.

The application provides a user-friendly interface through which users can explore crop recommendations and relevant agricultural information.

---

## 🎯 Objectives

- Develop an AI-based crop recommendation system.
- Analyze soil nutrients and environmental conditions.
- Recommend suitable crops using Machine Learning.
- Provide agricultural market price insights.
- Offer crop disease information and advisory.
- Provide weather-based agricultural guidance.
- Improve accessibility through Kannada language translation.
- Support informed and data-driven agricultural decisions.

---

## ✨ Key Features

### 1. 🌱 AI-Based Crop Recommendation
- Predicts suitable crops based on agricultural parameters.
- Uses soil nutrient values such as Nitrogen (N), Phosphorus (P), and Potassium (K).
- Considers temperature, humidity, soil pH, and rainfall.
- Uses a trained Machine Learning model for prediction.

### 2. 🔍 Explainable AI
- Designed to make AI-powered crop recommendations more understandable.
- Helps users understand the agricultural parameters considered during prediction.

### 3. 🌿 Crop Disease Information
- Provides crop-related disease information.
- Offers agricultural guidance and relevant advisory information.

### 4. 🌦️ Weather-Based Advisory
- Provides weather-related agricultural insights.
- Helps users understand environmental conditions relevant to farming.

### 5. 📊 Agricultural Market Analysis
- Provides crop market price information.
- Uses agricultural market datasets to display relevant price insights.

### 6. 🏛️ Government Agricultural Schemes
- Provides information about agricultural schemes.
- Helps users explore government support and farming-related initiatives.

### 7. 🌐 Kannada Language Translation
- Integrates Natural Language Processing (NLP)-based translation.
- Supports Kannada translation of agricultural recommendations.
- Improves accessibility for Kannada-speaking users.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | Flask |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Frontend | HTML, CSS, JavaScript |
| UI Framework | Bootstrap 5 |
| NLP | Kannada Language Translation |
| Data Visualization | Matplotlib |
| Development Tools | VS Code, Git, GitHub |

---

## 🏗️ System Architecture

The AgroXAI application follows a web-based architecture.

1. **User Input:** Users enter soil and climatic parameters.
2. **Data Processing:** Input parameters are processed and prepared for prediction.
3. **Machine Learning Model:** The trained model analyzes the input data.
4. **Crop Prediction:** The system generates a suitable crop recommendation.
5. **Additional Services:** Users can access market insights, disease information, weather advisory, and government schemes.
6. **Language Support:** Agricultural recommendations can be translated into Kannada.
7. **Output Display:** Results are presented through the Flask-based web interface.

---

## 📂 Project Structure

```text
Crop-Recommendation-System/
│
├── app.py
│
├── datasets/
│
├── models/
│
├── templates/
│   ├── index.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── utils/
│
├── requirements.txt
│
└── README.md
```

*Note: The structure above represents the main application components. Actual filenames and folders may vary depending on your repository.*

---

## ⚙️ Installation and Setup

### Prerequisites

Make sure the following are installed:

- Python 3.10 or later
- pip
- Git
- Visual Studio Code

### Step 1: Clone the Repository

```bash
git clone https://github.com/viharivijay/Crop-Recommendation-System.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Crop-Recommendation-System
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open in Browser

```text
http://127.0.0.1:5000/
```

---

## 🧪 Input Parameters

The crop recommendation model uses the following agricultural parameters:

| Parameter | Description |
|---|---|
| Nitrogen (N) | Nitrogen content in soil |
| Phosphorus (P) | Phosphorus content in soil |
| Potassium (K) | Potassium content in soil |
| Temperature | Environmental temperature |
| Humidity | Relative humidity |
| pH | Soil pH value |
| Rainfall | Rainfall measurement |

The model uses these parameters to identify a suitable crop based on the patterns learned during training.

---

## 🌍 Applications

- Smart and precision agriculture.
- Soil-based crop selection.
- Agricultural decision support.
- Market price awareness.
- Crop disease awareness.
- Regional language accessibility.
- Sustainable farming practices.

---

## 🚀 Future Enhancements

- Integration with real-time weather APIs.
- Advanced Explainable AI visualizations using SHAP or LIME.
- Image-based crop disease detection using Deep Learning.
- Voice-based agricultural assistance.
- Support for additional regional languages.
- Farmer-specific personalized recommendations.
- Mobile application integration.
- Real-time agricultural market data integration.

---

## 🎓 Project Information

**Project Name:** AgroXAI – Explainable AI Crop Recommendation System

**Domain:** Artificial Intelligence and Machine Learning

**Application Type:** Web-Based Agricultural Decision Support System

**Backend:** Python and Flask

**Primary Focus:** Machine Learning-Based Crop Recommendation

**Regional Language Support:** Kannada

---

## 👩‍💻 Developer

**Developed by:** Vihari Vijay

**GitHub:**  
https://github.com/viharivijay

**Project Repository:**  
https://github.com/viharivijay/Crop-Recommendation-System

---

## 📜 License

This project is developed for educational, learning, and demonstration purposes.

---

## 💚 Acknowledgement

AgroXAI represents the integration of Artificial Intelligence, Machine Learning, and agricultural data to explore practical solutions for smarter farming.

**Technology for Agriculture. Intelligence for a Better Future.** 🌾
