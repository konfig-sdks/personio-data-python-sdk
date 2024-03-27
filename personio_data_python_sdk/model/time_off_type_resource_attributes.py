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


class TimeOffTypeResourceAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            name = schemas.StrSchema
            
            
            class category(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "family_care": "FAMILY_CARE",
                        "maternity_parental_leave": "MATERNITY_PARENTAL_LEAVE",
                        "child_care": "CHILD_CARE",
                        "short_time_allowance": "SHORT_TIME_ALLOWANCE",
                        "quarantine": "QUARANTINE",
                        "lockout": "LOCKOUT",
                        "irrevocable_exemption": "IRREVOCABLE_EXEMPTION",
                        "sick_leave": "SICK_LEAVE",
                        "voluntary_military_service": "VOLUNTARY_MILITARY_SERVICE",
                        "unlawful_strike": "UNLAWFUL_STRIKE",
                        "lawful_strike": "LAWFUL_STRIKE",
                        "paid_vacation": "PAID_VACATION",
                        "unpaid_vacation": "UNPAID_VACATION",
                        "unexcused_absence": "UNEXCUSED_ABSENCE",
                        "offsite_work": "OFFSITE_WORK",
                        "other": "OTHER",
                        "undefined": "UNDEFINED",
                    }
                
                @schemas.classproperty
                def FAMILY_CARE(cls):
                    return cls("family_care")
                
                @schemas.classproperty
                def MATERNITY_PARENTAL_LEAVE(cls):
                    return cls("maternity_parental_leave")
                
                @schemas.classproperty
                def CHILD_CARE(cls):
                    return cls("child_care")
                
                @schemas.classproperty
                def SHORT_TIME_ALLOWANCE(cls):
                    return cls("short_time_allowance")
                
                @schemas.classproperty
                def QUARANTINE(cls):
                    return cls("quarantine")
                
                @schemas.classproperty
                def LOCKOUT(cls):
                    return cls("lockout")
                
                @schemas.classproperty
                def IRREVOCABLE_EXEMPTION(cls):
                    return cls("irrevocable_exemption")
                
                @schemas.classproperty
                def SICK_LEAVE(cls):
                    return cls("sick_leave")
                
                @schemas.classproperty
                def VOLUNTARY_MILITARY_SERVICE(cls):
                    return cls("voluntary_military_service")
                
                @schemas.classproperty
                def UNLAWFUL_STRIKE(cls):
                    return cls("unlawful_strike")
                
                @schemas.classproperty
                def LAWFUL_STRIKE(cls):
                    return cls("lawful_strike")
                
                @schemas.classproperty
                def PAID_VACATION(cls):
                    return cls("paid_vacation")
                
                @schemas.classproperty
                def UNPAID_VACATION(cls):
                    return cls("unpaid_vacation")
                
                @schemas.classproperty
                def UNEXCUSED_ABSENCE(cls):
                    return cls("unexcused_absence")
                
                @schemas.classproperty
                def OFFSITE_WORK(cls):
                    return cls("offsite_work")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
                
                @schemas.classproperty
                def UNDEFINED(cls):
                    return cls("undefined")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'category':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class legacy_category(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "family_care_sick_leave": "FAMILY_CARE_SICK_LEAVE",
                        "individual_prohibition_of_employment": "INDIVIDUAL_PROHIBITION_OF_EMPLOYMENT",
                        "maternity_protection_period": "MATERNITY_PROTECTION_PERIOD",
                        "other": "OTHER",
                        "paid_vacation": "PAID_VACATION",
                        "parental_leave": "PARENTAL_LEAVE",
                        "sick_leave": "SICK_LEAVE",
                        "lawful_strike": "LAWFUL_STRIKE",
                        "unlawful_strike": "UNLAWFUL_STRIKE",
                        "treatment": "TREATMENT",
                        "unexcused_absence": "UNEXCUSED_ABSENCE",
                        "unpaid_vacation": "UNPAID_VACATION",
                        "voluntary_military_service": "VOLUNTARY_MILITARY_SERVICE",
                        "offsite_work": "OFFSITE_WORK",
                        "family_care_long_term": "FAMILY_CARE_LONG_TERM",
                        "paid_child_sick": "PAID_CHILD_SICK",
                        "unpaid_child_sick": "UNPAID_CHILD_SICK",
                        "undefined": "UNDEFINED",
                    }
                
                @schemas.classproperty
                def FAMILY_CARE_SICK_LEAVE(cls):
                    return cls("family_care_sick_leave")
                
                @schemas.classproperty
                def INDIVIDUAL_PROHIBITION_OF_EMPLOYMENT(cls):
                    return cls("individual_prohibition_of_employment")
                
                @schemas.classproperty
                def MATERNITY_PROTECTION_PERIOD(cls):
                    return cls("maternity_protection_period")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
                
                @schemas.classproperty
                def PAID_VACATION(cls):
                    return cls("paid_vacation")
                
                @schemas.classproperty
                def PARENTAL_LEAVE(cls):
                    return cls("parental_leave")
                
                @schemas.classproperty
                def SICK_LEAVE(cls):
                    return cls("sick_leave")
                
                @schemas.classproperty
                def LAWFUL_STRIKE(cls):
                    return cls("lawful_strike")
                
                @schemas.classproperty
                def UNLAWFUL_STRIKE(cls):
                    return cls("unlawful_strike")
                
                @schemas.classproperty
                def TREATMENT(cls):
                    return cls("treatment")
                
                @schemas.classproperty
                def UNEXCUSED_ABSENCE(cls):
                    return cls("unexcused_absence")
                
                @schemas.classproperty
                def UNPAID_VACATION(cls):
                    return cls("unpaid_vacation")
                
                @schemas.classproperty
                def VOLUNTARY_MILITARY_SERVICE(cls):
                    return cls("voluntary_military_service")
                
                @schemas.classproperty
                def OFFSITE_WORK(cls):
                    return cls("offsite_work")
                
                @schemas.classproperty
                def FAMILY_CARE_LONG_TERM(cls):
                    return cls("family_care_long_term")
                
                @schemas.classproperty
                def PAID_CHILD_SICK(cls):
                    return cls("paid_child_sick")
                
                @schemas.classproperty
                def UNPAID_CHILD_SICK(cls):
                    return cls("unpaid_child_sick")
                
                @schemas.classproperty
                def UNDEFINED(cls):
                    return cls("undefined")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'legacy_category':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class unit(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "day": "DAY",
                        "hour": "HOUR",
                    }
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("day")
                
                @schemas.classproperty
                def HOUR(cls):
                    return cls("hour")
            half_day_requests_enabled = schemas.BoolSchema
            certification_required = schemas.BoolSchema
            certification_submission_timeframe = schemas.IntSchema
            
            
            class substitute_option(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "disabled": "DISABLED",
                        "optional": "OPTIONAL",
                        "required": "REQUIRED",
                    }
                
                @schemas.classproperty
                def DISABLED(cls):
                    return cls("disabled")
                
                @schemas.classproperty
                def OPTIONAL(cls):
                    return cls("optional")
                
                @schemas.classproperty
                def REQUIRED(cls):
                    return cls("required")
            approval_required = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "category": category,
                "legacy_category": legacy_category,
                "unit": unit,
                "half_day_requests_enabled": half_day_requests_enabled,
                "certification_required": certification_required,
                "certification_submission_timeframe": certification_submission_timeframe,
                "substitute_option": substitute_option,
                "approval_required": approval_required,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legacy_category"]) -> MetaOapg.properties.legacy_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["half_day_requests_enabled"]) -> MetaOapg.properties.half_day_requests_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["certification_required"]) -> MetaOapg.properties.certification_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["certification_submission_timeframe"]) -> MetaOapg.properties.certification_submission_timeframe: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["substitute_option"]) -> MetaOapg.properties.substitute_option: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approval_required"]) -> MetaOapg.properties.approval_required: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "category", "legacy_category", "unit", "half_day_requests_enabled", "certification_required", "certification_submission_timeframe", "substitute_option", "approval_required", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legacy_category"]) -> typing.Union[MetaOapg.properties.legacy_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> typing.Union[MetaOapg.properties.unit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["half_day_requests_enabled"]) -> typing.Union[MetaOapg.properties.half_day_requests_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["certification_required"]) -> typing.Union[MetaOapg.properties.certification_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["certification_submission_timeframe"]) -> typing.Union[MetaOapg.properties.certification_submission_timeframe, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["substitute_option"]) -> typing.Union[MetaOapg.properties.substitute_option, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approval_required"]) -> typing.Union[MetaOapg.properties.approval_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "category", "legacy_category", "unit", "half_day_requests_enabled", "certification_required", "certification_submission_timeframe", "substitute_option", "approval_required", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, None, str, schemas.Unset] = schemas.unset,
        legacy_category: typing.Union[MetaOapg.properties.legacy_category, None, str, schemas.Unset] = schemas.unset,
        unit: typing.Union[MetaOapg.properties.unit, str, schemas.Unset] = schemas.unset,
        half_day_requests_enabled: typing.Union[MetaOapg.properties.half_day_requests_enabled, bool, schemas.Unset] = schemas.unset,
        certification_required: typing.Union[MetaOapg.properties.certification_required, bool, schemas.Unset] = schemas.unset,
        certification_submission_timeframe: typing.Union[MetaOapg.properties.certification_submission_timeframe, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        substitute_option: typing.Union[MetaOapg.properties.substitute_option, str, schemas.Unset] = schemas.unset,
        approval_required: typing.Union[MetaOapg.properties.approval_required, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeOffTypeResourceAttributes':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            category=category,
            legacy_category=legacy_category,
            unit=unit,
            half_day_requests_enabled=half_day_requests_enabled,
            certification_required=certification_required,
            certification_submission_timeframe=certification_submission_timeframe,
            substitute_option=substitute_option,
            approval_required=approval_required,
            _configuration=_configuration,
            **kwargs,
        )
