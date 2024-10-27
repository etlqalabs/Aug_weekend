import pandas as pd
import pytest

@pytest.fixture()
def csv_file_path():
    return "../expected/sales_data.csv"

def test_DQ_checks_for_missing_values_file(csv_file_path):
    df = pd.read_csv(csv_file_path)
    missing_value_count = df.isnull().sum().sum()/10
    missing_perc = missing_value_count*100
    assert missing_perc <75,"Please verify the target why there are missing values"

