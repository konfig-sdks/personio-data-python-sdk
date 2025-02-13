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

from personio_data_python_sdk.type.performance_target import PerformanceTarget

class RequiredPerformanceTargetAttribute(TypedDict):
    pass

class OptionalPerformanceTargetAttribute(TypedDict, total=False):
    attribute_id: str

    data_type: str

    employee_id: int

    performance_targets: typing.List[PerformanceTarget]

class PerformanceTargetAttribute(RequiredPerformanceTargetAttribute, OptionalPerformanceTargetAttribute):
    pass
