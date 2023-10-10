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
    with open(f"input/{properties.json_name}.json", "r", encoding="utf-8") as file:
        json_content = json.loads(file.read())

    copy_json_to_db(
        properties.json_name,
        properties.bulk_insert,
        properties.bulk_insert_heap,
        json_content,
    )
