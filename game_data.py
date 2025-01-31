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


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: The name of the item.
        - start_position: The location the item starts at.
        - target_position: The location the target needs to be deposited at.
        - target_points: The amount of points received for depositing item in correct location.

    Representation Invariants:
        - isinstance(self.name, str) and len(self.name) > 0
        - isinstance(self.start_position, int) and -1 <= self.start_position <= 13
        - isinstance(self.target_position, int) and -1 <= self.target_position <= 13
        - isinstance(self.target_points, int)

    """
    name: str
    start_position: int
    target_position: int
    target_points: int

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


class Instrument(Item):
    """A child class of the Item class that represents an instrument in our text adventure game world.
    """
    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        super().__init__(name, start, target, target_points)

    def play_instrument(self) -> None:
        """ Plays the instrument.
        """
        print('You play some random notes, hoping it sounds nice.')


class Poster(Item):
    """A child class of the Item class that represents a poster in our text adventure game world.
    """
    info: str

    def __init__(self, name: str, info: str) -> None:
        start = 5
        target = 5
        target_points = 0
        super().__init__(name, start, target, target_points)
        self.info = info

    def examine_poster(self) -> str:
        """Print full description of poster"""
        return self.info


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - location_name: The name of the location.
        - location_num: The number of the location on the map.
        - points: The points player earn for visiting the location
        - short_descrip: The short description of the location.
        - long_descrip: The long description of the location.
        - first_visit: A bool that stores True if this location has never been visited before. Otherwise, it's False.
        - available_items: a list representing the Items present at the location.

    Representation Invariants:
        - isinstance(self.location_name, str) and len(self.location_name) > 0
        - isinstance(self.location_num, int) and -1 <= self.location_num <= 13
        - isinstance(self.short_descrip, str) and len(self.short_descrip) > 0
        - isinstance(self.long_descrip, str) and len(self.long_descrip) > 0
        - isitance(self.first_visit, bool)
        - all(isinstance(item, Item) for item in self.available_items)
    """
    location_name: str
    location_num: int
    points: int
    short_descrip: str
    long_descrip: str
    first_visit: bool
    available_items: Optional[list]

    def __init__(self, name: str, num: int, points: int, short: str, long: str, items: Optional[list] = None) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """
        self.location_name = name
        self.location_num = num
        self.points = points
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
        """Prints the name and description of the location.
        The long description is printed if it's the Player's first time visiting.
        Otherwise, the short descriptoin is printed.
        """
        if self.first_visit:
            print(f'{self.location_name} \n {self.long_descrip}')

        else:
            print(f'{self.location_name} \n {self.short_descrip}')

    def add_item(self, item: Item) -> None:
        """Add item to the location
        """
        self.available_items.append(item)

    def remove_item(self, item: Item) -> None:
        """Remove item from location.
        """
        self.available_items.remove(item)

    def examine_item(self, item_name: str) -> Any:
        """Examines the poster by printing the info on the poster."""
        for item in self.available_items:
            if item.name == item_name:
                print(f"You examine the {item_name}. {item.info}")
                return
        print(f"There is no {item_name} here to examine.")


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: The x-coordinate of the Player's position on the map. This represents the column number.
        - y: The y-coordinate of the Player's position on the map. This represents the row number.
        - inventory: The Player's bag that contains Items to be used in the game.
        - victory: A bool representing if the player has won the game yet. The game ends when victory is True.
        - score: The Player's current score.

    Representation Invariants:
        - isinstance(self.x, int)
        - isinstance(self.y, int)
        - isinstance(self.inventory, list) and all(isinstance(item, Item) for item in self.inventory)
        - isinstance(self.victory, bool)
        - isinstance(self.score, int) and self.score >= 0
    """
    x: int
    y: int
    inventory: list[Item]
    victory: bool
    score: int

    def __init__(self, x: int, y: int) -> None:
        """Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.score = 0

    def move(self, direction: str) -> None:
        """
        Moves the Player across the map by updating the Player's x and y coordinates.
        """
        if direction == 'go north':
            self.x += 1
        elif direction == 'go east':
            self.y += 1
        elif direction == 'go south':
            self.x -= 1
        elif direction == 'go west':
            self.y -= 1

    def drop_item(self, item_name: str, location: Location) -> None:
        """Removes the item from the Player's iventory.
        """
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                location.add_item(item)
                print(f"You dropped {item_name.capitalize()}.")
                return
        print(f"You don't have {item_name} in your inventory.")

    def pickup_item(self, item: Item, location: Location) -> None:
        """Automatically picks up an item after finishing a puzzle without the need for user input.
        """
        self.inventory.append(item)
        location.remove_item(item)
        self.change_score(item.target_points)

    def pick_up(self, item_name: str, location: Location) -> Any:
        """Pick up an item at a location through user prompt
        """
        for item in location.available_items:
            if item_name.lower() == item.name.lower():
                print(f"Picked up {item_name.capitalize()}.")
                self.inventory.append(item)
                location.remove_item(item)
                return

        print("\nThere's no such thing here.")

    def change_score(self, points: int) -> None:
        """Updates the Player's current score.
        """
        self.score += points


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - locations: a dictionary that stores all the location information of the world
        - items: a dictionary that stores all the items information ow the world

    Representation Invariants:
        - all(isinstance(row, list) and all(isinstance(loc, int) for loc in row) for row in self.map)
        - all(loc == -1 or isinstance(loc, int) for row in self.map for loc in row)
        - isinstance(self.locations, dict) and all(isinstance(key, int) and isinstance(value, Location) for key, value
          in self.locations.items())
        - isinstance(self.items, dict) and all(isinstance(key, str) and isinstance(value, Item) for key, value in
          self.items.items())
        - isinstance(self.location_data, TextIO) and self.location_data.readable()
        - isinstance(self.items_data, TextIO) and self.items_data.readable()
    """
    map: list[list[int]]
    locations: dict[int, Location]
    items: dict[str, Item]

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
        self.locations = {}
        self.load_locations(location_data)
        self.items = {}
        self.load_items(items_data)

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

    def load_locations(self, locations_data: TextIO) -> None:
        """
        Store location from open file location_data as the location attribute of this object, as a dictionary like so:

        If location_data is a file containing the following text:
         LOCATION -1
         0
         That way is blocked.
         That way is blocked.
         END
        then load_location should assign this World object's location to be {-1: Location(-1, 0, That way is blocked.,
         That way is blocked.} ."""

        location_data = []
        for line in locations_data:
            line = line.strip()
            if line == "END":
                # Process the collected data for a location
                if len(location_data) >= 4:
                    location_num = location_data[0]
                    name = location_data[1]
                    points = location_data[2]
                    short_description = location_data[3]
                    long_description = location_data[4]
                    location_num = int(location_num)
                    points = int(points)

                    location = Location(name, location_num, points, short_description, long_description, [])
                    self.locations[location_num] = location

                # Reset data for the next location
                location_data = []
            else:
                location_data.append(line)

    def load_items(self, items_data: TextIO) -> None:
        """
        Store items from open file items_data as the items attribute of this object, as a dictionary like so:

        If items_data is a file containing the following text:
        12 13 10 Cheat Sheet
        then load_items should assign this World object's items to be {'Cheat Sheet': Item('Cheat Sheet', 12, 13, 10)}

        If items_data is a file containing the following text:
        i 1 2 5 Harp
        then load_items should assign this World object's items to be {'Harp': Instrument('Harp', 1, 2, 5)}

        If items_data is a file containing the following text:
        p 3 Join The Fluff Buddies Club! Calling all animal lovers! Embark on a journey of cuteness and camaraderie with
         the Fluff Buddies Club!
        then load_items should assign this World object's items to be {'3': Poster('3', 5,5,0, "Join The Fluff Buddies
        Club! Calling all animal lovers! Embark on a journey of cuteness and camaraderie with the Fluff Buddies Club!")}

        """

        for line in items_data:
            line = line.split()
            if line[0] == 'i':
                start_loc, target_loc, point = map(int, line[1:4])
                name = ' '.join(line[4:])
                item = Instrument(name, int(start_loc), int(target_loc), int(point))
                self.locations[int(start_loc)].add_item(item)
                self.items[name] = item
            elif line[0] == 'p':
                name = line[1]
                info = ' '.join(line[2:])
                item = Poster(name, info)
                self.locations[5].add_item(item)
                self.items[name] = item
            else:
                start_loc, target_loc, point = map(int, line[:3])
                name = ' '.join(line[3:])
                item = Item(name, int(start_loc), int(target_loc), int(point))
                self.locations[int(start_loc)].add_item(item)
                self.items[name] = item

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map,
        if a valid location exists at that position (the location_num is not -1). Otherwise, return None.
        """
        loc_num = self.map[y][x]
        if loc_num == -1:
            return None
        else:
            return self.locations[loc_num]


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['hashlib']
    })
