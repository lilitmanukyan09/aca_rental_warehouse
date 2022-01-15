import sys
sys.path.insert(1, 'C:/Users/Lilit/Lilit/Study/Data_Engineering/Project/Github')
from conn import connect_to_db
from secrets import conn_params_dic
from collections import defaultdict
import pandas as pd
import psycopg2
import datetime
import numpy as np


def lambda_handler():
    conn = connect_to_db(conn_params_dic)
    with conn.cursor() as cursor:
        conn.autocommit = True
        sql = 'SELECT tenant_id FROM tenants;'
        tenants = pd.io.sql.read_sql_query(sql,  conn)
        tenant_id = tenants['tenant_id'].values.tolist()
        print('tenant_id fetched')
        sql = "SELECT property_id FROM properties;"
        properties = pd.io.sql.read_sql_query(sql, conn)
        property_id = properties['property_id'].values.tolist()

        sql = "SELECT * FROM stay;"
        stays = pd.io.sql.read_sql_query(sql, conn)
        stay = defaultdict(list)

        for k in range (1):
            stay['tenant_id'].append(np.random.choice(tenants['tenant_id'].unique()))
            stay['property_id'].append(np.random.choice(properties['property_id'].unique()))
            stay['start_date'].append(stays[stays['property_id'].isin(stay['property_id'])]['end_date'].max())
            stay['end_date'].append(datetime.datetime.strptime(str(stay['start_date'][0]), "%Y-%m-%d") + datetime.timedelta(days = 3))

        stay = pd.DataFrame(stay)
        print(stay)
        for i, row in stay.iterrows():
            sql = 'INSERT INTO stay (tenant_id, property_id, start_date, end_date) VALUES (%s,%s,%s,%s)'
            cursor.execute(sql, tuple(row))
    conn.close()
    print('Database connection closed.')

lambda_handler()


