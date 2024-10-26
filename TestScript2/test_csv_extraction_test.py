import pandas as pd
import pytest


# Read the expected data from expected
df_expected = pd.read_csv("expected/sales_data.csv")

# Read the actual  data from target
df_actual = pd.read_csv("target/sales_data_Target.csv")

# Compare the actual and expected data and mark the test cases as pass/fail

def test_compare_csv_extraction():
    assert df_actual.equals(df_expected),"Actual data does not match with expected data"

def test_compare_csv_extractionDemo():
    assert df_actual.equals(df_expected),"Actual data does not match with expected data"
