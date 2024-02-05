"""
# TODO: add description
"""
from game_data import Player, Item, Instrument, Coffee, TCard, World
from adventure import check_for_tcard


def pick_instrument(p: Player, w: World) -> str:
    """
    Returns the name of the instrument the Player wants to play. The name returned is capitalized.
    """
    location = w.get_location(p.x, p.y)
    available_instruments = location.available_items

    print(f'Availble items: {[item.name for item in available_instruments]}')
    print('Which one would you like to try playing?')
    instrument = input("\nEnter the instrument name: ")

    while instrument.capitalize() not in {'Harp', 'Ukulele', 'Harmonica'}:
        print('You cannot do that!')
        instrument = input("\nEnter a choice: ")

    instrument = instrument.capitalize()

    return instrument

def music_puzzle(p: Player) -> bool:
    """
    # TODO: add description
    """
    print('As you approach the grumpy looking guard, he stares down at you, expressionless.\n'
          'You try to strike up a conversation but the guard ignore you, and lets out a yamn.\n'
          'What should you do?')
    print('[leave, play an instrument]')
    action = input("\nEnter action: ")

    while action.lower() not in {'leave', 'play an instrument'}:
        print('Hm, it looks like you cannot do that.')
        action = input("\nEnter action: ")

    if action.lower() == 'leave':
        p.x, p.y = 2, 8

    elif action.lower() == 'play an instrument' and not any(isinstance(item, Instrument) for item in p.inventory):
        print('Uh oh, you dont have any instruments in your bag!')
        print('You should go find one.')

    elif action.lower() == 'play an instrument':
        for item in p.inventory:
            if isinstance(item, Instrument):
                item.play_instrument()

        if check_for_harp(p):
            return True

    return False


def check_for_harp(p: Player) -> bool:
    """Checks if Player has the Harp in their inventory.
    """
    for item in p.inventory:
        if item.name == 'Harp':
            return True

    return False


def talk_to_ta(p: Player) -> bool:
    """
    # TODO
    """
    print('Do you want to approach the TA?')
    choice = input("\nEnter yes or no: ")

    while choice.lower() not in {'yes', 'no'}:
        choice = input("\nEnter yes or no: ")

    if choice.lower() == 'yes':
        if check_for_tcard(p):
            print('You approach the extremely tired looking TA. He doesnt even look up from his work. You ask '
                  'him if he has seen the cheat sheet you made earlier in this room, but the TA just yawns.'
                  '\n"If only I had a cup of honey coffee with skimmed milk in a pink mug..." '
                  'he mutters while typing away.')
        else:
            print('Hm, the TA will not talk to you thanks to the new rule.')
            return False

    if not any(isinstance(item, Coffee) for item in p.inventory):
        print('Hm you seem to have no coffee to offer the poor TA...')
        return False

    else:
        print('You happen to have a cup of coffee with you! You offer it to the tired TA.')
        if check_correct_coffee(p):
            print('The TA takes the coffee from your hands and takes a long sip.'
                  '\nHe closes his eyes and smiles, savouring the magnificent taste of his drink.')
            print('The TA looks rejuvenated. With a smile, he asks you what questions you have.')
            print('You ask him if he has seen you Cheat Sheet. '
                  '\nThe TA nods, reaches into his bag, and pulls out a sheet of lined paper filled with scribbles.')
            print('You finally found your Cheat Sheet!')
            return True

        else:
            print('The TA takes the coffee from your hands and takes a long sip. '
                  '\nHis eyebrows furrow and he looks down and frowns at his coffee.')
            print('The TA still looks very tired and seems to have no energy to talk to you.')

    return False


def check_correct_coffee(p: Player) -> bool:
    """Checks if Player has the correct Coffee object in their inventory.
        """
    for item in p.inventory:
        if item.name == 'perfect coffee':
            return True

    return False


def make_coffee(p: Player) -> None:
    """
    # TODO: add descriptionnnnnnnnnn
   """
    print("You step up to the counter and approach the rack of mugs. There's a pink, purple, and blue mug. \n"
          "Which mug do you pick?")
    colour = input("\nEnter a colour: ")
    while colour.lower() not in {'pink', 'purple', 'blue'}:
        print(f'Hm, there is no {colour} mug.')
        colour = input("\nEnter another colour: ")
    colour = colour.lower()
    print(f'You pick up the {colour} mug and dispense some of the piping hot coffee inside. \n'
          f'The dark roast scent smells heavenly, and you resist the urge to take a sip.')

    print('You then turn your attention to the containers of skimmed milk, 2% milk, and cream.'
          'Which container do you pick?')
    container = input("\nEnter choice: ")
    while container.lower() not in {'skimmed milk', '2% milk', 'cream'}:
        print(f'Hm, there are no containers of {container}.')
        container = input("\nEnter another choice: ")
    container = container.lower()
    print(f'You pick up the container of {container} and pour it into the mug.'
          f'The dark liquid transforms into a light brown.')

    print('You spot the small packets of sugar, honey, and salt. Which packet do you pick?')
    packet = input("\nEnter choice: ")
    while packet.lower() not in {'sugar', 'honey', 'salt'}:
        print(f'Hm, there are no packts of {packet}.')
        packet = input("\nEnter another choice: ")
    packet = packet.lower()
    print(f'You rip open the pack and dump the {packet} into the mug. \n'
          f'Then you grab a spoon and give the coffee a good mix.')

    print('And voila! You now have a pipiing hot mug of coffee :)')

    if [colour, container, packet] == ['pink', 'skimmed milk', 'honey']:
        coffee = Item('perfect coffee', 10, 12, 5)
    else:
        coffee = Item('coffee', 10, 12, 0)

    print('Do you want to bring this with you?: ')
    choice = input("\nEnter yes or no: ")

    while choice.lower() not in {'yes', 'no'}:
        choice = input("\nEnter yes or no: ")

    if choice.lower() == 'yes':
        if all(item.name != 'coffee' for item in p.inventory):
            p.inventory.append(coffee)
