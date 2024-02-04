"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Item, Instrument, TCard, Location, Player
from puzzles import *

# Note: You may add helper functions, classes, etc. here as needed


def get_moves(p: Player, w: World) -> list[str]:
    """Returns the valid spots the Player can move to based on their current location.
    """
    x, y = p.x, p.y
    actions = []

    if (w.get_location(x + 1, y)).location_num != -1:
        actions.append('Go east')

    elif (w.get_location(x, y + 1)).location_num != -1:
        actions.append('Go south')

    elif (w.get_location(x - 1, y)).location_num != -1:
        actions.append('Go west')

    elif (w.get_location(x, y - 1)).location_num != -1:
        actions.append('Go north')

    return actions


def check_for_tcard(p: Player) -> bool:
    """Checks if the Player has their TCard.
    """
    return any(isinstance(item, TCard) for item in p.inventory)


def start_puzzle(p: Player, w: World) -> None:
    """
    # TODO
    """
    location = w.get_location(p.x, p.y)

    if location.location_num == 1:
        #somehow print instruments available at location

    elif location.location_num == 2:
        music_puzzle(p)

    elif location.location_num == 3:
        if any(item.name != 'key' for item in p.inventory):
            print('The door wont budge... \nIt seems that you need a key to open it.')

        # TODO: add function in check for available moves where if no key, can't go north

    elif location.location_num == 10:
        if any(item.name == 'coffee' for item in p.inventory):
            print('Oh no! You already have a cup of coffee. You really dont need that much coffee...')
            print('Do you want to discard your other cup?')
            choice = input("\nEnter yes or no: ")

            while choice.lower() not in {'yes', 'no'}:
                choice = input("\nEnter yes or no: ")

            if choice.lower() == 'yes':
                p.drop_item('coffee', location)
                make_coffee(p)

        else:
            make_coffee(p)

    elif location.location_num == 12:
        print('Do you want to approach the TA?')
        choice = input("\nEnter yes or no: ")

        while choice.lower() not in {'yes', 'no'}:
            choice = input("\nEnter yes or no: ")

        if choice.lower() == 'yes':
            if check_for_tcard:
                talk_to_ta(p)
            else:
                print('Hm, the TA will not talk to you')



def menu(p: Player, location: Location, choice: str) -> None:
    """
    # TODO
    """
    location = w.get_location(p.x, p.y)

    if choice == 'look':
        print(f'{location.location_name} \n {location.long_descrip}')

    elif choice == 'inventory':
        print(f'Inventory: {(item.name for item in p.inventory)}')

    elif choice == 'score':
        # TODO NEED TO MAKE SCORE FNCC!!
        print(p.score)

    elif choice == 'quit':
        print('GAME OVER')
        p.victory = True


# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"), open("posters.txt"))
    p = Player(3, 9)  # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit"]

    while not p.victory:
        location = w.get_location(p.x, p.y)

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)
        location.print_description()
        location.first_visit = False

        print("What to do? \n")
        moves = get_moves(p, w)
        print(f'menu: {menu}')
        print(f'available moves: {moves}')
        choice = input("\nEnter action: ")

        while choice.lower() not in (menu or moves):
            print('Uh oh, you cannot do that!')
            choice = input("\nEnter action: ")

        choice = choice.lower()

        if choice in menu:
            menu(p, location, choice)

        elif choice in moves:
            p.move(choice)

    if p.victory:





        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
