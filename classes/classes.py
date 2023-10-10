from constants.constant import (
    PROPERTIES_FILE_BULK_INSERT,
    PROPERTIES_FILE_BULK_INSERT_HEAP,
    PROPERTIES_FILE_JSON_NAME,
)


class Properties:
    def __init__(self, file_properties):
        self.json_name = file_properties[PROPERTIES_FILE_JSON_NAME]
        self.bulk_insert = file_properties[PROPERTIES_FILE_BULK_INSERT]
        self.bulk_insert_heap = file_properties[PROPERTIES_FILE_BULK_INSERT_HEAP]
