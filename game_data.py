"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Any, Optional, TextIO


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - location_name: The name of the location.
        - num: The number of the location on the map.
        - position: This is a tuple representing the x, y coordinates of the location.
                    The x-coordinate is the column number and the y-coordinate is the row number.
        - long_descrip: The long description of the location.
        - short_descrip: The short description of the location.
        - first_visit: A bool that stores True if this location has never been visited before. Otherwise, it's False.
        - available_items: Items present at the location.

    Representation Invariants:
        - isinstance(self.location_name, str) and len(self.location_name) > 0
        - isinstance(self.location_num, int) and -1 <= self.location_num <= 13
        - isinstance(self.long_descrip, str) and len(self.long_descrip) > 0
        - isinstance(self.short_descrip, str) and len(self.short_descrip) > 0
        - isitance(self.first_visit, bool)
        - all(isinstance(item, Item) for item in self.available_items)
    """
    location_name: str
    num: int
    position: tuple[int, int]
    long_descrip: str
    short_descrip: str
    first_visit: bool
    available_items: Optional[list]

    def __init__(self, name: str, num: int, x: int, y: int, long: str, short: str, items: Optional[list] = None) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """
        self.location_name = name
        self.location_num = num
        self.position = (x, y)
        self.long_descrip = long
        self.short_descrip = short
        self.first_visit = True
        if items is not None:
            self.available_items = items

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

    def print_description(self) -> None:
        """
        Prints the name and description of the location.
        The long description is printed if it's the Player's first time visiting.
        Otherwise, the short descriptoin is printed.
        """
        if self.first_visit:
            print(f'{self.location_name} \n {self.long_descrip}')

        else:
            print(f'{self.location_name} \n {self.short_descrip}')

    # def available_actions(self, position: tuple[int, int], available_items: list[Item]) -> list[str]:
    #     """
    #     Return the available actions in this location.
    #     The actions should depend on the items available in the location
    #     and the x,y position of this location on the world map.
    #     """
    #
    #     # NOTE: This is just a suggested method
    #     # i.e. You may remove/modify/rename this as you like, and complete the
    #     # function header (e.g. add in parameters, complete the type contract) as needed
    #
    #     # TODO: Complete this method, if you'd like or remove/replace it if you're not using it
    #     x, y = position[0], position[1]
    #     actions = []
    #     # uh maybe do the checking for invalid spots on map in adventure.py
    #     # if map[y][x + 1] != -1:
    #     #     actions.append('Go east')
    #     #
    #     # elif map[y + 1][x] != 1:
    #     #     actions.append('Go south')
    #     #
    #     # elif map[y][x - 1] != 1:
    #     #     actions.append('Go west')
    #     #
    #     # elif map[y - 1][x] != 1:
    #     #     actions.append('Go north')
    #     #
    #     # return actions


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - item_name: The name of the item.
        - start_location: The location the item starts at.
        - target_location: The location the target needs to be deposited at.
        - target_points: The amount of points received for depositing item in correct location.

    Representation Invariants:
        - isinstance(self.item_name, str) and len(self.item_name) > 0
        - isinstance(self.start_location, int) and -1 <= self.start_location <= 13
        - isinstance(self.target_location, int) and -1 <= self.target_location <= 13
        - isinstance(self.target_points, int)

    """
    item_name: str
    start_location: int
    target_location: int
    target_points: int
    item_uses: list[str]

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points
        self.item_uses = ['Drop item']


class TCard(Item):
    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        super().__init__(name, start, target, target_points)
        self.item_uses = ['Drop item', 'Use T-Card']

    def use_card(self) -> None:
        """Uses the Player's T-Card."""
        print('You pull out your T-Card and try not to cringe at your id photo.')


class Instrument(Item):
    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        super().__init__(name, start, target, target_points)
        self.item_uses = ['Drop item', 'Play instrument']

    def play_instrument(self) -> None:
        """ Plays the instrument.
        """
        print('You play some random notes, hoping it sounds nice.')

class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: The x-coordinate of the Player's position on the map. This represents the column number.
        - y: The y-coordinate of the Player's position on the map. This represents the row number.
        - inventory: The Player's bag that contains Items to be used in the game.
        - victory: A bool representing if the player has won the game yet. The game ends when victory is True.

    Representation Invariants:
        - # TODO
    """
    x: int
    y: int
    inventory: list[Item]
    victory: bool

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False

    def move(self, direction: str) -> None:
        """
        Moves the Player across the map by updating the Player's x and y coordinates.
        """
        if direction == 'Go north':
            self.x += 1
        elif direction == 'Go east':
            self.y += 1
        elif direction == 'Go south':
            self.x -= 1
        elif direction == 'Go west':
            self.y -= 1

    def drop_item(self):
        """
        Removes the item from the Player's iventory.
        """



class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - # TODO add more instance attributes as needed; do NOT remove the map attribute

    Representation Invariants:
        - # TODO
    """
    map: list[list[int]]
    location:

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        f = map_data
        lst = []
        for line in f:
            lst = lst + [line.split()]

        integer_nested_list = [[int(item) for item in inner_list] for inner_list in lst]
        self.map = integer_nested_list
        return self.map

     def load_location(self)

    # TODO: Add methods for loading location data and item data (see note above).

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """

        # TODO: Complete this method as specified. Do not modify any of this function's specifications.
