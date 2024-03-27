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

from personio_data_python_sdk.pydantic.public_report_attributes_columns import PublicReportAttributesColumns
from personio_data_python_sdk.pydantic.public_report_attributes_filters import PublicReportAttributesFilters

class PublicReportAttributes(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    # Report author
    author_first_name: typing.Optional[str] = Field(None, alias='author_first_name')

    # Report author
    author_last_name: typing.Optional[str] = Field(None, alias='author_last_name')

    type: typing.Optional[Literal["point_in_time", "historical_data", "timeframe"]] = Field(None, alias='type')

    status: typing.Optional[Literal["up_to_date", "updating", "update_failed"]] = Field(None, alias='status')

    start_date: typing.Optional[date] = Field(None, alias='start_date')

    end_date: typing.Optional[date] = Field(None, alias='end_date')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    data_refreshed_at: typing.Optional[datetime] = Field(None, alias='data_refreshed_at')

    columns: typing.Optional[PublicReportAttributesColumns] = Field(None, alias='columns')

    filters: typing.Optional[PublicReportAttributesFilters] = Field(None, alias='filters')

    period_type: typing.Optional[Literal["fixed", "today", "last_day_of_this_month", "this_year", "last_month", "last_thirty_days", "this_month", "year_to_date"]] = Field(None, alias='period_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
