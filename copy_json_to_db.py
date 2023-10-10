import tomllib

import orjson

from classes.classes import Properties
from constants.constant import PROPERTIES_FILE
from manager.copy_manager import copy_json_to_db

if __name__ == "__main__":
    # Load properties
    with open(PROPERTIES_FILE, "rb") as file:
        file_properties = tomllib.load(file)
    properties = Properties(file_properties)

    # load JSON file
    with open(f"input/{properties.json_name}.json", "r", encoding="utf-8") as file:
        json_content = orjson.loads(file.read())

    copy_json_to_db(
        properties,
        json_content,
    )
