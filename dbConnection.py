import psycopg2
from dbConfig import db_config

def get_db_connection():
    try:
        return psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            host=db_config['host'],
            password=db_config['password'])
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
