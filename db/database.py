import psycopg2
from psycopg2.extras import RealDictCursor

def connect_to_database():
    conn = psycopg2.connect(
        dbname='dbdeals',
        user='postgres',
        password='postgres',
        host='localhost'
    )
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cursor


