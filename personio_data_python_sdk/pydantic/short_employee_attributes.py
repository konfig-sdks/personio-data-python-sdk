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

from personio_data_python_sdk.pydantic.short_employee_attributes_email import ShortEmployeeAttributesEmail
from personio_data_python_sdk.pydantic.short_employee_attributes_first_name import ShortEmployeeAttributesFirstName
from personio_data_python_sdk.pydantic.short_employee_attributes_id import ShortEmployeeAttributesId
from personio_data_python_sdk.pydantic.short_employee_attributes_last_name import ShortEmployeeAttributesLastName

class ShortEmployeeAttributes(BaseModel):
    id: typing.Optional[ShortEmployeeAttributesId] = Field(None, alias='id')

    first_name: typing.Optional[ShortEmployeeAttributesFirstName] = Field(None, alias='first_name')

    last_name: typing.Optional[ShortEmployeeAttributesLastName] = Field(None, alias='last_name')

    email: typing.Optional[ShortEmployeeAttributesEmail] = Field(None, alias='email')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
