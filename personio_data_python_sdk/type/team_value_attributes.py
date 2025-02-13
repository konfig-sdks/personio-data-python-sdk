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


class RequiredTeamValueAttributes(TypedDict):
    pass

class OptionalTeamValueAttributes(TypedDict, total=False):
    name: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class TeamValueAttributes(RequiredTeamValueAttributes, OptionalTeamValueAttributes):
    pass
