# coding: utf-8

"""
    Personnel Data

    API for reading and writing personnel data including data about attendances, absences, documents, etc

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from personio_data_python_sdk.pydantic.employees_list_attributes_response_data import EmployeesListAttributesResponseData

class EmployeesListAttributesResponse(BaseModel):
    success: typing.Optional[bool] = Field(None, alias='success')

    data: typing.Optional[EmployeesListAttributesResponseData] = Field(None, alias='data')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
