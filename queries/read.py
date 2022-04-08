import sys
sys.path.append("/workspace/sql-heroes")
from connection import *
from pprint import pprint


def hero_names():
    print_me = execute_query(
        """
        SELECT name 
        FROM heroes 
        ORDER BY id ASC
        """
    ).fetchall()
    pprint(print_me)

# hero_names()

def hero_info(name):
    print_me = execute_query(
        """
        SELECT *
        FROM heroes
        WHERE name = %s
        """
    ).fetchone()
    pprint(print_me)

## try to update with actual friend names **********************************
# def friends():
#     print_me = execute_query(
#         """
#         SELECT name
#         FROM heroes h
#         WHERE EXISTS (SELECT hero1_id, hero2_id from relationships r WHERE r.hero1_id = h.id AND r.hero2_id = h.id AND r.relationship_type_id = 1)
#         """
#     ).fetchall()
#     pprint(print_me)

# friends()

friends_list = """
    SELECT h1.name, h2.name
    FROM relationships
    INNER JOIN heroes h1
    ON relationships.hero1_id = h1.id
    INNER JOIN heroes h2
    ON relationships.hero2_id = h2.id
    WHERE relationship_type_id = 1
    """
# execute_query(friends).fetchall()
pprint(execute_query(friends_list).fetchall())



