import tomllib
import toml

from constants.constant import PROPERTIES_FILE


def open_properties_file():
    with open(PROPERTIES_FILE, "rb") as file:
        file_properties = tomllib.load(file)
    return file_properties


def write_properties_file(properties):
    with open(PROPERTIES_FILE, "w") as file:
        toml.dump(properties, file)


def write_property(property_key, property_value):
    properties = open_properties_file()
    properties[property_key] = property_value
    write_properties_file(properties)
