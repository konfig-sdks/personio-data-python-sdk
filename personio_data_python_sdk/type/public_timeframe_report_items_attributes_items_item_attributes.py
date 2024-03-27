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

from personio_data_python_sdk.type.absence_overview_attribute import AbsenceOverviewAttribute
from personio_data_python_sdk.type.absence_period_attribute import AbsencePeriodAttribute
from personio_data_python_sdk.type.compensation_attribute import CompensationAttribute
from personio_data_python_sdk.type.cost_center_attribute import CostCenterAttribute
from personio_data_python_sdk.type.default_attribute import DefaultAttribute
from personio_data_python_sdk.type.duration_attribute import DurationAttribute
from personio_data_python_sdk.type.entity_attribute import EntityAttribute
from personio_data_python_sdk.type.performance_kpi_attribute import PerformanceKpiAttribute
from personio_data_python_sdk.type.performance_target_attribute import PerformanceTargetAttribute
from personio_data_python_sdk.type.salary_attribute import SalaryAttribute

PublicTimeframeReportItemsAttributesItemsItemAttributes = typing.List[typing.Union[typing.List[DefaultAttribute], typing.List[EntityAttribute], typing.List[DurationAttribute], typing.List[CostCenterAttribute], typing.List[AbsenceOverviewAttribute], typing.List[AbsencePeriodAttribute], typing.List[PerformanceTargetAttribute], typing.List[PerformanceKpiAttribute], typing.List[SalaryAttribute], typing.List[CompensationAttribute]]]
