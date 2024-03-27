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

from personio_data_python_sdk.type.type_enum import TypeEnum

class RequiredEmployeeHourlySalary(TypedDict):
    pass

class OptionalEmployeeHourlySalary(TypedDict, total=False):
    label: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    value: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    type: TypeEnum

    universal_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    currency: str

class EmployeeHourlySalary(RequiredEmployeeHourlySalary, OptionalEmployeeHourlySalary):
    pass
