import typing_extensions

from personio_data_python_sdk.paths import PathValues
from personio_data_python_sdk.apis.paths.company_employees import CompanyEmployees
from personio_data_python_sdk.apis.paths.company_employees_employee_id import CompanyEmployeesEmployeeId
from personio_data_python_sdk.apis.paths.company_employees_employee_id_absences_balance import CompanyEmployeesEmployeeIdAbsencesBalance
from personio_data_python_sdk.apis.paths.company_employees_custom_attributes import CompanyEmployeesCustomAttributes
from personio_data_python_sdk.apis.paths.company_employees_attributes import CompanyEmployeesAttributes
from personio_data_python_sdk.apis.paths.company_employees_employee_id_profile_picture_width import CompanyEmployeesEmployeeIdProfilePictureWidth
from personio_data_python_sdk.apis.paths.company_attendances import CompanyAttendances
from personio_data_python_sdk.apis.paths.company_attendances_id import CompanyAttendancesId
from personio_data_python_sdk.apis.paths.company_attendances_projects import CompanyAttendancesProjects
from personio_data_python_sdk.apis.paths.company_attendances_projects_id import CompanyAttendancesProjectsId
from personio_data_python_sdk.apis.paths.company_time_off_types import CompanyTimeOffTypes
from personio_data_python_sdk.apis.paths.company_time_offs import CompanyTimeOffs
from personio_data_python_sdk.apis.paths.company_time_offs_id import CompanyTimeOffsId
from personio_data_python_sdk.apis.paths.company_absence_periods import CompanyAbsencePeriods
from personio_data_python_sdk.apis.paths.company_absence_periods_id import CompanyAbsencePeriodsId
from personio_data_python_sdk.apis.paths.company_document_categories import CompanyDocumentCategories
from personio_data_python_sdk.apis.paths.company_documents import CompanyDocuments
from personio_data_python_sdk.apis.paths.company_custom_reports_reports import CompanyCustomReportsReports
from personio_data_python_sdk.apis.paths.company_custom_reports_reports_report_id import CompanyCustomReportsReportsReportId
from personio_data_python_sdk.apis.paths.company_custom_reports_columns import CompanyCustomReportsColumns

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COMPANY_EMPLOYEES: CompanyEmployees,
        PathValues.COMPANY_EMPLOYEES_EMPLOYEE_ID: CompanyEmployeesEmployeeId,
        PathValues.COMPANY_EMPLOYEES_EMPLOYEE_ID_ABSENCES_BALANCE: CompanyEmployeesEmployeeIdAbsencesBalance,
        PathValues.COMPANY_EMPLOYEES_CUSTOMATTRIBUTES: CompanyEmployeesCustomAttributes,
        PathValues.COMPANY_EMPLOYEES_ATTRIBUTES: CompanyEmployeesAttributes,
        PathValues.COMPANY_EMPLOYEES_EMPLOYEE_ID_PROFILEPICTURE_WIDTH: CompanyEmployeesEmployeeIdProfilePictureWidth,
        PathValues.COMPANY_ATTENDANCES: CompanyAttendances,
        PathValues.COMPANY_ATTENDANCES_ID: CompanyAttendancesId,
        PathValues.COMPANY_ATTENDANCES_PROJECTS: CompanyAttendancesProjects,
        PathValues.COMPANY_ATTENDANCES_PROJECTS_ID: CompanyAttendancesProjectsId,
        PathValues.COMPANY_TIMEOFFTYPES: CompanyTimeOffTypes,
        PathValues.COMPANY_TIMEOFFS: CompanyTimeOffs,
        PathValues.COMPANY_TIMEOFFS_ID: CompanyTimeOffsId,
        PathValues.COMPANY_ABSENCEPERIODS: CompanyAbsencePeriods,
        PathValues.COMPANY_ABSENCEPERIODS_ID: CompanyAbsencePeriodsId,
        PathValues.COMPANY_DOCUMENTCATEGORIES: CompanyDocumentCategories,
        PathValues.COMPANY_DOCUMENTS: CompanyDocuments,
        PathValues.COMPANY_CUSTOMREPORTS_REPORTS: CompanyCustomReportsReports,
        PathValues.COMPANY_CUSTOMREPORTS_REPORTS_REPORT_ID: CompanyCustomReportsReportsReportId,
        PathValues.COMPANY_CUSTOMREPORTS_COLUMNS: CompanyCustomReportsColumns,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COMPANY_EMPLOYEES: CompanyEmployees,
        PathValues.COMPANY_EMPLOYEES_EMPLOYEE_ID: CompanyEmployeesEmployeeId,
        PathValues.COMPANY_EMPLOYEES_EMPLOYEE_ID_ABSENCES_BALANCE: CompanyEmployeesEmployeeIdAbsencesBalance,
        PathValues.COMPANY_EMPLOYEES_CUSTOMATTRIBUTES: CompanyEmployeesCustomAttributes,
        PathValues.COMPANY_EMPLOYEES_ATTRIBUTES: CompanyEmployeesAttributes,
        PathValues.COMPANY_EMPLOYEES_EMPLOYEE_ID_PROFILEPICTURE_WIDTH: CompanyEmployeesEmployeeIdProfilePictureWidth,
        PathValues.COMPANY_ATTENDANCES: CompanyAttendances,
        PathValues.COMPANY_ATTENDANCES_ID: CompanyAttendancesId,
        PathValues.COMPANY_ATTENDANCES_PROJECTS: CompanyAttendancesProjects,
        PathValues.COMPANY_ATTENDANCES_PROJECTS_ID: CompanyAttendancesProjectsId,
        PathValues.COMPANY_TIMEOFFTYPES: CompanyTimeOffTypes,
        PathValues.COMPANY_TIMEOFFS: CompanyTimeOffs,
        PathValues.COMPANY_TIMEOFFS_ID: CompanyTimeOffsId,
        PathValues.COMPANY_ABSENCEPERIODS: CompanyAbsencePeriods,
        PathValues.COMPANY_ABSENCEPERIODS_ID: CompanyAbsencePeriodsId,
        PathValues.COMPANY_DOCUMENTCATEGORIES: CompanyDocumentCategories,
        PathValues.COMPANY_DOCUMENTS: CompanyDocuments,
        PathValues.COMPANY_CUSTOMREPORTS_REPORTS: CompanyCustomReportsReports,
        PathValues.COMPANY_CUSTOMREPORTS_REPORTS_REPORT_ID: CompanyCustomReportsReportsReportId,
        PathValues.COMPANY_CUSTOMREPORTS_COLUMNS: CompanyCustomReportsColumns,
    }
)
