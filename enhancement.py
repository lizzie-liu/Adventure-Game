def coffee_puzzle() -> None:
    """
    # TODO: add descriptionnnnnnnnnn
   """
    print("You step up to the counter and approach the rack of mugs. There's a pink, purple, and blue mug. \n"
          "Which mug do you pick?")
    colour = input("\nEnter a colour: ")
    while colour.lower() not in {'pink', 'purple', 'blue', 'none'}:
        print(f'Hm, there is no {colour} mug.')
        colour = input("\nEnter another colour: ")
    colour = colour.lower()
    print(f'You pick up the {colour} mug and dispense some of the piping hot coffee inside. \n'
          f'The dark roast scent smells heavenly, and you resist the urge to take a sip.')

    print('You then turn your attention to the containers of skimmed milk, 2% milk, and cream. \n '
          'Which container do you pick?')
    container = input("\nEnter choice: ")
    while container.lower() not in {'skimmed milk', '2% milk', 'cream'}:
        print(f'Hm, there are no containers of {container}.')
        container = input("\nEnter another choice: ")
    container = container.lower()
    print(f'You pick up the container of {container} and pour it into the mug. '
          f'The dark liquid transforms into a light brown.')

    print('You spot the small packets of sugar, honey, and salt. Which packet do you pick?')
    packet = input("\nEnter choice: ")
    while packet.lower() not in {'sugar', 'honey', 'salt'}:
        print(f'Hm, there are no packts of {packet}.')
        packet = input("\nEnter another choice: ")
    packet = packet.lower()
    print(f'You rip open the pack and dump the {packet} into the mug. \n'
          f'Then you grab a spoon and give the coffee a good mix.')
