# coding: utf-8

"""
    Personnel Data

    API for reading and writing personnel data including data about attendances, absences, documents, etc

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from personio_data_python_sdk.paths.company_attendances_projects.post import CreateProject
from personio_data_python_sdk.paths.company_attendances_projects_id.delete import DeleteProject
from personio_data_python_sdk.paths.company_attendances_projects.get import GetAll
from personio_data_python_sdk.paths.company_attendances_projects_id.patch import UpdateData
from personio_data_python_sdk.apis.tags.projects_api_raw import ProjectsApiRaw


class ProjectsApi(
    CreateProject,
    DeleteProject,
    GetAll,
    UpdateData,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectsApiRaw(api_client)
