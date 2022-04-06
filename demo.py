# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query

# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])


new_table = ("""
            CREATE TABLE duff (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)


execute_query(new_table)

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