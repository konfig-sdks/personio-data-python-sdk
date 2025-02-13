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

from personio_data_python_sdk.pydantic.error_details import ErrorDetails

class CustomReportsErrorResponse(BaseModel):
    status: typing.Optional[int] = Field(None, alias='status')

    trace_id: typing.Optional[str] = Field(None, alias='trace_id')

    timestamp: typing.Optional[datetime] = Field(None, alias='timestamp')

    errors: typing.Optional[typing.List[ErrorDetails]] = Field(None, alias='errors')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
