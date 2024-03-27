# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from personio_data_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    COMPANY_EMPLOYEES = "/company/employees"
    COMPANY_EMPLOYEES_EMPLOYEE_ID = "/company/employees/{employee_id}"
    COMPANY_EMPLOYEES_EMPLOYEE_ID_ABSENCES_BALANCE = "/company/employees/{employee_id}/absences/balance"
    COMPANY_EMPLOYEES_CUSTOMATTRIBUTES = "/company/employees/custom-attributes"
    COMPANY_EMPLOYEES_ATTRIBUTES = "/company/employees/attributes"
    COMPANY_EMPLOYEES_EMPLOYEE_ID_PROFILEPICTURE_WIDTH = "/company/employees/{employee_id}/profile-picture/{width}"
    COMPANY_ATTENDANCES = "/company/attendances"
    COMPANY_ATTENDANCES_ID = "/company/attendances/{id}"
    COMPANY_ATTENDANCES_PROJECTS = "/company/attendances/projects"
    COMPANY_ATTENDANCES_PROJECTS_ID = "/company/attendances/projects/{id}"
    COMPANY_TIMEOFFTYPES = "/company/time-off-types"
    COMPANY_TIMEOFFS = "/company/time-offs"
    COMPANY_TIMEOFFS_ID = "/company/time-offs/{id}"
    COMPANY_ABSENCEPERIODS = "/company/absence-periods"
    COMPANY_ABSENCEPERIODS_ID = "/company/absence-periods/{id}"
    COMPANY_DOCUMENTCATEGORIES = "/company/document-categories"
    COMPANY_DOCUMENTS = "/company/documents"
    COMPANY_CUSTOMREPORTS_REPORTS = "/company/custom-reports/reports"
    COMPANY_CUSTOMREPORTS_REPORTS_REPORT_ID = "/company/custom-reports/reports/{report_id}"
    COMPANY_CUSTOMREPORTS_COLUMNS = "/company/custom-reports/columns"
