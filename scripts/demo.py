# This is why you'll execute a series of SQL statements during demo day.
import sys
sys.path.append("/workspace/sql-heroes")
from connection import *


def create_a_hero(name, about_me, biography):
    insert_hero = """ 
        INSERT INTO heroes(name, about_me, biography)
        VALUES(%s, %s, %s)
    """
    create = execute_query(insert_hero, (name, about_me, biography))
    pprint(name + " was created!")

def create_input():
    name = input('Hello, what is your name?')
    about_me = input('Tell us about yourself.')
    biography = input('What\'s your story?')
    create_a_hero(name, about_me, biography)

create_input()



def demo():
    prompt = input("Hello, what would you like to do? \n"
        'Create a new hero \n'
        'See today\'s heroes \n'
        'Change a hero name \n'
        'Delete a hero \n')
    selection = prompt.lower()
    if selection == 'Create a new hero':
        print('Enter a hero name, a brief about me and biography in this order.')
        hero_info = input()
        create_a_hero(hero_info)
        demo()

# demo()

    










