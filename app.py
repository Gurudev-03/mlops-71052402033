import os
import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")
MODEL_VERSION = os.environ.get("MODEL_VERSION", "1.0")
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    if request.method == "POST":
        try:
            study_hours = float(request.form["study_hours"])
            attendance = float(request.form["attendance"])
            internal_marks = float(request.form["internal_marks"])
            if not 0 <= study_hours <= 24:
                raise ValueError("Study hours must be between 0 and 24.")
            if not 0 <= attendance <= 100:
                raise ValueError("Attendance must be between 0 and 100.")
            if not 0 <= internal_marks <= 50:
                raise ValueError("Internal marks must be between 0 and 50.")
            result = int(model.predict(np.array([[study_hours, attendance, internal_marks]]))[0])
            prediction = "Pass" if result == 1 else "Fail"
        except (ValueError, KeyError):
            error = "Enter valid numbers. Study hours: 0–24, attendance: 0–100, marks: 0–50."
    return render_template("index.html", prediction=prediction, error=error, model_version=MODEL_VERSION)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
