import tomllib

from classes.classes import Properties
from constants.constant import PROPERTIES_FILE
from db.database_manager import search_user, search_sentence


def initialize_properties():
    with open(PROPERTIES_FILE, "rb") as file:
        file_properties = tomllib.load(file)
    return Properties(file_properties)


def search_user_db(input_name):
    result = []
    for row in search_user(initialize_properties().json_name, input_name):
        result.append(*row + '\n')
    return result


def search_sentence_db(input_name):
    result = []
    for row in search_sentence(initialize_properties().json_name, input_name):
        result.append(*row + '\n')
    return result
