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

from personio_data_python_sdk.pydantic.cost_center_historical_attribute import CostCenterHistoricalAttribute
from personio_data_python_sdk.pydantic.default_historical_attribute import DefaultHistoricalAttribute
from personio_data_python_sdk.pydantic.duration_historical_attribute import DurationHistoricalAttribute
from personio_data_python_sdk.pydantic.entity_historical_attribute import EntityHistoricalAttribute
from personio_data_python_sdk.pydantic.salary_historical_attribute import SalaryHistoricalAttribute

PublicHistoricalReportItemsAttributesItemsItemHistoricalAttributes = typing.List[typing.Union[typing.List[DefaultHistoricalAttribute], typing.List[EntityHistoricalAttribute], typing.List[DurationHistoricalAttribute], typing.List[CostCenterHistoricalAttribute], typing.List[SalaryHistoricalAttribute]]]
