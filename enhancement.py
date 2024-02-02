def coffee_puzzle() -> None:
    """

   """
    print("You step up to the counter and approach the rack of mugs. There's a pink, purple, and blue mug. \n"
          "Which mug do you pick?")
    colour = input("\nEnter colour: ")

    while colour not in {'pink', 'purple', 'blue'}:
        colour = input("\nEnter colour: ")

    print(f'You pick up the {colour} mug and dispense some of the piping hot coffee inside. \n'
          f'You resist the urge to take a sip')

    print('You then turn your attention to the containers of skimmed milk, 2% milk, and cream. \n '
          'Which container do you pick?')
    container = input("\nEnter container: ")

    while container not in {''}


    # IGNORE capitalsssssssssssssssssss
