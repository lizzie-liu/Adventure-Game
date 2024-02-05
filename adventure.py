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
from game_data import World, Item, Instrument, Poster, TCard, Location, Player
from puzzles import *

# Note: You may add helper functions, classes, etc. here as needed


def get_moves(p: Player, w: World) -> list[str]:
    """Returns the valid spots the Player can move to based on their current location.
    """
    x, y = p.x, p.y
    actions = []

    if w.get_location(x + 1, y) is not None:
        actions.append('go north')

    if w.get_location(x, y + 1) is not None:
        actions.append('go east')

    if w.get_location(x - 1, y) is not None:
        actions.append('go south')

    if w.get_location(x, y - 1) is not None:
        actions.append('go west')

    # Check for locked doors
    if w.get_location(x, y).location_num == 3:
        if locked_door(p):
            actions.remove('go west')

    if w.get_location(x, y).location_num == 6:
        if locked_lab(p):
            actions.remove('go south')

    return actions

def locked_door(p: Player) -> bool:
    """Moves player back a step if they try to enter Bahen without a key in their inventory.
    """
    # x, y = p.x, p.y
    # location = w.get_location(p.x, p.y)
    #
    # if location.location_num == 3:
    #     if not any(item.name == 'Key' for item in p.inventory):
    #         print('The door wont budge... \nIt seems that you need a key to open it.')
    #         pass
    #
    #     else:
    #         print('You insert the key into the lock and slowly turn the key clockwise. '
    #               '*CLICK* *CLICK*  Hooray! You can now enter Bahen :)')
    #         p.move(choice)
    if not any(item.name == 'Key' for item in p.inventory):
        return True
    else:
        return False


def locked_lab(p: Player) -> bool:
    """Moves player back a step if they try to enter Bahen without a key in their inventory.
    """
    # x, y = p.x, p.y
    # location = w.get_location(p.x, p.y)
    #
    # if location.location_num == 6 and choice == 'go south':
    #     if not check_for_harp(p):
    #         print('The door wont budge... \nIt seems that you need your T-Card to open it.')
    #         pass
    #
    #     else:
    #         print('You swipe your T-Card in the scanner. '
    #               '*BEEP* *BEEP*  Hooray! You can now enter the CS Lab :)')
    #         p.move(choice)
    if not any(item.name == 'T-Card' for item in p.inventory):
        return True
    else:
        return False


def check_for_tcard(p: Player) -> bool:
    """
    Checks if the Player has their T-Card.
    """
    return any(item.name == 'T-Card' for item in p.inventory)


def check_for_cheat_sheet(p: Player) -> bool:
    """
    Checks if the Player has their Lucky Exam Pen.
    """
    return any(item.name == 'Lucky Exam Pen' for item in p.inventory)

def check_for_exam_items(p: Player) -> bool:
    """
    Checks if the Player has all the items they need for the exam (T-Card, Lucky Exam Pen, Cheat Sheet)
    """
    item_names = [item.name for item in p.inventory]
    if 'T-Card' not in item_names:
        return False

    elif 'Lucky Exam Pen' not in item_names:
        return False

    elif 'Cheat Sheet' not in item_names:
        return False

    return True


def pickup_desired_item(p: Player, w: World, item: str) -> None:
    """
    Add the desired item to Player's inventory.
    """
    location = w.get_location(p.x, p.y)

    for items in location.available_items:
        if items.name == item:
            p.pickup_item(items, location)


def start_puzzle(p: Player, w: World) -> None:
    """
    # TODO
    """
    location = w.get_location(p.x, p.y)

    if location.location_num == 1:
        if any(isinstance(item, Instrument) for item in p.inventory):
            print('Oh no! You alread have an instrument with you. '
                  'You only have 2 hands to use to play an instrument so you really do not need anymore.')
            print('Do you want to discard your current instrument?')
            choice = input("\nEnter yes or no: ")
            while choice.lower() not in {'yes', 'no'}:
                choice = input("\nEnter yes or no: ")

            if choice.lower() == 'yes':
                if any(item.name == 'Harmonica' for item in p.inventory):
                    p.drop_item('Harmonica', location)
                elif any(item.name == 'Ukulele' for item in p.inventory):
                    p.drop_item('Ukulele', location)
                else:
                    p.drop_item('Harp', location)
                pickup_desired_item(p, w, pick_instrument(p, w))

        else:
            pickup_desired_item(p, w, pick_instrument(p, w))

    elif location.location_num == 2:
        if not any(item.name == 'Key' for item in p.inventory):
            if music_puzzle(p):
                pickup_desired_item(p, w, 'Key')
        else:
            print('You already took the key from the guard. You should leave the poor guy alone')

    elif location.location_num == 10:
        if any((item.name == 'coffee' or item.name == 'perfect coffee')for item in p.inventory):
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
        if not check_for_cheat_sheet(p):
            print('Do you want to approach the TA?')
            choice = input("\nEnter yes or no: ")

            while choice.lower() not in {'yes', 'no'}:
                choice = input("\nEnter yes or no: ")

            if choice.lower() == 'yes':
                if talk_to_ta(p, w):
                    pickup_desired_item(p, w, 'Cheat Sheet')

    elif location.location_num == 5:
        available_posters = location.available_items
        print('Which poster do you wanna read?')
        print('T-card info, new rule, animal lover club, coffee recipe')
        choice = input("\n Choose one: ")

        while choice.lower() not in {'t-card info', 'new rule', 'animal lover club', 'coffee recipe'}:
            print('There is no such poster.')
            choice = input("\n Choose one: ")

        if choice.lower() == 't-card info':
            print(w.items['1'].examine_poster())
        elif choice.lower() == 'new rule':
            print(w.items['2'].examine_poster())
        elif choice.lower() == 'animal lover club':
            print(w.items['3'].examine_poster())
        else:
            print(w.items['4'].examine_poster())

        # if choice.lower() == 't-card info':
        #     poster_info = self.items['1'].examine_poster()
        #     print(poster_info)
        # elif choice.lower() == 'new rule':
        #     poster_info = self.items['2'].examine_poster()
        #     print(poster_info)
        #
        # elif choice.lower() == 'animal lover club':
        #     poster_info = self.items['3'].examine_poster()
        #     print(poster_info)
        # elif choice.lower() == 'coffee recipe':
        #     poster_info = self.items['4'].examine_poster()
        #     print(poster_info)
        # else:
        #     print('There is no such poster.')
        #     choice = input("\n Choose one: ")

    elif location.location_num == 11:
        available_items = [item.name for item in location.available_items]

        if 'T-Card' in available_items:
            pickup_desired_item(p, w, 'T-Card')
            print('You finally have your T-Card!')

    elif location.location_num == 7:
        available_items = [item.name for item in location.available_items]

        if 'Lucky Exam Pen' in available_items:
            pickup_desired_item(p, w, 'Lucky Exam Pen')
            print('You finally have your Lucky Exam Pen!')

    elif location.location_num == 13:
        if check_for_exam_items(p):
            print('Hooray!! :) Thankfully, you managed to find all the items you need for your exam.'
                  '\nWhat have you learned from this experience? '
                  '\nBahen has too many stairs. Oh, and you should be more careful with your belongings.')
            p.victory = True


def menu_action(p: Player, choice: str) -> None:
    """
    # TODO
    """
    location = w.get_location(p.x, p.y)

    if choice == 'look':
        print(f'{location.location_name} \n {location.long_descrip}')

    elif choice == 'inventory':
        print(f'Inventory: {[item.name for item in p.inventory]}')

    elif choice == 'score':
        # TODO NEED TO MAKE SCORE FNCC!!
        print(p.score)

    elif choice == 'quit':
        p.victory = True


# def use_inventory_item(p: Player) -> None:
#     """Allow Player to use item they select from their inventory.
#     """
#     print(f'Inventory: {[item.name for item in p.inventory]}')
#     name = input("\nEnter name of the item to use it or 'none': ")
#
#     while name.capitalize() not in {item.name for item in p.inventory}:
#         print('You do not have that in your bag!')
#         name = input("\nEnter name of the item to use it or 'none': ")
#
#     name = name.capitalize()
#
#     for item in p.inventory:
#         if item.name == name:
#             item_uses = item.item_uses
#             print(f'{name} uses: {item_uses}')
#
#             print('What would you like to do?')
#             action = input("\nEnter an action or 'none' to do nothing: ")
#
#             action = action.lower()
#
#             if action in item_uses:
#                 # i have no idea how to do this part
#                 carry_out_item_action(item, action)
#
#             elif action == 'none':
#                 print('You did not use the item.')
#
#             else:
#                 print('You cannot do that!')


# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = Player(2, 8)  # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit"]
    move_count = 0

    while not p.victory and move_count <= 600:
        location = w.get_location(p.x, p.y)

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)
        if location.first_visit is True:
            location.print_description()
            location.first_visit = False
        else:
            start_puzzle(p, w)
            moves = get_moves(p, w)

            print("What to do? \n")
            print(f'menu: {menu}')
            print(f'available moves: {moves}')
            choice = input("\nEnter action: ")
            move_count += 1

            while choice.lower() not in menu and choice.lower() not in moves:
                print('Uh oh, you cannot do that!')
                choice = input("\nEnter action: ")
                move_count += 1

            choice = choice.lower()

            if choice in menu:
                menu_action(p, choice)

            elif choice in moves:
                p.move(choice)
                loc = w.get_location(p.x,p.y)
                if loc.first_visit is False:
                    print(loc.short_descrip)


    if p.victory:
        print('GAME OVER')
        print(f'Score: {move_count}')


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
