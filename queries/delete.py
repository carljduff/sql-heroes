import sys
sys.path.append("/workspace/sql-heroes")
from connection import *


def delete_vehicles():
    execute_query("""
    DROP TABLE IF EXISTS
    super_vehicles""")

# delete_vehicles()

def delete_a_hero(name):
    delete_hero = """
    DELETE FROM heroes
    WHERE 
    heroes.name = %s;
    """
    delete = execute_query(delete_hero, [name]) # Ask about this <----------- [] --------- >
    pprint(name + ' was deleted!')

# https://access.crunchydata.com/documentation/psycopg2/2.7.4/usage.html
# delete_a_hero('Jordan3')



