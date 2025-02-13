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


RequiredAttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem = TypedDict("RequiredAttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem", {
    })

OptionalAttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem = TypedDict("OptionalAttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem", {
    "success": bool,

    "error_msg": str,

    "id": typing.Optional[int],

    "employee": int,

    "date": str,

    "start_time": str,

    "end_time": str,

    "break": int,

    "comment": str,

    "project_id": typing.Optional[int],
    }, total=False)

class AttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem(RequiredAttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem, OptionalAttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem):
    pass
