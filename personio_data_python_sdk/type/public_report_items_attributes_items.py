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

from personio_data_python_sdk.type.public_report_items_attributes_items_item import PublicReportItemsAttributesItemsItem

PublicReportItemsAttributesItems = typing.List[PublicReportItemsAttributesItemsItem]
