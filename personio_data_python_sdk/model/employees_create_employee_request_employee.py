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


class EmployeesCreateEmployeeRequestEmployee(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "last_name",
            "first_name",
            "email",
        }
        
        class properties:
            email = schemas.StrSchema
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            preferred_name = schemas.StrSchema
            gender = schemas.StrSchema
            position = schemas.StrSchema
            subcompany = schemas.StrSchema
            department = schemas.StrSchema
            office = schemas.StrSchema
            
            
            class hire_date(
                schemas.DateSchema
            ):
            
            
                class MetaOapg:
                    format = 'date'
                    regex=[{
                        'pattern': r'^\d{4}-\d{2}-\d{2}$',
                    }]
            weekly_working_hours = schemas.NumberSchema
            status = schemas.StrSchema
            supervisor_id = schemas.NumberSchema
        
            @staticmethod
            def custom_attributes() -> typing.Type['EmployeesCreateEmployeeRequestEmployeeCustomAttributes']:
                return EmployeesCreateEmployeeRequestEmployeeCustomAttributes
            __annotations__ = {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "preferred_name": preferred_name,
                "gender": gender,
                "position": position,
                "subcompany": subcompany,
                "department": department,
                "office": office,
                "hire_date": hire_date,
                "weekly_working_hours": weekly_working_hours,
                "status": status,
                "supervisor_id": supervisor_id,
                "custom_attributes": custom_attributes,
            }
    
    last_name: MetaOapg.properties.last_name
    first_name: MetaOapg.properties.first_name
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferred_name"]) -> MetaOapg.properties.preferred_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subcompany"]) -> MetaOapg.properties.subcompany: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> MetaOapg.properties.department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["office"]) -> MetaOapg.properties.office: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hire_date"]) -> MetaOapg.properties.hire_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekly_working_hours"]) -> MetaOapg.properties.weekly_working_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supervisor_id"]) -> MetaOapg.properties.supervisor_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_attributes"]) -> 'EmployeesCreateEmployeeRequestEmployeeCustomAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "first_name", "last_name", "preferred_name", "gender", "position", "subcompany", "department", "office", "hire_date", "weekly_working_hours", "status", "supervisor_id", "custom_attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferred_name"]) -> typing.Union[MetaOapg.properties.preferred_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subcompany"]) -> typing.Union[MetaOapg.properties.subcompany, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> typing.Union[MetaOapg.properties.department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["office"]) -> typing.Union[MetaOapg.properties.office, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hire_date"]) -> typing.Union[MetaOapg.properties.hire_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekly_working_hours"]) -> typing.Union[MetaOapg.properties.weekly_working_hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supervisor_id"]) -> typing.Union[MetaOapg.properties.supervisor_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_attributes"]) -> typing.Union['EmployeesCreateEmployeeRequestEmployeeCustomAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "first_name", "last_name", "preferred_name", "gender", "position", "subcompany", "department", "office", "hire_date", "weekly_working_hours", "status", "supervisor_id", "custom_attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        last_name: typing.Union[MetaOapg.properties.last_name, str, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        preferred_name: typing.Union[MetaOapg.properties.preferred_name, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        position: typing.Union[MetaOapg.properties.position, str, schemas.Unset] = schemas.unset,
        subcompany: typing.Union[MetaOapg.properties.subcompany, str, schemas.Unset] = schemas.unset,
        department: typing.Union[MetaOapg.properties.department, str, schemas.Unset] = schemas.unset,
        office: typing.Union[MetaOapg.properties.office, str, schemas.Unset] = schemas.unset,
        hire_date: typing.Union[MetaOapg.properties.hire_date, str, date, schemas.Unset] = schemas.unset,
        weekly_working_hours: typing.Union[MetaOapg.properties.weekly_working_hours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        supervisor_id: typing.Union[MetaOapg.properties.supervisor_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        custom_attributes: typing.Union['EmployeesCreateEmployeeRequestEmployeeCustomAttributes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeesCreateEmployeeRequestEmployee':
        return super().__new__(
            cls,
            *args,
            last_name=last_name,
            first_name=first_name,
            email=email,
            preferred_name=preferred_name,
            gender=gender,
            position=position,
            subcompany=subcompany,
            department=department,
            office=office,
            hire_date=hire_date,
            weekly_working_hours=weekly_working_hours,
            status=status,
            supervisor_id=supervisor_id,
            custom_attributes=custom_attributes,
            _configuration=_configuration,
            **kwargs,
        )

from personio_data_python_sdk.model.employees_create_employee_request_employee_custom_attributes import EmployeesCreateEmployeeRequestEmployeeCustomAttributes
