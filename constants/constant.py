PROPERTIES_FILE = "properties.toml"
PROPERTIES_FILE_JSON_NAME = "json_name"
PROPERTIES_FILE_BULK_INSERT = "bulk_insert"
PROPERTIES_FILE_BULK_INSERT_HEAP = "bulk_insert_heap"
PROPERTIES_FILE_ON_DB_CONFLICT_DELETE = "on_db_conflict_delete"


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
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL ,\
        value text,\
        date integer,\
        id_user text\
            )"
QUERY_FIND_USER = "SELECT * FROM user WHERE name LIKE '%{}%'"

QUERY_FIND_SENTENCE = "SELECT * FROM sentence WHERE value LIKE '%{}%'"

QUERY_ORDER_USER_BY_ACTIVITY = ("select u.name as Nome , Count(*) as conteggio from user as u,sentence as s WHERE "
                                "u.id=s.id_user Group by u.name ORDER BY COUNT(*) DESC")

QUERY_FIND_SENTENCES_BY_USER_NAME = ("select s.value as frase , u.name as utente , s.date as data "
                                     "from user as u,sentence as s WHERE u.id=s.id_user and u.name = '{}'")

QUERY_FIND_SENTENCE_DETAIL_BY_CHUNK = ("select s.value as frase , u.name as utente from user as u,sentence as s "
                                       "WHERE u.id=s.id_user AND s.value LIKE '%{}%'")

QUERY_TABLE_PARAMETER_USER = "id, name"
QUERY_TABLE_PARAMETER_WORD = "value, date, id_user"
