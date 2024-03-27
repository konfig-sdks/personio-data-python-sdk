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


class DocumentUploadFailedWithBadDocumentCategoryResponse(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    success = schemas.BoolSchema
                    
                    
                    class error(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                message = schemas.StrSchema
                                code = schemas.IntSchema
                                __annotations__ = {
                                    "message": message,
                                    "code": code,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "code", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "code", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
                            code: typing.Union[MetaOapg.properties.code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'error':
                            return super().__new__(
                                cls,
                                *args,
                                message=message,
                                code=code,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "success": success,
                        "error": error,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["success", "error", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> typing.Union[MetaOapg.properties.success, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["success", "error", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                success: typing.Union[MetaOapg.properties.success, bool, schemas.Unset] = schemas.unset,
                error: typing.Union[MetaOapg.properties.error, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    success=success,
                    error=error,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.all_of_0,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentUploadFailedWithBadDocumentCategoryResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
