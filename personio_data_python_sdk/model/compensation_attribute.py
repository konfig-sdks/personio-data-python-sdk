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


class CompensationAttribute(
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
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "COMPENSATION": "COMPENSATION",
                    }
                
                @schemas.classproperty
                def COMPENSATION(cls):
                    return cls("COMPENSATION")
            amount = schemas.StrSchema
            currency_code = schemas.StrSchema
            currency_symbol = schemas.StrSchema
            overtime_hours = schemas.StrSchema
            bonus_type = schemas.StrSchema
            employee_id = schemas.IntSchema
            __annotations__ = {
                "attribute_id": attribute_id,
                "data_type": data_type,
                "amount": amount,
                "currency_code": currency_code,
                "currency_symbol": currency_symbol,
                "overtime_hours": overtime_hours,
                "bonus_type": bonus_type,
                "employee_id": employee_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attribute_id"]) -> MetaOapg.properties.attribute_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_type"]) -> MetaOapg.properties.data_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_symbol"]) -> MetaOapg.properties.currency_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overtime_hours"]) -> MetaOapg.properties.overtime_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bonus_type"]) -> MetaOapg.properties.bonus_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_id"]) -> MetaOapg.properties.employee_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attribute_id", "data_type", "amount", "currency_code", "currency_symbol", "overtime_hours", "bonus_type", "employee_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attribute_id"]) -> typing.Union[MetaOapg.properties.attribute_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_type"]) -> typing.Union[MetaOapg.properties.data_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_symbol"]) -> typing.Union[MetaOapg.properties.currency_symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overtime_hours"]) -> typing.Union[MetaOapg.properties.overtime_hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bonus_type"]) -> typing.Union[MetaOapg.properties.bonus_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_id"]) -> typing.Union[MetaOapg.properties.employee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attribute_id", "data_type", "amount", "currency_code", "currency_symbol", "overtime_hours", "bonus_type", "employee_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        attribute_id: typing.Union[MetaOapg.properties.attribute_id, str, schemas.Unset] = schemas.unset,
        data_type: typing.Union[MetaOapg.properties.data_type, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_symbol: typing.Union[MetaOapg.properties.currency_symbol, str, schemas.Unset] = schemas.unset,
        overtime_hours: typing.Union[MetaOapg.properties.overtime_hours, str, schemas.Unset] = schemas.unset,
        bonus_type: typing.Union[MetaOapg.properties.bonus_type, str, schemas.Unset] = schemas.unset,
        employee_id: typing.Union[MetaOapg.properties.employee_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompensationAttribute':
        return super().__new__(
            cls,
            *args,
            attribute_id=attribute_id,
            data_type=data_type,
            amount=amount,
            currency_code=currency_code,
            currency_symbol=currency_symbol,
            overtime_hours=overtime_hours,
            bonus_type=bonus_type,
            employee_id=employee_id,
            _configuration=_configuration,
            **kwargs,
        )
