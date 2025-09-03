
# ✈️ Flight Fare Prediction System

A machine learning-based web application that predicts flight prices based on various parameters such as airline, duration, stops, and class.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Model Performance](#model-performance)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)

## 🎯 Overview

This project implements a flight fare prediction system using machine learning algorithms. The system analyzes historical flight data to predict ticket prices, helping users make informed decisions about when to book their flights. The project includes data preprocessing, feature engineering, model training, and a Flask web application for real-time predictions.

## ✨ Features

- **Real-time Price Prediction**: Get instant flight fare predictions based on input parameters
- **Multiple Airlines Support**: Predictions for 6 major airlines (Air India, AirAsia, GO_FIRST, Indigo, SpiceJet, Vistara)
- **User-friendly Web Interface**: Simple and intuitive interface for entering flight details
- **Advanced Feature Engineering**: Z-score normalization and feature selection for optimal performance
- **RESTful API**: CORS-enabled API endpoints for integration with other applications

## 🛠️ Tech Stack

### Backend
- **Python 3.x**
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing

### Machine Learning
- **scikit-learn** - Machine learning algorithms
- **XGBoost** - Gradient boosting
- **pandas** - Data manipulation
- **numpy** - Numerical computations
- **scipy** - Statistical functions

### Data Visualization & Analysis
- **matplotlib** - Plotting
- **seaborn** - Statistical visualization
- **sweetviz** - Automated EDA
- **autoviz** - Automated visualization

## 📊 Dataset

- **Size**: 300,153 records
- **Features**: 12 columns including:
  - Airline
  - Flight code
  - Source and destination cities
  - Departure and arrival times
  - Number of stops
  - Class (Economy/Business)
  - Duration
  - Days left until departure
  - Price (target variable)

### Data Statistics
- **Price Range**: ₹1,105 - ₹123,071
- **Average Price**: ₹20,890
- **Airlines**: 6 major Indian carriers
- **Cities**: 6 major Indian cities

## 🚀 Installation

### Prerequisites
```bash
Python 3.7+
pip (Python package manager)
```

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/flight-fare-prediction.git
cd flight-fare-prediction
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

4. **Download the dataset**
Place the `airlines_flights_data.csv` file in the project root directory

5. **Train the model** (if pickle file not available)
```bash
python train_model.py
```

6. **Run the Flask application**
```bash
python app.py
```

7. **Access the application**
Open your browser and navigate to `http://localhost:8083`

## 📁 Project Structure

```
flight-fare-prediction/
│
├── app.py                    # Flask application
├── flight_fare.pkl          # Trained model (pickle file)
├── flight_fare.ipynb        # Jupyter notebook with analysis
├── requirements.txt         # Python dependencies
├── templates/               # HTML templates
│   └── home.html
└── README.md               # Project documentation
```

## 📈 Model Performance

### Model Comparison

| Model | Training R² | Testing R² | RMSE |
|-------|------------|------------|------|
| Linear Regression | 0.92 | 0.92 | 0.28 |
| XGBoost Regressor | 0.94 | 0.94 | 0.24 |
| **Random Forest** | **0.98** | **0.98** | **0.14** |

**Selected Model**: Random Forest Regressor (98% accuracy)

### Key Features Used
1. Airline
2. Flight code
3. Number of stops
4. Class (Economy/Business)
5. Duration

## 💻 Usage

### Web Interface

1. Navigate to the home page
2. Enter the following details:
   - Select airline
   - Choose number of stops
   - Select class (Economy/Business)
   - Enter flight duration (in hours)
3. Click "Predict" to get the fare estimate

### Sample Input
```json
{
  "airline": "Indigo",
  "stops": "one",
  "class": "Economy",
  "duration": 2.5
}
```

## 🔌 API Endpoints

### `GET /`
Returns the home page with the prediction form

### `POST /predict`
Accepts flight details and returns predicted fare

**Request Body**:
```json
{
  "airline": "string",
  "flight": "string",
  "stops": "string",
  "class": "string",
  "duration": "float"
}
```

**Response**:
```
Your Flight price is Rs. XX,XXX
```

## 🔄 Data Processing Pipeline

1. **Data Cleaning**: Removed index column, handled missing values
2. **Feature Encoding**:
   - Manual encoding for departure time, stops, arrival time, class
   - Label encoding for categorical features
3. **Normalization**: Z-score normalization for all features
4. **Outlier Treatment**: Capped outliers at 5th and 95th percentiles
5. **Feature Selection**: Selected top 5 features using f_regression

## 🔮 Future Enhancements

- [ ] Add more airlines and international flights
- [ ] Include seasonal pricing patterns
- [ ] Implement price trend visualization
- [ ] Add flight recommendation system
- [ ] Mobile application development
- [ ] Real-time data integration with airline APIs
- [ ] Price alert notifications
- [ ] Historical price analysis dashboard

## 📝 Requirements

Create a `requirements.txt` file with:
```txt
Flask==2.3.2
flask-cors==4.0.0
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
scipy==1.11.1
xgboost==1.7.6
pickle-mixin==1.0.2
```

## 👥 Authors

- Rohini Bawake 

## 🙏 Acknowledgments

- Dataset source: https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data 
- Inspiration from various flight booking platforms
---

