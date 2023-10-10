from tqdm import tqdm

from db.database_manager import insert_user, initialize_db, insert_sentence, bulk_insert_sentences, bulk_insert_users
from json_parser import extract_JSON_data
from json_parser.extract_JSON_data import extract_user, extract_sentence


def copy_json_to_db(group_name, bulk_insert, bulk_insert_heap, json_content):
    # Extract entities
    messages = extract_JSON_data.extract_json_data(json_content)

    # initialize db
    initialize_db(group_name)

    # Insert into DB
    # if we want bulkInsert, put the property in the file and select how many rows
    if bulk_insert:
        users = []
        sentences = []
        i = 0
        for message in tqdm(messages):
            item_sentence = extract_sentence(message)
            if item_sentence[0].strip() != "":
                sentences.append([*item_sentence])
                users.append([*extract_user(message)])
                i += 1
                if bulk_insert_heap == i:
                    bulk_insert_sentences(group_name, sentences)
                    sentences = []
                    bulk_insert_users(group_name, users)
                    users = []
                    i = 0

    else:
        for message in tqdm(messages):
            item_sentence = extract_sentence(message)
            if item_sentence[0].strip() != "":
                insert_sentence(group_name, *item_sentence)
                insert_user(group_name, *extract_user(message))
