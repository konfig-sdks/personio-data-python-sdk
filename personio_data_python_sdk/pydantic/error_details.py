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

from personio_data_python_sdk.pydantic.error_meta import ErrorMeta

class ErrorDetails(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    details: typing.Optional[str] = Field(None, alias='details')

    type: typing.Optional[str] = Field(None, alias='type')

    _meta: typing.Optional[typing.List[ErrorMeta]] = Field(None, alias='_meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
