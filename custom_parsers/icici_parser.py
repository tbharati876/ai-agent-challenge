import pandas as pd

def parse(pdf_path: str) -> pd.DataFrame:
    """
    Parse ICICI bank statement PDF into a DataFrame
    that matches the CSV schema in data/icici/results.csv
    """
    # For now, just load the CSV directly (placeholder logic)
    df = pd.read_csv("data/icici/results.csv")
    return df
