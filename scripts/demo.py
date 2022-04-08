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

friends_list = """
    SELECT h1.name, h2.name
    FROM relationships
    INNER JOIN heroes h1
    ON relationships.hero1_id = h1.id
    INNER JOIN heroes h2
    ON relationships.hero2_id = h2.id
    WHERE relationship_type_id = 1
    """

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
        '5: View Friends List \n'
        '6: Delete a hero \n')
    if prompt != '1' or '2' or '3' or '4' or '5' or '6':
        pprint('Please enter a valid choice.')
        demo()
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
        pprint(execute_query(friends_list).fetchall())
        demo()
    elif prompt == '6':
        name = input('Who are you? ')
        if name == input():
            pprint('Please try again with a valid name.')
            demo()
        else:
            choice = input('*** You are deleting your account. Are you sure? (y or n) *** ')
            if choice == 'y':
                delete_a_hero(name)
                pprint(name + ' has been deleted. Goodbye.')
                demo()
            elif choice == 'n':
                pprint('Thanks for staying!')
                demo()

demo()

    










