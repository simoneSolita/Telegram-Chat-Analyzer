import tomllib

import pandas as pd

from classes.classes import Properties
from constants.constant import PROPERTIES_FILE, QUERY_TABLE_COLUMN_USER, QUERY_TABLE_COLUMN_SENTENCE, \
    QUERY_TABLE_COLUMN_SENTENCE_BY_CHUNK, QUERY_TABLE_COLUMN_SENTENCE_BY_USER
from db.database_manager import search_user, search_sentence, search_sentence_by_user


def initialize_properties():
    with open(PROPERTIES_FILE, "rb") as file:
        file_properties = tomllib.load(file)
    return Properties(file_properties)


def search_user_db(input_name):
    return pd.DataFrame(
        search_user(initialize_properties().json_name, input_name), columns=QUERY_TABLE_COLUMN_USER
    )


def search_sentence_db(input_name):
    return pd.DataFrame(
        search_sentence(initialize_properties().json_name, input_name), columns=QUERY_TABLE_COLUMN_SENTENCE_BY_CHUNK
    )


def search_sentence_by_user_db(input_name):
    return pd.DataFrame(
        search_sentence_by_user(initialize_properties().json_name, input_name),
        columns=QUERY_TABLE_COLUMN_SENTENCE_BY_USER
    )
