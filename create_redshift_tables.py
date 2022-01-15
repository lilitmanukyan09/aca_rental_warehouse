import Warehouse_structure
from conn import connect_to_warehouse
from secrets import conn_params_warehouse_dic

def create_redshift_tables():
    conn = connect_to_warehouse(conn_params_warehouse_dic)
    with conn.cursor() as cursor:
        conn.autocommit = True
        
        # Create database structure
        commands = Warehouse_structure.commands
        for command in commands:
            cursor.execute(command)
    

    conn.close()
    print('Warehouse connection closed.')


create_redshift_tables()