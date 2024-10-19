from pymysql import connect
from sqlalchemy import create_engine
import pandas as pd
import cx_Oracle

mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/etlqalabsdb')
#mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/enterpriseretaildwh')

df_mysql = pd.read_sql("select * from employees",mysql_engine)
#print(df_mysql)

oracle_engine = create_engine('oracle+cx_oracle://system:admin@localhost:1521/xe')
myOracle_engine = oracle_engine.connect()
df_oracle = pd.read_sql("select * from employee",myOracle_engine)
#print(df_oracle)

df_result = pd.merge(df_mysql,df_oracle, left_on='id',right_on='eno',how='inner')
print(df_result)

