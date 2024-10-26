import pandas as pd
import pytest


# Read the expected data from expected
df_expected = pd.read_json("expected/supplier_data.json")

# Read the actual  data from target
df_actual = pd.read_json("target/supplier_data_target.json")

# Compare the actual and expected data and mark the test cases as pass/fail

def test_compare_json_extraction():
    assert df_actual.equals(df_expected),"Actual data does not match with expected data"

if __name__ =="__main__":
    test_compare_csv_extraction()
