import cc_dat_utils
import cc_classes
import json

# Creates and returns a cc_level_pack object(defined in cc_classes) from loaded json_data
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
        optional_fields = level["optional_fields"]

        for field in optional_fields:
            # title
            if field["type_val"] == 3:
                new_title_field = cc_classes.CCMapTitleField(field["byte_val"])
                new_level.add_field(new_title_field)

            # traps
            elif field["type_val"] == 4:
                traps = field["byte_val"]

                # list to store CCTrapControl objects
                traps_list = []
                # populate list with CCCloningMachineControl objects
                for trap in traps:
                    new_cc_trap_control = cc_classes.CCTrapControl(trap["bx"], trap["by"], trap["tx"], trap["ty"])
                    traps_list.append(new_cc_trap_control)

                new_cc_trap_controls_field = cc_classes.CCTrapControlsField(traps_list)
                new_level.add_field(new_cc_trap_controls_field)

            # machines
            elif field["type_val"] == 5:
                machines = field["byte_val"]

                # list to store CCCloningMachineControl objects
                machines_list = []
                # populate list with CCCloningMachineControl objects
                for machine in machines:
                    new_cc_cloning_machine_control = cc_classes.CCCloningMachineControl(machine["bx"], machine["by"],
                                                                                        machine["tx"], machine["ty"])
                    machines_list.append(new_cc_cloning_machine_control)

                new_cc_cloning_machine_controls_field = cc_classes.CCCloningMachineControlsField(machines_list)
                new_level.add_field(new_cc_cloning_machine_controls_field)

            # encoded password
            elif field["type_val"] == 6:
                new_password_field = cc_classes.CCEncodedPasswordField(field["byte_val"])
                new_level.add_field(new_password_field)

            # hint
            elif field["type_val"] == 7:
                new_hint_field = cc_classes.CCMapHintField(field["byte_val"])
                new_level.add_field(new_hint_field)

            # monsters
            elif field["type_val"] == 10:
                monsters = field["byte_val"]

                # list to store CCCoordinates of monsters
                monsters_list = []
                # populate list with CCCoordinates of monsters
                for monster in monsters:
                    new_cc_coordinate = cc_classes.CCCoordinate(monster["x"], monster["y"])
                    monsters_list.append(new_cc_coordinate)

                new_monster_field = cc_classes.CCMonsterMovementField(monsters_list)
                new_level.add_field(new_monster_field)

        # Add that level object to the cc_level_pack
        cc_level_pack.add_level(new_level)

        #print(new_level)
    ### End Add Code Here ###

    return cc_level_pack

#Part 3
#Load your custom JSON file
input_json_file = "data/rsookhoo_cc_level_pack.json"

#Convert JSON data to CCLevelPack
reader = open(input_json_file, "r")
json_data = json.load(reader)
new_cc_level_pack = make_cc_level_pack_from_json(json_data)

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(new_cc_level_pack, "data/rsookhoo_cc_level_pack.dat")