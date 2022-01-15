import sys
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import psycopg2.extras as extras
import pandas as pd
import create_data
from io import StringIO
import sql_script
import os
from conn import connect_to_db
from secrets import conn_params_dic



def copy_data_to_database(cursor, data: pd.DataFrame, table_name: str):

    buffer = StringIO()
    # Save dataframe to an in memory buffer
    data.to_csv(buffer, header=False, index=False)

    # print(f'Cursor position is index={buffer.tell()}')
    # Set the cursor position on index=0 in the file.
    buffer.seek(0)
    cursor.copy_from(buffer, table_name, sep=",", columns=data.columns)
    
    # print("Is the file closed?", buffer.closed)
    buffer.close()
    print(f"The {table_name} data has been successfully copied to the database.")

def create_fill_tables():
    conn = connect_to_db(conn_params_dic)
    with conn.cursor() as cursor:
        conn.autocommit = True
        
        # Create database structure
        commands = sql_script.commands
        for command in commands:
            cursor.execute(command)
       
        for name, data in sql_script.table_names.items():
            data = data
            copy_data_to_database(cursor=cursor, data=data, table_name=name)
    conn.close()
    print('Database connection closed.')


create_fill_tables()