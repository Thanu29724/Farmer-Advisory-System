from flask import Flask, render_template, request, session
import pickle
import numpy as np
import os

app = Flask(__name__)
app.secret_key = "farmer_advisory_secret_key"

# 📁 Base directory (project root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 📁 Model directory
MODEL_DIR = os.path.join(BASE_DIR, "model")

# ✅ Load trained model & encoders
model = pickle.load(open(os.path.join(MODEL_DIR, "crop_model.pkl"), "rb"))
soil_enc = pickle.load(open(os.path.join(MODEL_DIR, "soil_encoder.pkl"), "rb"))
season_enc = pickle.load(open(os.path.join(MODEL_DIR, "season_encoder.pkl"), "rb"))
crop_enc = pickle.load(open(os.path.join(MODEL_DIR, "crop_encoder.pkl"), "rb"))

print("✅ Loaded model files from:", MODEL_DIR)

@app.route("/")
def home():
    result = session.get("result")
    return render_template("index.html", result=result)

@app.route("/predict", methods=["POST"])
def predict():
    soil = request.form["soil"]
    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    rainfall = float(request.form["rainfall"])
    season = request.form["season"]

    soil_val = soil_enc.transform([soil])[0]
    season_val = season_enc.transform([season])[0]

    features = np.array([[soil_val, temp, humidity, rainfall, season_val]])
    prediction = model.predict(features)
    crop = crop_enc.inverse_transform(prediction)[0]

    # Store result
    session["result"] = crop

    return render_template("index.html", result=crop)

if __name__ == "__main__":
    app.run(debug=True)
