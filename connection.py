from psycopg import OperationalError, connect
from pprint import pprint


def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        connection = connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection



# Context managers - python
# open vs. closed to DBs - need to close
def select_all(query):
    # Connect to an existing database
    with create_connection("postgres", "postgres", "postgres") as conn:
        # Execute the query and fethc all records
        pprint(conn.execute(query).fetchall())
        return conn.execute(query).fetchall()

def select_one(query):
    # Connect to an existing database
    with create_connection("postgres", "postgres", "postgres") as conn:
        # Execute the query and fethc first record matching select
        pprint(conn.execute(query).fetchone())
        return conn.execute(query).fetchone()

def delete(query):
    # Connect to an existing database
    with create_connection("postgres", "postgres", "postgres") as conn:
        # Execute the query to delete
        conn.execute(query)
        # Commit the query to the database for reals
        conn.commit()
        pprint(conn.commit())

def create(query):
    with create_connection("postgres", "postgres", "postgres") as conn:
        conn.execute(query)
        conn.commit()
        pprint(conn.commit())

def update(query):
    with create_connection("postgres", "postgres", "postgres") as conn:
        conn.execute(query)
        conn.commit()
        pprint(conn.commit())
