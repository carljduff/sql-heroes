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

def hero_info(name):
    hero_info = """
        SELECT *
        FROM heroes
        WHERE name = %s
        """
    info = execute_query(hero_info, (name,)).fetchone()
    pprint(info)

def hero_names():
    print_me = execute_query(
        """
        SELECT name 
        FROM heroes 
        ORDER BY id ASC
        """
    ).fetchall()
    pprint(print_me)

def update_hero_name(new_name, original_name):
    update_name = """
    UPDATE heroes
    SET name = %s
    WHERE name = %s;
    """
    update = execute_query(update_name, (new_name, original_name))
    pprint(original_name + " was changed to " + new_name + "!")

def delete_a_hero(name):
    delete_hero = """
    DELETE FROM heroes
    WHERE 
    heroes.name = %s;
    """
    delete = execute_query(delete_hero, [name]) 



def demo():
    prompt = input("Hello, what would you like to do? \n"
        '1: Create a new hero \n'
        '2: View hero information \n'
        '3: See logged in heroes \n'
        '4: Change a hero name \n'
        '5: Delete a hero \n')
    if prompt == '1':
        name = input('Enter your hero name. ')
        about_me = input('Tell us about yourself. ')
        biography = input('What\'s your story? ')
        create_a_hero(name, about_me, biography)
        demo()
    elif prompt == '2':
        name = input('Which heroes information would you like? ')
        hero_info(name)
        demo()
    elif prompt == '3':
        hero_names()
        demo()
    elif prompt == '4':
        original_name = input('What is your name? ')
        new_name = input('Who are you now? ')
        update_hero_name(new_name, original_name)
        demo()
    elif prompt == '5':
        name = input('Who are you? ')
        choice = input('*** You are deleting your account. Are you sure? (y or n) *** ')
        if choice == 'y':
            delete_a_hero(name)
            pprint(name + ' has been deleted. Goodbye.')
            demo()
        elif choice == 'n':
            pprint('Thanks for staying!')
            demo()

demo()

    










