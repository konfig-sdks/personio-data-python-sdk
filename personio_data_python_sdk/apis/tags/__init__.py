# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from personio_data_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EMPLOYEES = "Employees"
    ABSENCES = "Absences"
    ATTENDANCES = "Attendances"
    PROJECTS = "Projects"
    CUSTOM_REPORTS = "Custom Reports"
    DOCUMENTS = "Documents"
