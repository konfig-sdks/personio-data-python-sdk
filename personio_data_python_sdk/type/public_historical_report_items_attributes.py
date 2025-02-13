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

from personio_data_python_sdk.type.public_historical_report_items_attributes_columns import PublicHistoricalReportItemsAttributesColumns
from personio_data_python_sdk.type.public_historical_report_items_attributes_filters import PublicHistoricalReportItemsAttributesFilters
from personio_data_python_sdk.type.public_historical_report_items_attributes_items import PublicHistoricalReportItemsAttributesItems

class RequiredPublicHistoricalReportItemsAttributes(TypedDict):
    pass

class OptionalPublicHistoricalReportItemsAttributes(TypedDict, total=False):
    description: str

    id: str

    name: str

    # Report author
    author_first_name: str

    # Report author
    author_last_name: str

    type: str

    status: str

    start_date: datetime

    end_date: datetime

    created_at: datetime

    updated_at: datetime

    data_refreshed_at: datetime

    columns: PublicHistoricalReportItemsAttributesColumns

    filters: PublicHistoricalReportItemsAttributesFilters

    period_type: str

    items: PublicHistoricalReportItemsAttributesItems

class PublicHistoricalReportItemsAttributes(RequiredPublicHistoricalReportItemsAttributes, OptionalPublicHistoricalReportItemsAttributes):
    pass
