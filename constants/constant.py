PROPERTIES_FILE = "properties.toml"
PROPERTIES_FILE_GROUP_NAME = "group_name"

FILE_DB_NAME = "dizionario_telegram_"

JSON_PROPERTY_FROM_ID = "from_id"
JSON_PROPERTY_FROM = "from"
JSON_PROPERTY_MESSAGES = "messages"
JSON_PROPERTY_DATE_UNIXTIME = "date_unixtime"
JSON_PROPERTY_TEXT_ENTITIES = "text_entities"
JSON_PROPERTY_TYPE = "type"
JSON_PROPERTY_PLAIN = "plain"
JSON_PROPERTY_SPOILER = "spoiler"
JSON_PROPERTY_TEXT = "text"

UNKNOWN_ID = "unknown_id"
UNKNOWN_ID_NAME = "UNKNOWN USER"

QUERY_INSERT_TABLE_USER = "CREATE TABLE IF NOT EXISTS user(\
        id text PRIMARY KEY UNIQUE NOT NULL ,\
        name text NOT NULL\
            )"
QUERY_INSERT_TABLE_WORD = "CREATE TABLE IF NOT EXISTS sentence(\
        id integer  PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL ,\
        value text,\
        date integer,\
        id_user text\
            )"

QUERY_TABLE_PARAMETER_USER = "id, name"
QUERY_TABLE_PARAMETER_WORD = "value, date, id_user"
