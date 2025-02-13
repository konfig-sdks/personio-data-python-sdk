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


class TypeEnum(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "standard": "STANDARD",
            "date": "DATE",
            "integer": "INTEGER",
            "decimal": "DECIMAL",
            "list": "LIST",
            "link": "LINK",
            "tags": "TAGS",
            "multiline": "MULTILINE",
        }
    
    @schemas.classproperty
    def STANDARD(cls):
        return cls("standard")
    
    @schemas.classproperty
    def DATE(cls):
        return cls("date")
    
    @schemas.classproperty
    def INTEGER(cls):
        return cls("integer")
    
    @schemas.classproperty
    def DECIMAL(cls):
        return cls("decimal")
    
    @schemas.classproperty
    def LIST(cls):
        return cls("list")
    
    @schemas.classproperty
    def LINK(cls):
        return cls("link")
    
    @schemas.classproperty
    def TAGS(cls):
        return cls("tags")
    
    @schemas.classproperty
    def MULTILINE(cls):
        return cls("multiline")
