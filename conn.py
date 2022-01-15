import psycopg2
import sys
sys.path.insert(1, 'C:/Users/Lilit/Lilit/Study/Data_Engineering/Project/Github/')
from secrets import conn_params_dic, conn_params_warehouse_dic

def connect_to_db(instance_params: dict):
    """ Connect to the PostgreSQL database server """

    conn = None
    
    conn = psycopg2.connect(
            host=conn_params_dic['host'],
            port=conn_params_dic['port'],
            database=conn_params_dic['database'],
            user=conn_params_dic['user'],
            password=conn_params_dic['password']
        )
    print('Connected to DB')
    return conn

def connect_to_warehouse(instance_params: dict):
    """ Connect to the redshift warehouse """

    conn = None
    
    conn = psycopg2.connect(
            host = conn_params_warehouse_dic['host'],
            port = conn_params_warehouse_dic['port'],
            database = conn_params_warehouse_dic['database'],
            user = conn_params_warehouse_dic['user'],
            password = conn_params_warehouse_dic['password']
        )
    print('Connected to DB')
    return conn