import joblib

model = joblib.load("models/expense_model.pkl")


def predict_category(text):
    return model.predict([text])[0]


if __name__ == "__main__":
    while True:
        text = input("\nEnter expense description (or type 'exit'): ").strip()

        # Exit condition
        if text.lower() == "exit":
            print("👋 Exiting...")
            break

        # Validation
        if text.isdigit():
            print("⚠️ Please enter a valid description, not just numbers.")
            continue

        if len(text) < 3:
            print("⚠️ Description too short. Try something like 'Swiggy order'.")
            continue

        # Prediction
        category = predict_category(text)
        print(f"✅ Predicted Category: {category}")