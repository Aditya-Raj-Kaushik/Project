# 🔥 Fire Weather Index (FWI) Prediction Web App

This project is a **Machine Learning–powered web application** that predicts the **Fire Weather Index (FWI)** based on meteorological and environmental inputs.  
The application is built using **Flask**, **Scikit-learn**, **Docker**, and is **deployed on AWS EC2**.

---

## 📌 Problem Statement

Forest fires are strongly influenced by weather conditions such as temperature, humidity, wind speed, and moisture content of fuels.  
The **Fire Weather Index (FWI)** is a numerical indicator used to estimate **fire intensity and spread risk**.

This project aims to:
- Predict FWI using historical weather data
- Provide an easy-to-use web interface for prediction
- Deploy the model as a scalable cloud application

---

## 🧠 Machine Learning Model

- **Algorithm**: Ridge Regression  
- **Preprocessing**: StandardScaler  
- **Training**: Model trained on historical fire-weather data  
- **Model Persistence**: Saved using `pickle`

---

## 🖥️ Tech Stack

### Backend
- Python
- Flask
- NumPy
- Scikit-learn

### Frontend
- HTML
- CSS (embedded styling)

### DevOps & Deployment
- Docker
- AWS EC2 (Ubuntu)
- Docker Desktop

---

## 📊 Input Features

| Feature | Description |
|------|------------|
| Temperature | Ambient temperature (°C) |
| RH | Relative Humidity (%) |
| Ws | Wind Speed (km/h) |
| Rain | Rainfall (mm) |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| ISI | Initial Spread Index |
| Classes | Fire occurrence (0 = No Fire, 1 = Fire) |
| Region | Region identifier (0 / 1) |

---

## 📁 Project Structure

Project/
│── app.py
│── Dockerfile
│── requirements.txt
│── README.md
│
├── models/
│ ├── ridge.pkl
│ └── scaler.pkl
│
└── templates/
├── home.html
└── index.html


---

## 🚀 Running the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd Project

2️⃣ (Optional) Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask App
python app.py


Open in browser:

http://127.0.0.1:5000

🐳 Running with Docker
1️⃣ Build Docker Image
docker build -t fwi-predictor .

2️⃣ Run Docker Container
docker run -p 5000:5000 fwi-predictor


Open in browser:

http://localhost:5000

☁️ AWS Deployment (EC2)

Instance Type: t2.micro (Free Tier)

OS: Ubuntu 22.04

Containerization: Docker

Exposed Port: 5000

Access the app using:

http://<EC2_PUBLIC_IP>:5000

💡 Key Features

End-to-end ML pipeline (training → inference)

User-friendly input guide with value ranges

Dockerized application for portability

Cloud deployment on AWS EC2

Beginner-friendly and scalable architecture

🧪 Future Enhancements

Input validation and error handling

Fire risk categorization (Low / Medium / High)

REST API support (JSON-based)

Production setup using Gunicorn + Nginx

CI/CD pipeline

HTTPS support

🧠 Interview Explanation (Short)

“I built a Flask-based machine learning web application that predicts Fire Weather Index using Ridge Regression. The model is containerized using Docker and deployed on AWS EC2, ensuring portability, scalability, and reproducibility.”

👤 Author

Aditya Raj Kaushik
Machine Learning & Software Development Enthusiast