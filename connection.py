import psycopg
from psycopg import OperationalError, connect
from pprint import pprint

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalsError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("postgres", "postgres", "postgres")

def execute_query(query, params = None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        return cursor
    except OperationalError as e:
        print(f"The error '{e}' occurred")

        ### READ ###
        """
        SELECT
            select_list
        FROM        
            table_name;
        """

        ### CREATE ###
        """
        CREATE TABLE [IF NOT EXISTS] table_name (
            column1 datatype(length) column_contraint,
            column2 datatype(length) column_contraint,
            column3 datatype(length) column_contraint,
            table_constraints
            );
        """

        ### UPDATE ###
        """
        UPDATE table_name
            SET column1 = value1,
            column2 = value2,
            WHERE condition;
        """

        ### DELETE ###
        """
        DROP TABLE [IF EXISTS] 
        table_name_1,
        table_name_2,
        [CASCADE | RESTRICT];
        """
