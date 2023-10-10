from tqdm import tqdm

from db.database_manager import (
    bulk_insert_sentences,
    bulk_insert_users,
    initialize_db,
    insert_sentence,
    insert_user,
)
from json_parser.extract_JSON_data import (
    extract_json_data,
    extract_sentence,
    extract_user,
)


def copy_json_to_db(json_name, bulk_insert, bulk_insert_heap, json_content):
    # Extract entities
    messages = extract_json_data(json_content)

    # initialize db
    initialize_db(json_name)

    # Insert into DB
    # if we want bulkInsert, put the property in the file and select how many rows
    if bulk_insert:
        for bulk_index in tqdm(range(0, len(messages), bulk_insert_heap)):
            # n_messages is always 'bulk_insert_heap' or less for the last bulk of messages
            n_messages = min(bulk_insert_heap, len(messages) - bulk_index)
            sentences = []
            users = []

            # Extract data
            for i in range(bulk_index, bulk_index + n_messages):
                message = messages[i]
                item_sentence = extract_sentence(message)
                if item_sentence[0].strip() != "":
                    sentences.append(item_sentence)
                    users.append(extract_user(message))

            # Insert data into db
            bulk_insert_sentences(json_name, sentences)
            bulk_insert_users(json_name, users)

    else:
        for message in tqdm(messages):
            item_sentence = extract_sentence(message)
            if item_sentence[0].strip() != "":
                insert_sentence(json_name, *item_sentence)
                insert_user(json_name, *extract_user(message))
