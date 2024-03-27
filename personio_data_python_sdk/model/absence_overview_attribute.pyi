# coding: utf-8

"""
    Personnel Data

    API for reading and writing personnel data including data about attendances, absences, documents, etc

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from personio_data_python_sdk import schemas  # noqa: F401


class AbsenceOverviewAttribute(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            attribute_id = schemas.StrSchema
            
            
            class data_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ABSENCE_OVERVIEW(cls):
                    return cls("ABSENCE_OVERVIEW")
            start_date = schemas.DateSchema
            end_date = schemas.DateSchema
            duration_days = schemas.StrSchema
            duration_hours = schemas.StrSchema
            employee_id = schemas.IntSchema
            __annotations__ = {
                "attribute_id": attribute_id,
                "data_type": data_type,
                "start_date": start_date,
                "end_date": end_date,
                "duration_days": duration_days,
                "duration_hours": duration_hours,
                "employee_id": employee_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attribute_id"]) -> MetaOapg.properties.attribute_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_type"]) -> MetaOapg.properties.data_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_days"]) -> MetaOapg.properties.duration_days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_hours"]) -> MetaOapg.properties.duration_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_id"]) -> MetaOapg.properties.employee_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attribute_id", "data_type", "start_date", "end_date", "duration_days", "duration_hours", "employee_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attribute_id"]) -> typing.Union[MetaOapg.properties.attribute_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_type"]) -> typing.Union[MetaOapg.properties.data_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_days"]) -> typing.Union[MetaOapg.properties.duration_days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_hours"]) -> typing.Union[MetaOapg.properties.duration_hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_id"]) -> typing.Union[MetaOapg.properties.employee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attribute_id", "data_type", "start_date", "end_date", "duration_days", "duration_hours", "employee_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        attribute_id: typing.Union[MetaOapg.properties.attribute_id, str, schemas.Unset] = schemas.unset,
        data_type: typing.Union[MetaOapg.properties.data_type, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, date, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, date, schemas.Unset] = schemas.unset,
        duration_days: typing.Union[MetaOapg.properties.duration_days, str, schemas.Unset] = schemas.unset,
        duration_hours: typing.Union[MetaOapg.properties.duration_hours, str, schemas.Unset] = schemas.unset,
        employee_id: typing.Union[MetaOapg.properties.employee_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceOverviewAttribute':
        return super().__new__(
            cls,
            *args,
            attribute_id=attribute_id,
            data_type=data_type,
            start_date=start_date,
            end_date=end_date,
            duration_days=duration_days,
            duration_hours=duration_hours,
            employee_id=employee_id,
            _configuration=_configuration,
            **kwargs,
        )
