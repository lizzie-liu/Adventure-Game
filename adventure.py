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

    if (w.get_location(x + 1, y)).num != -1:
        actions.append('Go east')

    elif (w.get_location(x, y + 1)).num != -1:
        actions.append('Go south')

    elif (w.get_location(x - 1, y)).num != -1:
        actions.append('Go west')

    elif (w.get_location(x, y - 1)).num != -1:
        actions.append('Go north')

    return actions

def check_for_tcard(p: Player) -> bool:
    """Checks if the Player has their TCard.
    """
    return any(isinstance(item, TCard) for item in p.inventory)

def get_puzzle(p: Player, w: World) -> None:
    """
    # TODO
    """
    location = w.get_location(p.x, p.y)
    puzzles = []

    if location.num == 2:
        puzzles.music_puzzle(p)

    elif location.num == 12:
        if check_for_tcard:
            talk_to_ta()

    elif location.num == 10:
        coffee_details = make_coffee
        print('Do you want to bring this with you?: ')
        choice = input("\nEnter yes or no: ")

        while choice.lower() not in {'yes', 'no'}:
            choice = input("\nEnter yes or no: ")

        if choice.lower() == 'yes':
            coffee = Item('coffee', 10, 12, 3)
            coffee = Item(coffee, 10, 12, 3)
            if coffee not in p.inventory:

            p.inventory.append(Item(coffee: str, start: int, target: int, target_points: int))


def pickup_items(player: Player) -> list[]:



# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
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
        moves = get_moves(p)
        print(f'available moves: {moves}')
        choice = input("\nEnter action: ")

        while choice.lower() not in (menu or moves):
            print('Uh oh, you cannot do that!')
            choice = input("\nEnter action: ")

        if choice == "[menu]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

        if choice.lower() == 'look':
            location.first_visit = True
            location.print_description()
            location.first_visit = False

        elif choice.lower() == 'inventory':
            print(p.inventory)

        elif choice.lower() == 'score':
            # NEED TO MAKE SCORE FNC
            print()

        elif choice.lower() == 'quit':
            print('GAME OVER')
            p.victory = True

        elif choice.lower() in moves:
            p.move(choice)



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
