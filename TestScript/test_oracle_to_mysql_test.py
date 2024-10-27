import pandas as pd
import pytest
# for connection string
from sqlalchemy import create_engine
# for connecting oracle
import cx_Oracle

# Read from oracle as source system
oracle_engine = create_engine('''oracle+cx_oracle://system:admin@localhost:1521/xe''')

# Read from mysql as traget db
mysql_engine = create_engine('''mysql+pymysql://root:Admin%40143@localhost:3308/etlautomation''')

# Compare the actual and expected data and mark the test cases as pass/fail

def test_compare_oracleToMysql_extraction():
    query_oracle_src = '''select * from city'''
    query_mysql_tgt = '''select * from city'''

    df_oracle = pd.read_sql(query_oracle_src,oracle_engine)
    df_mysql = pd.read_sql(query_mysql_tgt, mysql_engine)
    assert df_mysql.equals(df_oracle),"Actual data does not match with expected data"

if __name__ =="__main__":
    test_compare_oracleToMysql_extraction()
