import pandas as pd
import pytest
# for connection string
from sqlalchemy import create_engine
# for connecting oracle
import cx_Oracle


@pytest.fixture()
def connect_to_oracle_source():
    print("opening my connectiion for oracle")
    oracle_engine = create_engine('''oracle+cx_oracle://system:admin@localhost:1521/xe''')
    connection_oracle = oracle_engine.connect()
    yield connection_oracle
    print("closing my connectiion for oracle")
    connection_oracle.close()


@pytest.fixture()
def connect_to_mysql_target():
    print("opening my connection for mysql")
    mysql_engine = create_engine('''mysql+pymysql://root:Admin%40143@localhost:3308/etlautomation''')
    connection_mysql = mysql_engine.connect()
    yield connection_mysql
    print("closing my connectiion for mysql")
    connection_mysql.close()

# Compare the actual and expected data and mark the test cases as pass/fail

def test_compare_oracleToMysql_extraction(connect_to_oracle_source,connect_to_mysql_target):
    print(" My test begins....")
    query_oracle_src = '''select count(*) from city'''
    query_mysql_tgt = '''select count(*) from city'''

    df_oracle = pd.read_sql(query_oracle_src,connect_to_oracle_source)
    df_mysql = pd.read_sql(query_mysql_tgt, connect_to_mysql_target)
    count_oracle = df_oracle.iloc[0,0]
    count_mysql = df_mysql.iloc[0, 0]

    print(" The row count from source - oracle is : ",count_oracle)
    print(" The row count from target - mysql is : ", count_mysql)

    assert count_oracle == count_mysql ," Row count between source as target doesn match"



    print(" My test finishes....")