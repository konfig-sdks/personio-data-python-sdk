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

from personio_data_python_sdk.type.absence import Absence
from personio_data_python_sdk.type.response import Response

AbsencePeriodsResponse = typing.Union[Response,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
AbsencePeriodsResponse = object
