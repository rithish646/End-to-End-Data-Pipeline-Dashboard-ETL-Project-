import pandas as pd

def extract_from_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

if __name__ == "__main__":
    df = extract_from_csv("data/sample_input.csv")
    print(df.head())
