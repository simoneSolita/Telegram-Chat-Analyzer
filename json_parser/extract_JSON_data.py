import re
from constants.constant import JSON_PROPERTY_FROM_ID, JSON_PROPERTY_MESSAGES, JSON_PROPERTY_FROM, \
    JSON_PROPERTY_DATE_UNIXTIME, UNKNOWN_ID, UNKNOWN_ID_NAME, JSON_PROPERTY_TEXT_ENTITIES, JSON_PROPERTY_TYPE, \
    JSON_PROPERTY_PLAIN, JSON_PROPERTY_SPOILER, JSON_PROPERTY_TEXT


def extract_user(message):
    if JSON_PROPERTY_FROM_ID in message:
        return message[JSON_PROPERTY_FROM_ID], message[JSON_PROPERTY_FROM]
    return UNKNOWN_ID, UNKNOWN_ID_NAME


def extract_sentence(message):
    date = message[JSON_PROPERTY_DATE_UNIXTIME]
    id_user = message[JSON_PROPERTY_FROM_ID] if JSON_PROPERTY_FROM_ID in message else UNKNOWN_ID
    sentence = ""
    entities = message[JSON_PROPERTY_TEXT_ENTITIES]
    for entity in entities:
        if entity[JSON_PROPERTY_TYPE] in [JSON_PROPERTY_PLAIN, JSON_PROPERTY_SPOILER]:
            sentence += entity[JSON_PROPERTY_TEXT] + " "
    sentence = re.sub(r'[^a-zA-Zà-úÀ-Ú ]', '', sentence).strip()
    return sentence, date, id_user


def extract_json_data(json_content):
    return json_content[JSON_PROPERTY_MESSAGES]
