import os
import sys
import subprocess
import importlib.util
import pandas as pd

MAX_ATTEMPTS = 3

def generate_parser(bank: str):
    """Generate a new parser file inside custom_parsers/"""
    parser_path = f"custom_parsers/{bank}_parser.py"

    # minimal parser template
    code = f'''
import pandas as pd

def parse(pdf_path: str) -> pd.DataFrame:
    # TODO: implement PDF parsing logic here
    # For now, return an empty DataFrame (just for testing structure)
    return pd.DataFrame()
    '''

    with open(parser_path, "w") as f:
        f.write(code)
    return parser_path

def run_test(bank: str) -> bool:
    """Run pytest for the bank parser"""
    try:
        subprocess.run(["pytest", "-q", f"tests/test_{bank}.py"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main(bank: str):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"\n Attempt {attempt} for {bank} parser...")

        parser_file = generate_parser(bank)
        print(f" Generated {parser_file}")

        if run_test(bank):
            print(" Tests passed! Parser is ready.")
            return
        else:
            print(" Tests failed, retrying...")

    print("Failed after max attempts.")

if __name__ == "__main__":
    if "--target" in sys.argv:
        bank = sys.argv[sys.argv.index("--target") + 1]
    else:
        bank = "icici"
    main(bank)
