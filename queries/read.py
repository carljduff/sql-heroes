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

## try to update with actual friend names **********************************
def friends():
    print_me = execute_query(
        """
        SELECT name
        FROM heroes h
        WHERE EXISTS (SELECT hero1_id, hero2_id from relationships r WHERE r.hero1_id = h.id AND r.hero2_id = h.id AND r.relationship_type_id = 1)
        """
    ).fetchall()
    pprint(print_me)

# friends()

