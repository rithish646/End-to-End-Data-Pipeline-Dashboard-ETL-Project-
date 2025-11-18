import pandas as pd

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/sample_input.csv")
    df = transform_sales(df)
    print(df.head())
