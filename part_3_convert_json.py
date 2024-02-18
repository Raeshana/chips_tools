import cc_dat_utils
import cc_classes
import json

def make_cc_level_pack_from_json(json_data):
    # Initialize a new CCLevelPack
    cc_level_pack = cc_classes.CCLevelPack()

    ### Begin Add Code Here ###
    levels = json_data["levels"]

    # Loop through the json_data
    for level in levels:
        # Create a new Level object from the json_data by reading
        new_level = cc_classes.CCLevel()

        #  level_number
        new_level.level_number = level["level_number"]
        #print(new_level.level_number)

        # time
        new_level.time = level["time"]
        #print(new_level.time)

        # num_chips
        new_level.num_chips = level["num_chips"]
        #print(new_level.num_chips)

        # upper_layer
        new_level.upper_layer = level["upper_layer"]
        #print(new_level.upper_layer)

        # lower_layer
        new_level.lower_layer = level["lower_layer"]
        #print(new_level.lower_layer)

        # optional_fields
        # title
        new_level.optional_fields = level["optional_fields"]

        #new_cc_field = cc_classes.CCField()
        #new_cc_field.byte_val = level["optional_fields"]["byte_data"]
        #new_cc_field.type_val = level["optional_fields"]["type_val"]
        #new_level.add_field(new_cc_field)
        #print(new_level)

        # Add that Game object to the game_library
        cc_level_pack.add_level(new_level)

        print(new_level)
    ### End Add Code Here ###

    return cc_level_pack

#Part 3
#Load your custom JSON file
input_json_file = "data/rsookhoo_cc1.json"

#Convert JSON data to CCLevelPack
reader = open(input_json_file, "r")
json_data = json.load(reader)
new_cc_level_pack = make_cc_level_pack_from_json(json_data)

#Save converted data to DAT file
#cc_dat_utils.write_cc_level_pack_to_dat(cc_dat, dat_file)