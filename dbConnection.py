import psycopg2
import os
from dbConfig import db_config

def get_db_connection():
    try:
        return psycopg2.connect(
            dbname=os.environ.get('DB_NAME', db_config['dbname']),
            user=os.environ.get('DB_USER', db_config['user']),
            host=os.environ.get('DB_HOST', db_config['host']),
            password=os.environ.get('DB_PASSWORD', db_config['password'])
        )
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
