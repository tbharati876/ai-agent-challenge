import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from custom_parsers.icici_parser import parse

def test_icici():
    expected = pd.read_csv("data/icici/result.csv")
    actual = parse("data/icici/icici sample.pdf")  # space in filename
    assert actual.equals(expected)


