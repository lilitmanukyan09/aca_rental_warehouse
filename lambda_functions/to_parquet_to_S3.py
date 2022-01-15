import boto3
import psycopg2
import pytz
import pandas as pd
from datetime import datetime, timedelta
from conn import conn_params_warehouse_dic, connect_to_warehouse

# ObjectName = str(datetime.now(pytz.timezone('Asia/Tbilisi'))).replace(' ', '_')
BucketName = 'acarentalwarehouse'

def put_object_to_S3(
	conn,
	client,
	tables: tuple
):
	for table in tables:
		sql = f"""
				SELECT * FROM {table}
				;
			   """
		frame = pd.io.sql.read_sql_query(sql,  conn)
		frame.to_parquet(
			f's3://{BucketName}/{table}/{table}',
			compression='brotli',
			engine='pyarrow',
			index=False
			)
	
def lambda_handler(event, context):
    conn = connect_to_warehouse(conn_params_warehouse_dic)
    s3_client = boto3.client('s3')
    
    transaction_tables = (
                    'stay',
                    'logs',
                    'transactions'
                )
    static_tables =  (
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
    put_object_to_S3(conn, s3_client, transaction_tables)
    put_object_to_S3(conn, s3_client, static_tables)
    return 0