import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Correct import (important)
from src.data.load_data import load_data


def train():
    # Load data
    df = load_data()

    # Features & target
    X = df["description"]
    y = df["category"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ML Pipeline
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=200))
    ])

    # Train model
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluation
    print("\n📊 Model Evaluation:\n")
    print(classification_report(y_test, y_pred))

    # SAFE SAVE (no error)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    model_dir = os.path.join(base_dir, "models")

    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, "expense_model.pkl")

    joblib.dump(model, model_path)

    print(f"\n✅ Model saved at: {model_path}")


if __name__ == "__main__":
    train()