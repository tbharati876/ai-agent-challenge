import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from custom_parsers.icici_parser import parse

def test_icici():
    #  Use the correct CSV filename
    expected = pd.read_csv("data/icici/result.csv")
    
    # Use the correct PDF filename (with space in the name)
    actual = parse("data/icici/icici sample.pdf")
    
    assert actual.equals(expected)



