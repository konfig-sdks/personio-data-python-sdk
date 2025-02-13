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


class RequiredDefaultHistoricalAttribute(TypedDict):
    pass

class OptionalDefaultHistoricalAttribute(TypedDict, total=False):
    attribute_id: str

    data_type: str

    value: str

    employee_id: int

    effective_date: str

class DefaultHistoricalAttribute(RequiredDefaultHistoricalAttribute, OptionalDefaultHistoricalAttribute):
    pass
