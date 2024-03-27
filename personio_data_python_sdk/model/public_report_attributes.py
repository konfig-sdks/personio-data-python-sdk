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


class PublicReportAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            id = schemas.StrSchema
            name = schemas.StrSchema
            author_first_name = schemas.StrSchema
            author_last_name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "point_in_time": "POINT_IN_TIME",
                        "historical_data": "HISTORICAL_DATA",
                        "timeframe": "TIMEFRAME",
                    }
                
                @schemas.classproperty
                def POINT_IN_TIME(cls):
                    return cls("point_in_time")
                
                @schemas.classproperty
                def HISTORICAL_DATA(cls):
                    return cls("historical_data")
                
                @schemas.classproperty
                def TIMEFRAME(cls):
                    return cls("timeframe")
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "up_to_date": "UP_TO_DATE",
                        "updating": "UPDATING",
                        "update_failed": "UPDATE_FAILED",
                    }
                
                @schemas.classproperty
                def UP_TO_DATE(cls):
                    return cls("up_to_date")
                
                @schemas.classproperty
                def UPDATING(cls):
                    return cls("updating")
                
                @schemas.classproperty
                def UPDATE_FAILED(cls):
                    return cls("update_failed")
            start_date = schemas.DateSchema
            end_date = schemas.DateSchema
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            data_refreshed_at = schemas.DateTimeSchema
        
            @staticmethod
            def columns() -> typing.Type['PublicReportAttributesColumns']:
                return PublicReportAttributesColumns
        
            @staticmethod
            def filters() -> typing.Type['PublicReportAttributesFilters']:
                return PublicReportAttributesFilters
            
            
            class period_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "fixed": "FIXED",
                        "today": "TODAY",
                        "last_day_of_this_month": "LAST_DAY_OF_THIS_MONTH",
                        "this_year": "THIS_YEAR",
                        "last_month": "LAST_MONTH",
                        "last_thirty_days": "LAST_THIRTY_DAYS",
                        "this_month": "THIS_MONTH",
                        "year_to_date": "YEAR_TO_DATE",
                    }
                
                @schemas.classproperty
                def FIXED(cls):
                    return cls("fixed")
                
                @schemas.classproperty
                def TODAY(cls):
                    return cls("today")
                
                @schemas.classproperty
                def LAST_DAY_OF_THIS_MONTH(cls):
                    return cls("last_day_of_this_month")
                
                @schemas.classproperty
                def THIS_YEAR(cls):
                    return cls("this_year")
                
                @schemas.classproperty
                def LAST_MONTH(cls):
                    return cls("last_month")
                
                @schemas.classproperty
                def LAST_THIRTY_DAYS(cls):
                    return cls("last_thirty_days")
                
                @schemas.classproperty
                def THIS_MONTH(cls):
                    return cls("this_month")
                
                @schemas.classproperty
                def YEAR_TO_DATE(cls):
                    return cls("year_to_date")
            __annotations__ = {
                "description": description,
                "id": id,
                "name": name,
                "author_first_name": author_first_name,
                "author_last_name": author_last_name,
                "type": type,
                "status": status,
                "start_date": start_date,
                "end_date": end_date,
                "created_at": created_at,
                "updated_at": updated_at,
                "data_refreshed_at": data_refreshed_at,
                "columns": columns,
                "filters": filters,
                "period_type": period_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_first_name"]) -> MetaOapg.properties.author_first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_last_name"]) -> MetaOapg.properties.author_last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_refreshed_at"]) -> MetaOapg.properties.data_refreshed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columns"]) -> 'PublicReportAttributesColumns': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filters"]) -> 'PublicReportAttributesFilters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["period_type"]) -> MetaOapg.properties.period_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "author_first_name", "author_last_name", "type", "status", "start_date", "end_date", "created_at", "updated_at", "data_refreshed_at", "columns", "filters", "period_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_first_name"]) -> typing.Union[MetaOapg.properties.author_first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_last_name"]) -> typing.Union[MetaOapg.properties.author_last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_refreshed_at"]) -> typing.Union[MetaOapg.properties.data_refreshed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> typing.Union['PublicReportAttributesColumns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filters"]) -> typing.Union['PublicReportAttributesFilters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["period_type"]) -> typing.Union[MetaOapg.properties.period_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "author_first_name", "author_last_name", "type", "status", "start_date", "end_date", "created_at", "updated_at", "data_refreshed_at", "columns", "filters", "period_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        author_first_name: typing.Union[MetaOapg.properties.author_first_name, str, schemas.Unset] = schemas.unset,
        author_last_name: typing.Union[MetaOapg.properties.author_last_name, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, date, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, date, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        data_refreshed_at: typing.Union[MetaOapg.properties.data_refreshed_at, str, datetime, schemas.Unset] = schemas.unset,
        columns: typing.Union['PublicReportAttributesColumns', schemas.Unset] = schemas.unset,
        filters: typing.Union['PublicReportAttributesFilters', schemas.Unset] = schemas.unset,
        period_type: typing.Union[MetaOapg.properties.period_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PublicReportAttributes':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            name=name,
            author_first_name=author_first_name,
            author_last_name=author_last_name,
            type=type,
            status=status,
            start_date=start_date,
            end_date=end_date,
            created_at=created_at,
            updated_at=updated_at,
            data_refreshed_at=data_refreshed_at,
            columns=columns,
            filters=filters,
            period_type=period_type,
            _configuration=_configuration,
            **kwargs,
        )

from personio_data_python_sdk.model.public_report_attributes_columns import PublicReportAttributesColumns
from personio_data_python_sdk.model.public_report_attributes_filters import PublicReportAttributesFilters
