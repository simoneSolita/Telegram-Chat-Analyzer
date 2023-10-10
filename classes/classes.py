from constants.constant import PROPERTIES_FILE_GROUP_NAME, PROPERTIES_FILE_BULK_INSERT_HEAP, PROPERTIES_FILE_BULK_INSERT


class Properties:

    def __init__(self, file_properties):
        self.group_name = file_properties[PROPERTIES_FILE_GROUP_NAME]
        self.bulk_insert = file_properties[PROPERTIES_FILE_BULK_INSERT]
        self.bulk_insert_heap = file_properties[PROPERTIES_FILE_BULK_INSERT_HEAP]
