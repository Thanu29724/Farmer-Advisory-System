import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

# Get base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "crop_data.csv")

# Model save directory (THIS is key)
MODEL_DIR = os.path.join(BASE_DIR, "model")

print("Dataset path:", DATASET_PATH)
print("Model will be saved in:", MODEL_DIR)

# Load dataset
data = pd.read_csv(DATASET_PATH)

# Encoders
le_soil = LabelEncoder()
le_season = LabelEncoder()
le_crop = LabelEncoder()

data["soil_type"] = le_soil.fit_transform(data["soil_type"])
data["season"] = le_season.fit_transform(data["season"])
data["crop"] = le_crop.fit_transform(data["crop"])

X = data.drop("crop", axis=1)
y = data["crop"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save files INSIDE model folder
with open(os.path.join(MODEL_DIR, "crop_model.pkl"), "wb") as f:
    pickle.dump(model, f)

with open(os.path.join(MODEL_DIR, "soil_encoder.pkl"), "wb") as f:
    pickle.dump(le_soil, f)

with open(os.path.join(MODEL_DIR, "season_encoder.pkl"), "wb") as f:
    pickle.dump(le_season, f)

with open(os.path.join(MODEL_DIR, "crop_encoder.pkl"), "wb") as f:
    pickle.dump(le_crop, f)

print("✅ Model and encoders saved successfully")
