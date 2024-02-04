"""
# TODO: add description
"""
from game_data import Player, Item, Instrument, TCard
from adventure import check_for_tcard


def music_puzzle(p: Player) -> None:
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

    if action.lower() == 'play an insrument':
        instrument = [item for item in p.inventory if isinstance(item, Instrument)]
        if len(instrument) != 0:
            instrument[0].play_instrument()

        else:
            print('Uh oh, you dont have any instruments in your bag!')

        if instrument[0].name == 'Harp':
            print('The guard starts to get sleepier, and slowly his eyes close and he begins to snore. '
                  '\nYou grab the shiny key from his belt and slip it into your pocket.')
            key = Item('Key', 2, 3, 5)
            p.inventory.append(key)

        else:
            print('The guard cringes at your attempts to serenade him and covers his ears with his hands.')
            print('Unfortunately, you have no chance at swiping his key.')


def talk_to_ta(p: Player) -> None:
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
        coffee = Item('coffee', 10, 12, 5)
    else:
        coffee = Item('coffee', 10, 12, 0)

    print('Do you want to bring this with you?: ')
    choice = input("\nEnter yes or no: ")

    while choice.lower() not in {'yes', 'no'}:
        choice = input("\nEnter yes or no: ")

    if choice.lower() == 'yes':
        if all(item.name != 'coffee' for item in p.inventory):
            p.inventory.append(coffee)

<<<<<<< HEAD

def music_puzzle(p: Player) -> None:
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

    if action.lower() == 'play an insrument':
        instrument = [item for item in p.inventory if isinstance(item, Instrument)]
        if len(instrument) != 0:
            instrument[0].play_instrument()

        else:
            print('Uh oh, you dont have any instruments in your bag!')

        if instrument[0].name == 'Harp':
            print('The guard starts to get sleepier, and slowly his eyes close and he begins to snore. '
                  '\nYou grab the shiny key from his belt and slip it into your pocket.')
            key = Item('Key', 2, 3, 5)
            p.inventory.append(key)

        else:
            print('The guard cringes at your attempts to serenade him and covers his ears with his hands.')
            print('Unfortunately, you have no chance at swiping his key.')

    
    def poster_puzzle(p:Player) -> None:
        """TODO: add description"""
        print('Which poster do you wanna examine?')
        print('T-card Info, T-card Info, Join the Fluff Buddies Club!, Midnight Magic Coffee Recipe')
        action = input("\nChoose one: ")
        if action.lower() in posters: