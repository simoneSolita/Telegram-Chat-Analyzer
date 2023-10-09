import json
import tomllib
import constants.constant
from classes import classes
from manager.copy_manager import copy_json_to_db

if __name__ == "__main__":
    # Load properties
    with open(constants.constant.PROPERTIES_FILE, "rb") as file:
        file_properties = tomllib.load(file)
    properties = classes.Properties(file_properties)

    # load JSON file
    with open(f"input/result_{properties.group_name}.json", "r", encoding="utf-8") as file:
        json_content = json.load(file)

    copy_json_to_db(properties.group_name, json_content)
