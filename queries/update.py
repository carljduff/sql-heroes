import sys
sys.path.append("/workspace/sql-heroes")
from connection import *

# add_vehicle = """ 
#     INSERT INTO super_vehicles(id, name, description, hero_id) 
#     VALUES (default, 'Blackbird', 'The Blackbird has an on-board Cerebro, used to find mutants, as well as an enhanced cloaking device that literally makes the Blackbird invisible. This cloak is perhaps one of the most recognizable traits of the Blackbird. While each Blackbird is a little different, they have been seen going deep underwater, far into space, and high altitudes on Earth.',
#     (SELECT id FROM heroes WHERE name='The Hummingbird'))
# """

# update(add_vehicle)

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