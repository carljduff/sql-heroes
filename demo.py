# This is why you'll execute a series of SQL statements during demo day.
from connection import select_all

# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])


# new_table = ("""
#             CREATE TABLE newtable (
#                 id serial PRIMARY KEY,
#                 num integer,
#                 data text)
#             """)


select_all('SELECT * FROM heroes')
create('CREATE TABLE jordan(id int generated always as identity, num int, data text, PRIMARY KEY(id))')



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


create_script = ''' CREATE TABLE IF NOT EXISTS jordan (
    id int generated always as identity
    name varchar NOT NULL,
    somestring varchar,
    somenumber int,
    PRIMARY KEY(id)
) '''

# insert_script = '''INSERT INTO -tableName- (default, name, somestring, somenumber) VALUES (%s, %s, %s, %s)'''
# insert_values = [('Jordan', 'This is a string', 3), ('Duff', 'This is also a string', 4)]
# for record in insert_values:
#     curr.execute(insert_script, record)

