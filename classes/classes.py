from constants.constant import PROPERTIES_FILE_GROUP_NAME


class Properties:

    def __init__(self, file_properties):
        self.group_name = file_properties[PROPERTIES_FILE_GROUP_NAME]
