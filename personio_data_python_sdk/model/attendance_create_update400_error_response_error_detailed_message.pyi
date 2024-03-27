# coding: utf-8

"""
    Personnel Data

    API for reading and writing personnel data including data about attendances, absences, documents, etc

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from personio_data_python_sdk import schemas  # noqa: F401


class AttendanceCreateUpdate400ErrorResponseErrorDetailedMessage(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['AttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem']:
            return AttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['AttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem'], typing.List['AttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AttendanceCreateUpdate400ErrorResponseErrorDetailedMessage':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'AttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem':
        return super().__getitem__(i)

from personio_data_python_sdk.model.attendance_create_update400_error_response_error_detailed_message_item import AttendanceCreateUpdate400ErrorResponseErrorDetailedMessageItem
