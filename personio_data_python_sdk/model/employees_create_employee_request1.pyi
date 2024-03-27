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


class EmployeesCreateEmployeeRequest1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "employee[last_name]",
            "employee[email]",
            "employee[first_name]",
        }
        
        class properties:
            employee_email = schemas.StrSchema
            employee_first_name = schemas.StrSchema
            employee_last_name = schemas.StrSchema
            employee_preferred_name = schemas.StrSchema
            
            
            class employee_gender(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("male")
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("female")
                
                @schemas.classproperty
                def DIVERSE(cls):
                    return cls("diverse")
            employee_position = schemas.StrSchema
            employee_department = schemas.StrSchema
            
            
            class employee_hire_date(
                schemas.DateSchema
            ):
                pass
            employee_weekly_working_hours = schemas.NumberSchema
            employee_supervisor_id = schemas.NumberSchema
            
            
            class employee_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ONBOARDING(cls):
                    return cls("onboarding")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def LEAVE(cls):
                    return cls("leave")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("inactive")
            __annotations__ = {
                "employee[email]": employee_email,
                "employee[first_name]": employee_first_name,
                "employee[last_name]": employee_last_name,
                "employee[preferred_name]": employee_preferred_name,
                "employee[gender]": employee_gender,
                "employee[position]": employee_position,
                "employee[department]": employee_department,
                "employee[hire_date]": employee_hire_date,
                "employee[weekly_working_hours]": employee_weekly_working_hours,
                "employee[supervisor_id]": employee_supervisor_id,
                "employee[status]": employee_status,
            }
    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[email]"]) -> MetaOapg.properties.employee_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[first_name]"]) -> MetaOapg.properties.employee_first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[last_name]"]) -> MetaOapg.properties.employee_last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[preferred_name]"]) -> MetaOapg.properties.employee_preferred_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[gender]"]) -> MetaOapg.properties.employee_gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[position]"]) -> MetaOapg.properties.employee_position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[department]"]) -> MetaOapg.properties.employee_department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[hire_date]"]) -> MetaOapg.properties.employee_hire_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[weekly_working_hours]"]) -> MetaOapg.properties.employee_weekly_working_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[supervisor_id]"]) -> MetaOapg.properties.employee_supervisor_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee[status]"]) -> MetaOapg.properties.employee_status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employee[email]", "employee[first_name]", "employee[last_name]", "employee[preferred_name]", "employee[gender]", "employee[position]", "employee[department]", "employee[hire_date]", "employee[weekly_working_hours]", "employee[supervisor_id]", "employee[status]", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[email]"]) -> MetaOapg.properties.employee_email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[first_name]"]) -> MetaOapg.properties.employee_first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[last_name]"]) -> MetaOapg.properties.employee_last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[preferred_name]"]) -> typing.Union[MetaOapg.properties.employee_preferred_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[gender]"]) -> typing.Union[MetaOapg.properties.employee_gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[position]"]) -> typing.Union[MetaOapg.properties.employee_position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[department]"]) -> typing.Union[MetaOapg.properties.employee_department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[hire_date]"]) -> typing.Union[MetaOapg.properties.employee_hire_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[weekly_working_hours]"]) -> typing.Union[MetaOapg.properties.employee_weekly_working_hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[supervisor_id]"]) -> typing.Union[MetaOapg.properties.employee_supervisor_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee[status]"]) -> typing.Union[MetaOapg.properties.employee_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employee[email]", "employee[first_name]", "employee[last_name]", "employee[preferred_name]", "employee[gender]", "employee[position]", "employee[department]", "employee[hire_date]", "employee[weekly_working_hours]", "employee[supervisor_id]", "employee[status]", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeesCreateEmployeeRequest1':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
