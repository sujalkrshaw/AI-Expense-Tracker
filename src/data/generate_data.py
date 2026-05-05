import pandas as pd
import random
from datetime import datetime, timedelta

categories = {
    "Food": ["Swiggy", "Zomato", "Restaurant", "Cafe"],
    "Transport": ["Uber", "Ola", "Metro", "Fuel"],
    "Shopping": ["Amazon", "Flipkart", "Myntra"],
    "Bills": ["Electricity", "Water Bill", "Internet", "Mobile Recharge"],
    "Entertainment": ["Netflix", "Movie", "Spotify"],
    "Health": ["Pharmacy", "Doctor"],
}

payment_methods = ["UPI", "Card", "Cash"]

def generate_data(n=200):
    data = []
    start_date = datetime(2026, 1, 1)

    for _ in range(n):
        category = random.choice(list(categories.keys()))
        description = random.choice(categories[category])

        amount = round(random.uniform(50, 2000), 2)
        amount = -amount  # expense

        date = start_date + timedelta(days=random.randint(0, 120))

        payment = random.choice(payment_methods)

        data.append([
            date.strftime("%Y-%m-%d"),
            description,
            amount,
            category,
            payment
        ])

    df = pd.DataFrame(data, columns=[
        "date", "description", "amount", "category", "payment_method"
    ])

    return df


if __name__ == "__main__":
    df = generate_data(300)
    df.to_csv("data/expenses.csv", index=False)
    print("✅ Dataset created: data/expenses.csv")