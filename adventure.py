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

def locked_door(p: Player, w: World, choice: str) -> None:
    """Moves player back a step if they try to enter Bahen without a key in their inventory.
    """
    x, y = p.x, p.y
    location = w.get_location(p.x, p.y)

    if location.location_num == 3 and choice == 'Go west':
        if not any(item.name == 'Key' for item in p.inventory):
            print('The door wont budge... \nIt seems that you need a key to open it.')

        else:
            print('You insert the key into the lock and slowly turn the key clockwise. '
                  '*CLICK* *CLICK*  Hooray! You can now enter Bahen :)')
            p.move(choice)


def check_for_tcard(p: Player) -> bool:
    """Checks if the Player has their TCard.
    """
    return any(isinstance(item, TCard) for item in p.inventory)


def pickup_desired_item(p: Player, w: World, item: str) -> None:
    """
    Add the desired item to Player's inventory.
    """
    location = w.get_location(p.x, p.y)

    for item in location.available_items:
        if item.name == item:
            p.pickup_item(item, location)


def start_puzzle(p: Player, w: World) -> None:
    """
    # TODO
    """
    location = w.get_location(p.x, p.y)

    if location.location_num == 1:
        available_instruments = location.available_items
        print(f'Availble items: {(item.name for item in available_instruments)}')
        print('')  # somehow print instruments available at location
        print('Which one would you like to try playing?')
        instrument = input("\nEnter the instrument name: ")

        while instrument.capitalize() not in {'Harp', 'Ukulele', 'Harmonica'}:
            print('You cannot do that!')
            instrument = input("\nEnter a choice: ")

        instrument = instrument.capitalize()

        if any(isinstance(item, Instrument) for item in p.inventory):
            print('Oh no! You alread have an instrument with you. '
                  'You only have 2 hands to use to play an instrument so you really do not need anymore.')

        else:
            pickup_desired_item(p, w, instrument)

    elif location.location_num == 2:
        if music_puzzle(p):
            pickup_desired_item(p, w, 'Key')


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

    elif location.location_num == 5:
        print('Which poster do you wanna read?')
        print('T-card info, new rule, animal lover club, coffee recipe')
        choice = input("\n Choose one: ")

        while choice not in {'T-card info', 'new rule', 'animal lover club', 'coffee recipe'}:
            print('Uh oh, that is not an option!')
            choice = input("\n Choose one: ")

        if choice.lower() == 't-card info':
            poster_info = self.items['1'].examine_poster()
            print(poster_info)
        elif choice.lower() == 'new rule':
            poster_info = self.items['2'].examine_poster()
            print(poster_info)

        elif choice.lower() == 'animal lover club':
            poster_info = self.items['3'].examine_poster()
            print(poster_info)
        elif choice.lower() == 'coffee recipe':
            poster_info = self.items['4'].examine_poster()
            print(poster_info)
        else:
            print('There is no such poster.')
            choice = input("\n Choose one: ")


    elif location.location_num ==



def menu_action(p: Player, choice: str) -> None:
    """
    # TODO
    """
    location = w.get_location(p.x, p.y)

    if choice == 'look':
        print(f'{location.location_name} \n {location.long_descrip}')

    elif choice == 'inventory':
        print(f'Inventory: {(item.name for item in p.inventory)}')
        action = input("\nEnter name of item to use it or None: ")

        while

    elif choice == 'score':
        # TODO NEED TO MAKE SCORE FNCC!!
        print(p.score)

    elif choice == 'quit':
        p.victory = True


def use_inventory_item(p: Player) -> None:
    """Allow Player to use item they select from their inventory.
    """
    print(f'Inventory: {(item.name for item in p.inventory)}')
    name = input("\nEnter name of the item to use it or None: ")

    while name.capitalize() not in {item.name for item in p.inventory}:
        print('You do not have that in your bag!')
        name = input("\nEnter name of the item to use it or None: ")

    name = name.capitalize()

    for item in p.inventory:
        if item.name == name:
            item_uses = item.item_uses
            print(f'{name} uses: {item_uses}')

            print('What would you like to do?')
            action = input("\nEnter an action or None to do nothing: ")

            if action in item_uses:
                item.

        while action.capitalize() not in item_uses:



def get_item_use(item: Item) -> str:
    """Return what Player wants to do with item.
    """
    print(f'Inventory: {(item.name for item in p.inventory)}')
    name = input("\nEnter name of the item to use it or None: ")

    while name.capitalize() not in {item.name for item in p.inventory}:
        print('You do not have that in your bag!')
        name = input("\nEnter name of the item to use it or None: ")

    name = name.capitalize()

    for item in p.inventory:
        if item.name == name:
            item_uses = item.item_uses
            print(f'{name} uses: {item_uses}')

            print('What would you like to do?')
            action = input("\nEnter an action or None to do nothing: ")



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
        if

        print(f'menu: {menu}')
        print(f'available moves: {moves}')
        choice = input("\nEnter action: ")

        while choice.lower() not in (menu or moves):
            print('Uh oh, you cannot do that!')
            choice = input("\nEnter action: ")

        choice = choice.lower()

        if choice in menu:
            menu_action(p, choice)

        elif choice in moves:
            locked_door(p, w, choice)
            p.move(choice)

    if p.victory:
        print('GAME OVER')
        print()  # TODO Print Player's score!!!!!!!!!!!!!




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
