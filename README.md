# 🌾 Farmer Advisory System

A **machine learning–based Farmer Advisory System** that helps farmers make informed agricultural decisions by recommending suitable crops based on **soil type, weather parameters, and season**.  
The system uses a **Flask backend with an ML model** and a **modern React + JavaScript frontend** inspired by BookMyShow-style UI for better usability.

---

## 📌 Project Overview

Farmers often face challenges in selecting the right crop due to lack of timely guidance on soil conditions, weather, and seasonal factors.  
This project provides a **data-driven crop recommendation system** that suggests the most suitable crop using machine learning and an easy-to-use web interface.

---

## ✨ Features

- 🌱 Crop recommendation using Machine Learning  
- 🌦 Input-based advisory using temperature, humidity, rainfall, soil, and season  
- ⚛️ Modern React frontend with JavaScript  
- 🔗 REST API communication between React and Flask  
- 🧠 Trained ML model using Decision Tree algorithm  
- 💾 Model persistence using Pickle  
- 🌐 User-friendly and responsive interface  
- 📊 Clear and visually attractive output display  

---

## 🛠️ Technologies Used

### 🔹 Frontend
- React.js  
- JavaScript (ES6)  
- HTML5  
- CSS3  

### 🔹 Backend
- Python  
- Flask  
- Flask-CORS (API communication)  

### 🔹 Machine Learning
- Scikit-learn  
- Decision Tree Classifier  
- Pandas  
- NumPy  

### 🔹 Tools & Platforms
- VS Code  
- Git & GitHub  
- Postman (API testing)  

---

## 🧠 Machine Learning Details

- **Algorithm Used:** Decision Tree Classifier  
- **Input Parameters:**
  - Soil Type (Loamy, Sandy, Clay)
  - Temperature (°C)
  - Humidity (%)
  - Rainfall (mm)
  - Season (Kharif, Rabi, Summer)
- **Output:** Recommended Crop  

---

## 🗂️ Project Structure

Farmer-Advisory-System/
│
├── dataset/

│ └── crop_data.csv

├── model/

│ ├── train_model.py

│ ├── crop_model.pkl

│ ├── soil_encoder.pkl

│ ├── season_encoder.pkl

│ └── crop_encoder.pkl
│
├── templates/

│ └── index.html
│
├── app.py

├── README.md

├── .gitignore

└── venv/


---

## 🚀 How to Run the Project

## 1️⃣ Clone the Repository

git clone https://github.com/Thanu29724/Farmer-Advisory-System.git

cd Farmer-Advisory-System

## 2️⃣ Install Dependencies

pip install flask pandas numpy scikit-learn flask-cors

## 3️⃣ Train the Model

python model/train_model.py

## 4️⃣ Run Flask Backend

python app.py

Backend runs on: 

 ## Future Enhancements

🌦 Live Weather API integration

🌱 Fertilizer recommendation system

🌍 Regional language support (Kannada, Hindi, etc.)

📊 Confidence score for recommendations

📜 Prediction history tracking

📱 Mobile-first UI / Android app

🚀 Cloud deployment (Render / AWS / Vercel)

## 💼 Use Cases

Smart agriculture systems

Farmer decision-support tools

Educational and research purposes

Government and NGO agricultural advisory platforms

## 👨‍💻 Author

Thanush M N

AI / ML | Full Stack | Electronics

GitHub: https://github.com/Thanu29724

