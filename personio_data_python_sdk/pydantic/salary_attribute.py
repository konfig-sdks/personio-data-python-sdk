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


class SalaryAttribute(BaseModel):
    attribute_id: typing.Optional[str] = Field(None, alias='attribute_id')

    data_type: typing.Optional[Literal["SALARY"]] = Field(None, alias='data_type')

    amount: typing.Optional[str] = Field(None, alias='amount')

    currency_symbol: typing.Optional[str] = Field(None, alias='currency_symbol')

    employee_id: typing.Optional[int] = Field(None, alias='employee_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
