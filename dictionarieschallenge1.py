# Challenge time!
# We have mentioned that the data for the Adventure game could be organised in many
# different ways.  We've created another way for you.
# Your mission, if you choose to accept it, is to
# change the code to make it work.
# Below is the the complete program from the last video, but with the
# locations dictionary modified so that everything is in a single dictionary.
# N.B. Yes the code has some errors, thats what you need to fix!

# Solution is in dictionarieschallenge12

locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }

# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
# namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
#               2: {"5": 5},
#               3: {"1": 1},
#               4: {"1": 1, "2": 2,},
#               5: {"2": 2, "1": 1}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "WEST": "W",
              "EAST": "E",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

loc = 1
while True:
    availableExits = ", ".join(locations[loc].keys())
    print(locations[loc]["exits"])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    # Parse the user input using vocabulary dictionary
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
    if direction in allExits:    # exits[loc] changed to allExits
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")