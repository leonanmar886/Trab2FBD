import psycopg2
from dbConfig import db_config

def connect():
        conn = psycopg2.connect(
                        dbname=db_config['dbname'],
                        user=db_config['user'],
                        host=db_config['host'],
                        password=db_config['password']
                )

        context = conn.cursor()

        return conn, context

def disconnect(conn, context):
        context.close()
        conn.close()