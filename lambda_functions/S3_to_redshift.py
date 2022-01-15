from collections import defaultdict
import pandas as pd
import psycopg2
import datetime
import numpy as np
import boto3
from conn import conn_params_warehouse_dic, connect_to_warehouse

s3 = boto3.client('s3')

conn_params_dic = {
    "host"      : "rentalwarehouse.cwoiba8doqsq.eu-central-1.redshift.amazonaws.com",
    "database"  : "dev",
    "user"      : "lilit1996",
    "password"  : "Lilit1996",
    "port" : 5439
} 

def connect_to_db(instance_params: dict):
    """ Connect to the PostgreSQL database server """

    conn = None
    
    conn = connect_to_warehouse(conn_params_warehouse_dic)
    print('Connected to DB')
    return conn
    
def lambda_handler(event, context):
    conn = connect_to_db(conn_params_dic)
    with conn.cursor() as cursor:
        conn.autocommit = True
        tables =  ('stay',
                    'logs',
                    'transactions',
                    'availability',
                    'building_features',
                    'building_junction',
                    'city',
                    'community_features',
                    'community_junction',
                	'furnishing',
                    'lease_term',
                    'location',
                    'properties',
                    'property_features',
                    'property_junction',
                    'property_type',
                    'region',
                    'tenants',
                    'users'
                )
        
        for table in tables:
            
            copy_query = f"COPY {table} FROM 's3://acarentalwarehouse/{table}/{table}' iam_role 'arn:aws:iam::000441274275:role/service-role/AmazonRedshift-CommandsAccessRole-20220109T153101' FORMAT AS PARQUET;"
            cursor.execute(copy_query)
    conn.close()