import os
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")

def main():
    # Reproducible synthetic sample data: study hours, attendance %, internal marks.
    rng = np.random.default_rng(42)
    n = 500
    study_hours = rng.uniform(0, 10, n)
    attendance = rng.uniform(30, 100, n)
    internal_marks = rng.uniform(0, 50, n)

    # Simple synthetic rule with a little noise to create a teaching/demo dataset.
    score = (study_hours * 4.0) + (attendance * 0.12) + (internal_marks * 0.65)
    labels = (score >= 48).astype(int)
    flip = rng.random(n) < 0.04
    labels[flip] = 1 - labels[flip]

    X = np.column_stack([study_hours, attendance, internal_marks])
    model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42, max_iter=1000))
    model.fit(X, labels)
    joblib.dump(model, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")

if __name__ == "__main__":
    main()
