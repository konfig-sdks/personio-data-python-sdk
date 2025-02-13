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


class PublicAPIException(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CustomReportsErrorResponse']:
            return CustomReportsErrorResponse

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CustomReportsErrorResponse'], typing.List['CustomReportsErrorResponse']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PublicAPIException':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CustomReportsErrorResponse':
        return super().__getitem__(i)

from personio_data_python_sdk.model.custom_reports_error_response import CustomReportsErrorResponse
