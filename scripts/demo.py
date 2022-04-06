# This is why you'll execute a series of SQL statements during demo day.
import sys
sys.path.append("/workspace/sql-heroes")
from connection import *

# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])




# test_one = 'SELECT * FROM heroes'
# select_all(test_one)

# create('CREATE TABLE super_vehicle(id int generated always as identity,  int, data text, PRIMARY KEY(id))')
# delete('DROP TABLE jordan')


# '''
# UPDATE relationships
# SET relationship_type_id = 2
# WHERE id = 1;
# '''

# '''
# UPDATE relationships
# SET relationship_type_id = 2
# WHERE id = 2;
# '''

# insert_script = '''INSERT INTO -tableName- (default, name, somestring, somenumber) VALUES (%s, %s, %s, %s)'''
# insert_values = [('Jordan', 'This is a string', 3), ('Duff', 'This is also a string', 4)]
# for record in insert_values:
#     curr.execute(insert_script, record)


# select_all('SELECT * FROM heroes')
# heroes = 'SELECT * FROM heroes'
# for name in heroes:
#     print(name)


select_all('SELECT * FROM heroes')
