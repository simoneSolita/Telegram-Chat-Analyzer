from tqdm import tqdm

from db.database_manager import insert_user, initialize_db, insert_sentence
from json_parser import extract_JSON_data
from json_parser.extract_JSON_data import extract_user, extract_sentence


def copy_json_to_db(group_name, json_content):
    # Extract entities
    messages = extract_JSON_data.extract_json_data(json_content)

    # initialize db
    initialize_db(group_name)

    # Insert into DB
    for message in tqdm(messages):
        item_sentence = extract_sentence(message)
        if item_sentence[0].strip() != "":
            insert_sentence(group_name, *item_sentence)
            insert_user(group_name, *extract_user(message))
