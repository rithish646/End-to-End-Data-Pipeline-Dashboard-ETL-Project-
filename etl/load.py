import pandas as pd
from warehouse.postgres_client import engine

def load_to_postgres(df: pd.DataFrame, table_name="sales"):
    df.to_sql(table_name, engine, if_exists="append", index=False)

if __name__ == "__main__":
    df = pd.read_csv("data/sample_input.csv")
    df["revenue"] = df["quantity"] * df["unit_price"]
    load_to_postgres(df)
    print("Loaded successfully.")
