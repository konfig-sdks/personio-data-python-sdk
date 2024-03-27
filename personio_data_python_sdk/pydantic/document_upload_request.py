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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class DocumentUploadRequest(BaseModel):
    # Title of the document. Maximum length is 255 characters.
    title: str = Field(alias='title')

    # Employee identifier
    employee_id: int = Field(alias='employee_id')

    # Document Category identifier
    category_id: int = Field(alias='category_id')

    # The document that shall be uploaded to an employees profile. Maximum file size is 30MB.
    file: typing.IO = Field(alias='file')

    # Optional comment that can be added to the uploaded document.
    comment: typing.Optional[str] = Field(None, alias='comment')

    # Optional date can be added to the uploaded document. Must follow the format: Y-m-d
    date: typing.Optional[date] = Field(None, alias='date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
