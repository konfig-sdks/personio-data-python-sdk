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

from personio_data_python_sdk.type.absence_entitlement_value_item_attributes import AbsenceEntitlementValueItemAttributes

class RequiredAbsenceEntitlementValueItem(TypedDict):
    pass

class OptionalAbsenceEntitlementValueItem(TypedDict, total=False):
    type: str

    attributes: AbsenceEntitlementValueItemAttributes

class AbsenceEntitlementValueItem(RequiredAbsenceEntitlementValueItem, OptionalAbsenceEntitlementValueItem):
    pass
