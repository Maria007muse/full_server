import psycopg2

def create_tables():
    conn = psycopg2.connect(
        dbname='dbdeals',
        user='postgres',
        password='postgres',
        host='localhost'
    )
    cursor = conn.cursor()

    with open('db/schema.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())

    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(
        dbname='dbdeals',
        user='postgres',
        password='postgres',
        host='localhost'
    )
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM deals;')
    count = cursor.fetchone()[0]
    if count == 0:
        with open('db/data.sql', 'r', encoding='utf-8') as file:
            cursor.execute(file.read())

    conn.commit()
    conn.close()
