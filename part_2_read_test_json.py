import test_data
import json


# Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    # Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    games = json_data["games"]
    # Loop through the json_data
    for game in games:
        # Create a new Game object from the json_data by reading
        new_game = test_data.Game()
        #  title
        new_game.title = game["title"]
        #print(new_game.title)
        #  year
        new_game.year = game["year"]
        #print(new_game.year)
        #  platform (which requires reading name and launch_year)
        new_platform = test_data.Platform()
        new_platform.name = game["platform"]["name"]
        new_platform.launch_year = game["platform"]["launch_year"]
        new_game.platform = new_platform
        # Add that Game object to the game_library
        game_library.add_game(new_game)
    ### End Add Code Here ###

    return game_library


# Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
# Open the file specified by input_json_file
reader = open(input_json_file, "r")
# Use the json module to load the data from the file
json_data = json.load(reader)
# Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
new_game_library = make_game_library_from_json(json_data)
# Print out the resulting GameLibrary data using print()
print(new_game_library)
### End Add Code Here ###
