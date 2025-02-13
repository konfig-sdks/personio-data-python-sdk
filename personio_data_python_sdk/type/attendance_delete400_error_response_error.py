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


class RequiredAttendanceDelete400ErrorResponseError(TypedDict):
    pass

class OptionalAttendanceDelete400ErrorResponseError(TypedDict, total=False):
    code: int

    message: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class AttendanceDelete400ErrorResponseError(RequiredAttendanceDelete400ErrorResponseError, OptionalAttendanceDelete400ErrorResponseError):
    pass
