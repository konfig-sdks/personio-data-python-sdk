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


class EmployeesListAttributesResponseData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['EmployeesListAttributesResponseDataItem']:
            return EmployeesListAttributesResponseDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['EmployeesListAttributesResponseDataItem'], typing.List['EmployeesListAttributesResponseDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EmployeesListAttributesResponseData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'EmployeesListAttributesResponseDataItem':
        return super().__getitem__(i)

from personio_data_python_sdk.model.employees_list_attributes_response_data_item import EmployeesListAttributesResponseDataItem
