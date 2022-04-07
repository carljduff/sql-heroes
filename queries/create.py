import sys
sys.path.append("/workspace/sql-heroes")
from connection import *

def create_vehicles():
    execute_query(""" CREATE TABLE IF NOT EXISTS super_vehicles(
        id int generated always as identity,
        name varchar,
        description varchar,
        hero_id int,
        PRIMARY KEY(id),
        FOREIGN KEY (hero_id)
        REFERENCES heroes(id))"""
    )

# create_vehicles()

def create_a_hero(name, about_me, biography):
    insert_hero = """ 
        INSERT INTO heroes(name, about_me, biography)
        VALUES(%s, %s, %s)
    """
    create = execute_query(insert_hero, (name, about_me, biography))
    pprint(name + " was created!")

# create_a_hero('Jordan3', 'I am ME', 'I\'m a superhero!')
