import sys
sys.path.insert(1, 'C:/Users/Lilit/Lilit/Study/Data_Engineering/Project/Github')
from conn import connect_to_db
from secrets import conn_params_dic
from collections import defaultdict
import pandas as pd
from datetime import datetime, timedelta
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
     
        transactions = defaultdict(list)

        for k in range (10):
            transactions['date'].append(datetime.now() - timedelta(days = 1))
            transactions['tenant_id'].append(np.random.choice(tenants['tenant_id'].unique()))
            transactions['property_id'].append(np.random.choice(properties['property_id'].unique()))
        transactions = pd.DataFrame(transactions)
        print(transactions)
        for i, row in transactions.iterrows():
            sql = 'INSERT INTO transactions (date, tenant_id, property_id) VALUES (%s,%s,%s)'
            cursor.execute(sql, tuple(row))
    conn.close()

lambda_handler()


