import sys
sys.path.insert(1, 'C:/Users/Lilit/Lilit/Study/Data_Engineering/Project/Github/')
from conn import connect_to_db
from secrets import conn_params_dic
from collections import defaultdict
import pandas as pd
import random
import psycopg2
from datetime import datetime, timedelta


def lambda_handler():
    conn = connect_to_db(conn_params_dic)
    with conn.cursor() as cursor:
        conn.autocommit = True
        sql = 'SELECT user_id FROM users;'
        users = pd.io.sql.read_sql_query(sql,  conn)
        users_id = users['user_id'].values.tolist()
        print('userids fetched')
        sql = "SELECT property_id FROM properties;"
        properties = pd.io.sql.read_sql_query(sql, conn)
        property_id = properties['property_id'].values.tolist()
     
        logs = defaultdict(list)

        for k in range (10):
            logs['user_id'].append(random.choices(users['user_id'], k = 1)[0])
            logs['property_id'].append(random.choices(properties['property_id'].unique(), k = 1)[0])
            logs['date'].append(datetime.now() - timedelta(days = 1))
        logs = pd.DataFrame(logs)
        print(logs)
        for i, row in logs.iterrows():
            sql = 'INSERT INTO logs (user_id, property_id, date) VALUES (%s,%s,%s)'
            cursor.execute(sql, tuple(row))
    conn.close()
    print('Database connection closed.')

lambda_handler()


