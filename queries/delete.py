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
    delete = execute_query(delete_hero, (name,)) 
    pprint(name + ' was deleted!')

# delete_a_hero('')

def delete_vehicle(name):
    delete_vehicle = """
    DELETE FROM super_vehicles
    WHERE 
    name = %s;
    """
    delete = execute_query(delete_vehicle, (name,)) 
    pprint(name + ' was deleted!')

# delete_vehicle('Duff')


delete_relationship =   """
    DELETE FROM relationships
    WHERE 
    heroes.name = %s;
    """



## Come back to this later
## Something with parameters and strings
# def delete(table_name, column, column_value):
#     delete_statement = """
#     DELETE FROM %s
#     WHERE
#     %s = %s;
#     """
#     delete = execute_query(delete_statement, (table_name, column, column_value))
#     pprint(column_value + ' was deleted from' + table_name)

# delete(super_vehicles, name, 'Duff') 




# execute_query("""
# DELETE FROM ability_types
# WHERE 
# name = 'Shapeshifting'
# """)




















# https://access.crunchydata.com/documentation/psycopg2/2.7.4/usage.html
# https://stackoverflow.com/questions/58136769/typeerror-params-must-be-in-a-list-tuple-or-row-in-python





