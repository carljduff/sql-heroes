import sys
sys.path.append("/workspace/sql-heroes")
from connection import *
from pprint import pprint


# hero_names = """
# SELECT name
# FROM heroes
# """

# select_all(hero_names)

# friends = """
# SELECT hero1_id, hero2_id
# FROM relationships
# WHERE relationship_type_id = 1
# """



## try to update with actual friend names
def friends():
    print_me = execute_query(
        """
        SELECT name
        FROM heroes h
        WHERE EXISTS (SELECT hero1_id, hero2_id from relationships r WHERE r.hero1_id = h.id AND r.hero2_id = h.id AND r.relationship_type_id = 1)
        """
    ).fetchall()
    pprint(print_me)

friends()

