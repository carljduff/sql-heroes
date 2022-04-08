import sys
sys.path.append("/workspace/sql-heroes")
from connection import *



# update_relationship = '''
# UPDATE relationships
# SET relationship_type_id = 2
# WHERE id = 1;
# '''
# update(update_relationship)

# update_relationship_1 = '''
# UPDATE relationships
# SET relationship_type_id = 2
# WHERE id = 2;
# '''

# update(update_relationship_1)

# add_superpower = """
# INSERT INTO ability_types(id, name)
# VALUES (default, 'Shapeshifting')
# """

# update(add_superpower)

#UPDATE HERO ABILITIES WITH NEW SHAPESHIFTING ABILITY

def alter_relationships():
    execute_query(
        """
        ALTER TABLE relationships
        ADD COLUMN 
        """
    )

def update_hero_name(new_name, original_name):
    update_name = """
    UPDATE heroes
    SET name = %s
    WHERE name = %s;
    """
    update = execute_query(update_name, (new_name, original_name))
    pprint(original_name + " was changed to " + new_name + "!")

# change_hero_name('NEWBIE2', 'Jordan')




def update_relationships(relationship_type_id, id):
    update_relationship = """
    UPDATE relationships
    SET relationship_type_id = %s
    WHERE id = %s
    """
    update = execute_query(update_relationship, (relationship_type_id, id))
    if relationship_type_id == 1:
        pprint('You are now friends! Hug!')
    elif relationship_type_id == 2:
        pprint('You are now foes! Attack!')

update_relationships(1, 2)

# update_relationship = '''
# UPDATE relationships
# SET relationship_type_id = 2
# WHERE id = 1;
# '''
# update(update_relationship)