import psycopg2
from psycopg2.extras import execute_values
from contextlib import contextmanager 

@contextmanager
def get_db_connection(server, database, user, password, port):
    conn_string = f"host={server} dbname= {database} user={user} password= {password} port={port}"
    connection = psycopg2.connect(conn_string)
    try:
        yield connection.cursor()
    finally:
        connection.commit()
        if connection:
            connection.close()