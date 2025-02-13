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


class RequiredProjectAttributes(TypedDict):
    pass

class OptionalProjectAttributes(TypedDict, total=False):
    name: str

    # Marks the availability of the project. The default value is false.
    active: bool

    created_at: str

    updated_at: str

class ProjectAttributes(RequiredProjectAttributes, OptionalProjectAttributes):
    pass
