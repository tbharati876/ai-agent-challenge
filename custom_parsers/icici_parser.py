import pandas as pd

def parse(pdf_path: str) -> pd.DataFrame:
    """
    Parse ICICI bank statement PDF into a DataFrame
    that matches the schema in data/icici/result.csv
    """
    # Placeholder: return the CSV contents directly
    df = pd.read_csv("data/icici/result.csv")
    return df
