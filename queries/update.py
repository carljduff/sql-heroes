import sys
sys.path.append("/workspace/sql-heroes")
from connection import *
from pprint import pprint


def add_superpower(name):
    add_superpower = """
    INSERT INTO ability_types(name)
    VALUES (%s)
    """
    add = execute_query(add_superpower, [name])
    pprint(name + ' is a new cool superpower!')

# add_superpower('Shapeshifting')




# def alter_relationships():
#     execute_query(
#         """
#         ALTER TABLE relationships
#         ADD COLUMN 
#         """
#     )

def update_hero_name(new_name, original_name):
    update_name = """
    UPDATE heroes
    SET name = %s
    WHERE name = %s;
    """
    update = execute_query(update_name, (new_name, original_name))
    pprint(original_name + " was changed to " + new_name + "!")

# change_hero_name('NEWBIE2', 'Jordan')





def friends(id):
    update_friendship = """
    UPDATE relationships
    SET relationship_type_id = 1
    WHERE id = %s
    """
    update = execute_query(update_friendship, [id])
    pprint('You are now friends! Hug!')

# friends(1)

def foes(id):
    update_foeship = """
    UPDATE relationships
    SET relationship_type_id = 2
    WHERE id = %s
    """
    update = execute_query(update_foeship, [id])
    pprint('You are now foes! Attack!')

# foes(1)




# ----------------- Made separate friend/foe methods------------------------------- # 

# def update_relationships(relationship_type_id, id):
    # update_relationship = """
    # UPDATE relationships
    # SET relationship_type_id = %s
    # WHERE id = %s
    # """
    # update = execute_query(update_relationship, (relationship_type_id, id))
    # if relationship_type_id == 1:
    #     pprint('You are now friends! Hug!')
#     elif relationship_type_id == 2:
        # pprint('You are now foes! Attack!')

# update_relationships(1, 2)