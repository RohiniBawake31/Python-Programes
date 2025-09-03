from flask import Flask, request, render_template, send_from_directory
from flask_cors import CORS, cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np
from scipy.stats import zscore
import os

app = Flask(__name__)
CORS(app)
model = pickle.load(open("flight_fare.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        try:
            # Get form data
            airline = request.form['airline']
            flight = request.form.get('flight', 'DEFAULT-123')  # Default flight code
            stops = request.form["stops"]
            travel_class = request.form["class"]
            duration = float(request.form["duration"])
            
            print(f"Raw inputs: airline={airline}, flight={flight}, stops={stops}, class={travel_class}, duration={duration}")
            
            # Manual encoding exactly as in your training code
            # Departure time mapping
            departure_time_map = {'Evening': 3, 'Early_Morning': 0, 'Morning': 1, 'Afternoon': 2, 'Night': 4, 'Late_Night': 5}
            
            # Stops mapping
            stops_map = {'zero': 0, 'one': 1, 'two_or_more': 2}
            stops_encoded = stops_map[stops]
            
            # Arrival time mapping
            arrival_time_map = {'Night': 4, 'Morning': 1, 'Early_Morning': 0, 'Afternoon': 2, 'Evening': 3, 'Late_Night': 5}
            
            # Class mapping
            class_map = {'Economy': 0, 'Business': 1}
            class_encoded = class_map[travel_class]
            
            # Airline mapping (LabelEncoder sorts alphabetically)
            # Run find_airline_mapping.py to get exact mapping
            airline_map = {
                'Air_India': 0,    # Air_India comes first alphabetically
                'AirAsia': 1,      # AirAsia
                'GO_FIRST': 2,     # GO_FIRST  
                'Indigo': 3,       # Indigo
                'SpiceJet': 4,     # SpiceJet
                'Vistara': 5       # Vistara
            }
            airline_encoded = airline_map[airline]
            
            # Flight encoding - since we don't have the exact mapping, use a default approach
            # You might need to adjust this based on your actual flight encoding
            flight_encoded = hash(flight) % 1000  # Simple hash-based encoding
            
            print(f"Encoded values: airline={airline_encoded}, flight={flight_encoded}, stops={stops_encoded}, class={class_encoded}, duration={duration}")
            
            # ACTUAL training data statistics from your training data
            training_stats = {
                'airline': {'mean': 3.104873, 'std': 1.833265},
                'flight': {'mean': 1088.338497, 'std': 426.691349},
                'stops': {'mean': 0.924312, 'std': 0.398106},
                'class': {'mean': 0.311464, 'std': 0.463093},
                'duration': {'mean': 12.221021, 'std': 7.191997},
            }
            
            # Create features array
            raw_features = [airline_encoded, flight_encoded, stops_encoded, class_encoded, duration]
            
            # Manually apply z-score normalization using training statistics
            normalized_features = []
            feature_names = ['airline', 'flight', 'stops', 'class', 'duration']
            
            for i, (feature_val, feature_name) in enumerate(zip(raw_features, feature_names)):
                mean = training_stats[feature_name]['mean']
                std = training_stats[feature_name]['std']
                z_score = (feature_val - mean) / std
                normalized_features.append(z_score)
                print(f"{feature_name}: {feature_val} -> z_score: {z_score:.4f}")
            
            # Create DataFrame with proper column names that match training
            feature_columns = ['airline_z', 'flight_z', 'stops_z', 'class_z', 'duration_z']
            features_df = pd.DataFrame([normalized_features], columns=feature_columns)
            
            print(f"Final features DataFrame:")
            print(features_df)
            
            # Make prediction (this will give z-score normalized price)
            prediction_z = model.predict(features_df)
            
            print(f"Z-score prediction: {prediction_z[0]}")
            
            # Convert z-score back to actual price using ACTUAL training statistics
            price_mean = 20889.66  # Your actual training data mean
            price_std = 22697.77   # Your actual training data std
            
            actual_price = (prediction_z[0] * price_std) + price_mean
            output = max(1000, round(actual_price, 2))  # Ensure minimum reasonable price
            
            print(f"Final predicted price: {output}")
            
            return render_template('home.html', prediction_text=f"Your Flight price is Rs. {output:,}")

        except KeyError as e:
            return render_template('home.html', prediction_text=f"Missing form field: {str(e)}")
        except ValueError as e:
            return render_template('home.html', prediction_text=f"Invalid input value: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return render_template('home.html', prediction_text=f"Error in prediction: {str(e)}")

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port=8083)