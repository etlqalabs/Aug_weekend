import pandas as pd
import pytest

@pytest.fixture()
def csv_file_path():
    return "../expected/sales_data.csv"

def test_DQ_checks_for_missing_values_file(csv_file_path):
    df = pd.read_csv(csv_file_path)
    duplicates  =  df.duplicated()
    duplicate_counts = duplicates.sum()
    assert duplicate_counts == 0 ," Pleae check why duplicat values in target"



