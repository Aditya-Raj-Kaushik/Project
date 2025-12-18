import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

with open("models/ridge.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predictdata", methods=["GET", "POST"])
def predictdata():
    if request.method == "POST":
        try:
            features = [
                float(request.form["Temperature"]),
                float(request.form["RH"]),
                float(request.form["Ws"]),
                float(request.form["Rain"]),
                float(request.form["FFMC"]),
                float(request.form["DMC"]),
                float(request.form["ISI"]),
                float(request.form["Classes"]),
                float(request.form["Region"])
            ]

            scaled_features = scaler.transform([features])
            prediction = model.predict(scaled_features)[0]

            return render_template(
                "index.html",
                result=round(float(prediction), 2)
            )

        except Exception as e:
            return render_template(
                "index.html",
                result=f"Error: {e}"
            )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
