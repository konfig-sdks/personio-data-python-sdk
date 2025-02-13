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


class PublicListColumnsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            success = schemas.BoolSchema
        
            @staticmethod
            def metadata() -> typing.Type['PublicReportMetaData']:
                return PublicReportMetaData
            offset = schemas.IntSchema
            limit = schemas.IntSchema
        
            @staticmethod
            def data() -> typing.Type['PublicColumnData']:
                return PublicColumnData
            __annotations__ = {
                "success": success,
                "metadata": metadata,
                "offset": offset,
                "limit": limit,
                "data": data,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'PublicReportMetaData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'PublicColumnData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["success", "metadata", "offset", "limit", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> typing.Union[MetaOapg.properties.success, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['PublicReportMetaData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> typing.Union[MetaOapg.properties.offset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> typing.Union[MetaOapg.properties.limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['PublicColumnData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["success", "metadata", "offset", "limit", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        success: typing.Union[MetaOapg.properties.success, bool, schemas.Unset] = schemas.unset,
        metadata: typing.Union['PublicReportMetaData', schemas.Unset] = schemas.unset,
        offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        data: typing.Union['PublicColumnData', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PublicListColumnsResponse':
        return super().__new__(
            cls,
            *args,
            success=success,
            metadata=metadata,
            offset=offset,
            limit=limit,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from personio_data_python_sdk.model.public_column_data import PublicColumnData
from personio_data_python_sdk.model.public_report_meta_data import PublicReportMetaData
