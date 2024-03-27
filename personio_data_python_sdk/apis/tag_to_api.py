import typing_extensions

from personio_data_python_sdk.apis.tags import TagValues
from personio_data_python_sdk.apis.tags.employees_api import EmployeesApi
from personio_data_python_sdk.apis.tags.absences_api import AbsencesApi
from personio_data_python_sdk.apis.tags.attendances_api import AttendancesApi
from personio_data_python_sdk.apis.tags.projects_api import ProjectsApi
from personio_data_python_sdk.apis.tags.custom_reports_api import CustomReportsApi
from personio_data_python_sdk.apis.tags.documents_api import DocumentsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.ABSENCES: AbsencesApi,
        TagValues.ATTENDANCES: AttendancesApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.CUSTOM_REPORTS: CustomReportsApi,
        TagValues.DOCUMENTS: DocumentsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.ABSENCES: AbsencesApi,
        TagValues.ATTENDANCES: AttendancesApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.CUSTOM_REPORTS: CustomReportsApi,
        TagValues.DOCUMENTS: DocumentsApi,
    }
)
