# coding: utf-8

"""
    Personnel Data

    API for reading and writing personnel data including data about attendances, absences, documents, etc

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from personio_data_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from personio_data_python_sdk.api_response import AsyncGeneratorResponse
from personio_data_python_sdk import api_client, exceptions
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

from personio_data_python_sdk.model.document_upload_failed_with_unsupported_file_type_response import DocumentUploadFailedWithUnsupportedFileTypeResponse as DocumentUploadFailedWithUnsupportedFileTypeResponseSchema
from personio_data_python_sdk.model.document_upload_success_response import DocumentUploadSuccessResponse as DocumentUploadSuccessResponseSchema
from personio_data_python_sdk.model.document_upload_failed_with_bad_document_category_response import DocumentUploadFailedWithBadDocumentCategoryResponse as DocumentUploadFailedWithBadDocumentCategoryResponseSchema
from personio_data_python_sdk.model.document_upload_request import DocumentUploadRequest as DocumentUploadRequestSchema

from personio_data_python_sdk.type.document_upload_request import DocumentUploadRequest
from personio_data_python_sdk.type.document_upload_failed_with_bad_document_category_response import DocumentUploadFailedWithBadDocumentCategoryResponse
from personio_data_python_sdk.type.document_upload_success_response import DocumentUploadSuccessResponse
from personio_data_python_sdk.type.document_upload_failed_with_unsupported_file_type_response import DocumentUploadFailedWithUnsupportedFileTypeResponse

from ...api_client import Dictionary
from personio_data_python_sdk.pydantic.document_upload_failed_with_unsupported_file_type_response import DocumentUploadFailedWithUnsupportedFileTypeResponse as DocumentUploadFailedWithUnsupportedFileTypeResponsePydantic
from personio_data_python_sdk.pydantic.document_upload_success_response import DocumentUploadSuccessResponse as DocumentUploadSuccessResponsePydantic
from personio_data_python_sdk.pydantic.document_upload_request import DocumentUploadRequest as DocumentUploadRequestPydantic
from personio_data_python_sdk.pydantic.document_upload_failed_with_bad_document_category_response import DocumentUploadFailedWithBadDocumentCategoryResponse as DocumentUploadFailedWithBadDocumentCategoryResponsePydantic

# Header params
XPersonioPartnerIDSchema = schemas.StrSchema
XPersonioAppIDSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'X-Personio-Partner-ID': typing.Union[XPersonioPartnerIDSchema, str, ],
        'X-Personio-App-ID': typing.Union[XPersonioAppIDSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_personio_partner_id = api_client.HeaderParameter(
    name="X-Personio-Partner-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XPersonioPartnerIDSchema,
)
request_header_x_personio_app_id = api_client.HeaderParameter(
    name="X-Personio-App-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XPersonioAppIDSchema,
)
# body param
SchemaForRequestBodyMultipartFormData = DocumentUploadRequestSchema


request_body_document_upload_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
SchemaFor201ResponseBodyApplicationJson = DocumentUploadSuccessResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: DocumentUploadSuccessResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: DocumentUploadSuccessResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = DocumentUploadFailedWithBadDocumentCategoryResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: DocumentUploadFailedWithBadDocumentCategoryResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: DocumentUploadFailedWithBadDocumentCategoryResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = DocumentUploadFailedWithUnsupportedFileTypeResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: DocumentUploadFailedWithUnsupportedFileTypeResponse


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: DocumentUploadFailedWithUnsupportedFileTypeResponse


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _upload_for_employees_mapped_args(
        self,
        title: str,
        employee_id: int,
        category_id: int,
        file: typing.IO,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if comment is not None:
            _body["comment"] = comment
        if employee_id is not None:
            _body["employee_id"] = employee_id
        if category_id is not None:
            _body["category_id"] = category_id
        if date is not None:
            _body["date"] = date
        if file is not None:
            _body["file"] = file
        args.body = _body
        if x_personio_partner_id is not None:
            _header_params["X-Personio-Partner-ID"] = x_personio_partner_id
        if x_personio_app_id is not None:
            _header_params["X-Personio-App-ID"] = x_personio_app_id
        args.header = _header_params
        return args

    async def _aupload_for_employees_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_personio_partner_id,
            request_header_x_personio_app_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/documents',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_document_upload_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _upload_for_employees_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_personio_partner_id,
            request_header_x_personio_app_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/documents',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_document_upload_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UploadForEmployeesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupload_for_employees(
        self,
        title: str,
        employee_id: int,
        category_id: int,
        file: typing.IO,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_for_employees_mapped_args(
            title=title,
            employee_id=employee_id,
            category_id=category_id,
            file=file,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            comment=comment,
            date=date,
        )
        return await self._aupload_for_employees_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def upload_for_employees(
        self,
        title: str,
        employee_id: int,
        category_id: int,
        file: typing.IO,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_for_employees_mapped_args(
            title=title,
            employee_id=employee_id,
            category_id=category_id,
            file=file,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            comment=comment,
            date=date,
        )
        return self._upload_for_employees_oapg(
            body=args.body,
            header_params=args.header,
        )

class UploadForEmployees(BaseApi):

    async def aupload_for_employees(
        self,
        title: str,
        employee_id: int,
        category_id: int,
        file: typing.IO,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        validate: bool = False,
        **kwargs,
    ) -> DocumentUploadSuccessResponsePydantic:
        raw_response = await self.raw.aupload_for_employees(
            title=title,
            employee_id=employee_id,
            category_id=category_id,
            file=file,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            comment=comment,
            date=date,
            **kwargs,
        )
        if validate:
            return RootModel[DocumentUploadSuccessResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(DocumentUploadSuccessResponsePydantic, raw_response.body)
    
    
    def upload_for_employees(
        self,
        title: str,
        employee_id: int,
        category_id: int,
        file: typing.IO,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        validate: bool = False,
    ) -> DocumentUploadSuccessResponsePydantic:
        raw_response = self.raw.upload_for_employees(
            title=title,
            employee_id=employee_id,
            category_id=category_id,
            file=file,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            comment=comment,
            date=date,
        )
        if validate:
            return RootModel[DocumentUploadSuccessResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(DocumentUploadSuccessResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        title: str,
        employee_id: int,
        category_id: int,
        file: typing.IO,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_for_employees_mapped_args(
            title=title,
            employee_id=employee_id,
            category_id=category_id,
            file=file,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            comment=comment,
            date=date,
        )
        return await self._aupload_for_employees_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        title: str,
        employee_id: int,
        category_id: int,
        file: typing.IO,
        x_personio_partner_id: typing.Optional[str] = None,
        x_personio_app_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_for_employees_mapped_args(
            title=title,
            employee_id=employee_id,
            category_id=category_id,
            file=file,
            x_personio_partner_id=x_personio_partner_id,
            x_personio_app_id=x_personio_app_id,
            comment=comment,
            date=date,
        )
        return self._upload_for_employees_oapg(
            body=args.body,
            header_params=args.header,
        )

