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
from game_data import World, Instrument, Player
from puzzles import pick_instrument, music_puzzle, check_for_tcard, talk_to_ta, make_coffee

# Note: You may add helper functions, classes, etc. here as needed


def get_moves() -> list[str]:
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
        if locked_door():
            actions.remove('go west')

    if w.get_location(x, y).location_num == 6:
        if locked_lab():
            actions.remove('go south')

    return actions


def no_cheat_sheet() -> bool:
    """Returns True if the Player does not have their Cheat Sheet.
    """
    return not any(item.name == 'Cheat Sheet' for item in p.inventory)


def locked_door() -> bool:
    """Returns True if the Player does not have a Key in their inventory.
    This means the Bahen doors are locked and the Player cannot enter Bahen.
    """
    if not any(item.name == 'Key' for item in p.inventory):
        return True
    else:
        return False


def locked_lab() -> bool:
    """Returns True if the Player does not have their T-Card in their inventory.
    This means the CS lab doors are locked and the Player cannot enter the lab.
    """
    if not check_for_tcard(p):
        return True
    else:
        return False


def check_for_exam_items() -> bool:
    """Returns True if the Player has all the items they need for the exam (T-Card, Lucky Exam Pen, Cheat Sheet).
    """
    item_names = [item.name for item in p.inventory]
    if 'T-Card' not in item_names:
        return False

    elif 'Lucky Exam Pen' not in item_names:
        return False

    elif 'Cheat Sheet' not in item_names:
        return False

    return True


def pickup_desired_item(item: str) -> None:
    """Add the desired item to Player's inventory.
    """
    curr_location = w.get_location(p.x, p.y)
    for items in curr_location.available_items:
        if items.name == item:
            p.pickup_item(items, curr_location)


def menu_action(action: str) -> None:
    """Allows users to carry out a menu actions.
    """
    if action == 'look':
        print(f'{location.location_name} \n {location.long_descrip}')

    elif action == 'inventory':
        print(f'Inventory: {[item.name for item in p.inventory]}')
        if len([item.name for item in p.inventory]) > 0:
            print('Optional action: ["drop"]')

    elif action == 'score':
        print(f'Score: {p.score}')

    elif action == 'quit':
        p.victory = True


def already_have_instrument() -> None:
    """Let Player decide if they want to remove the instrument in their inventory to pick up a different one
    from the table. Drop the instrument if they enter yes or keep the one already in posession if they say no.
    """
    print('Oh no! You alread have an instrument with you. '
          'You only have 2 hands to use to play an instrument so you really do not need anymore.')

    print('Do you want to discard your current instrument?')
    decision = input("\nEnter yes or no: ")
    while decision.lower() not in {'yes', 'no'}:
        decision = input("\nEnter yes or no: ")

    if decision.lower() == 'yes':
        if any(i.name == 'Harmonica' for i in p.inventory):
            p.drop_item('Harmonica', location)
        elif any(i.name == 'Ukulele' for i in p.inventory):
            p.drop_item('Ukulele', location)
        else:
            p.drop_item('Harp', location)

        pickup_desired_item(pick_instrument(p, w))

    else:
        pass


def already_have_coffee(coffee_name: str) -> None:
    """Let Player decide if they want to remove the coffee in their inventory to nmake a different one.
    Drop the current coffee in their inventory  if they enter yes or keep the one already in posession if they say no.
    """
    print('Oh no! You already have a cup of coffee. You really dont need that much coffee...')
    print('Do you want to discard your other cup?')
    decision = input("\nEnter yes or no: ")

    while decision.lower() not in {'yes', 'no'}:
        decision = input("\nEnter yes or no: ")

    if decision.lower() == 'yes':
        for item in p.inventory:
            if item.name == coffee_name:
                p.drop_item(coffee_name, location)
                location.remove_item(item)
        make_coffee(p)

    else:
        pass


def get_cheat_sheet() -> None:
    """Allows the Player to approach TA to start the puzzle to obtain their Cheat Sheet.
    """
    print('Do you want to approach the TA?')
    action = input("\nEnter yes or no: ")

    while action.lower() not in {'yes', 'no'}:
        action = input("\nEnter yes or no: ")

    if action.lower() == 'yes':
        if talk_to_ta(p, w):
            pickup_desired_item('Cheat Sheet')


def get_key() -> None:
    """Allows the Player to approach the guard to start the puzzle to obtain the Key
    if they don't already have it.
    """
    if not any(item.name == 'Key' for item in p.inventory):
        if music_puzzle(p):
            pickup_desired_item('Key')

    else:
        print('You already took the Key from the guard. You should leave the poor guy alone')


def start_puzzle() -> None:
    """Runs the corresponding puzzles at a location (if any) when the Player moves to the spot.
    """
    if location.location_num == 1:
        if any(isinstance(i, Instrument) for i in p.inventory):
            already_have_instrument()

        else:
            pickup_desired_item(pick_instrument(p, w))

    elif location.location_num == 2:
        get_key()

    elif location.location_num == 10:
        if any(item.name == 'Coffee' for item in p.inventory):
            already_have_coffee('Coffee')

        elif any(item.name == 'Perfect coffee' for item in p.inventory):
            already_have_coffee('Perfect coffee')

        else:
            make_coffee(p)

    elif location.location_num == 12:
        if no_cheat_sheet():
            get_cheat_sheet()

        else:
            print('You already got your Cheat Sheet. You should let the tired TA have a break.')

    elif location.location_num == 5:
        print('Which poster do you wanna read?')
        print('1, 2, 3, 4')
        decision = input("\n Choose one: ")

        while decision not in ['1', '2', '3', '4']:
            print('There is no such poster.')
            decision = input("\n Choose one: ")

        print(w.items[decision].examine_poster())

    elif location.location_num == 11:
        available_items = [item.name for item in location.available_items]

        if 'T-Card' in available_items:
            pickup_desired_item('T-Card')
            print('You finally have your T-Card!')

    elif location.location_num == 7:
        available_items = [item.name for item in location.available_items]

        if 'Lucky Exam Pen' in available_items:
            pickup_desired_item('Lucky Exam Pen')
            print('You finally have your Lucky Exam Pen!')


# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['hashlib']
    })

    with open('map.txt') as map_file, open('locations.txt') as location_file, open('items.txt') as item_file:
        w = World(map_file, location_file, item_file)
    p = Player(2, 8)  # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit"]
    commands = ['drop', 'examine', 'pick up']
    move_count = 0

    while not p.victory and move_count <= 60:
        location = w.get_location(p.x, p.y)

        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)
        if location.first_visit is True:
            location.print_description()
            location.first_visit = False
            p.change_score(location.points)

        else:
            if location.location_num == 13 and check_for_exam_items():
                print('Hooray!! :) Thankfully, you managed to find all the items you need for your exam.')
                print('What have you learned from this experience?')
                print('Bahen has too many stairs. Oh, and you should be more careful with your belongings.')
                p.victory = True
                break

            start_puzzle()
            moves = get_moves()

            print("What to do? \n")
            print(f'menu: {menu}')
            print(f'available moves: {moves}')
            choice = input("\nEnter action: ")
            move_count += 1

            while choice.lower() not in menu and choice.lower() not in moves and choice.lower() not in commands:
                print('Uh oh, you cannot do that!')
                choice = input("\nEnter action: ")
                move_count += 1

            choice = choice.lower()

            if choice in menu:
                menu_action(choice)

            elif choice in moves:
                p.move(choice)
                loc = w.get_location(p.x, p.y)
                if loc.first_visit is False:
                    print(loc.short_descrip)

            elif choice == 'drop':
                item_name = input("Enter the name of the item to drop: ")
                p.drop_item(item_name, location)

            elif choice == "examine":
                item_name = input("Enter the number of the poster to examine: ")
                location.examine_item(item_name)

            elif choice == 'pick up':
                item_name = input("Enter the name of the item to pick up: ")
                p.pick_up(item_name, location)

    if move_count > 60:
        print('Uh oh! You are out of time! Looks like you will not be able to write your exam :(')
        print('Take this as a lesson to be more careful with your belongings.')
        print('GAME OVER')
        print(f'SCORE: {p.score}')

    if p.victory:
        print('GAME OVER')
        print(f'SCORE: {p.score}')
