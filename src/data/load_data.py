import pandas as pd

def load_data(path="data/expenses.csv"):
    df = pd.read_csv(path)

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Add useful features
    df["month"] = df["date"].dt.to_period("M").astype(str)
    df["day"] = df["date"].dt.day_name()

    return df


if __name__ == "__main__":
    df = load_data()
    print(df.head())