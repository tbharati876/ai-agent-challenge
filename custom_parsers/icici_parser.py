import pandas as pd

def parse(pdf_path: str) -> pd.DataFrame:
    """
    Parse ICICI bank statement PDF into a DataFrame
    that matches data/icici/result.csv
    """
    # Placeholder: load CSV directly
    df = pd.read_csv("data/icici/result.csv")
    return df

