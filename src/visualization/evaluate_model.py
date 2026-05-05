import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix, classification_report
from src.data.load_data import load_data


def evaluate():
    # Load data
    df = load_data()

    X = df["description"]
    y = df["category"]

    # Load trained model
    model = joblib.load("models/expense_model.pkl")

    # Predictions
    y_pred = model.predict(X)

    # Create outputs folder
    os.makedirs("outputs", exist_ok=True)

    # ==============================
    # 1. Confusion Matrix
    # ==============================
    cm = confusion_matrix(y, y_pred)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=model.classes_,
                yticklabels=model.classes_)

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.savefig("outputs/confusion_matrix.png")
    plt.show()

    # ==============================
    # 2. Classification Report
    # ==============================
    print("\n📊 Classification Report:\n")
    print(classification_report(y, y_pred))

    # ==============================
    # 3. Feature Importance (Top Words)
    # ==============================
    vectorizer = model.named_steps["tfidf"]
    classifier = model.named_steps["clf"]

    feature_names = vectorizer.get_feature_names_out()

    for i, category in enumerate(model.classes_):
        top10 = classifier.coef_[i].argsort()[-10:]

        print(f"\n🔥 Top words for {category}:")
        for j in top10:
            print(feature_names[j])

    print("\n✅ Visualization completed. Images saved in /outputs")


if __name__ == "__main__":
    evaluate()